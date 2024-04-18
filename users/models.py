from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models
from datetime import datetime
from typing import Any
from collections.abc import Collection

from aaa_api.choices import *

class CustomUserManager(UserManager):
    def create_user(self, username: str, email: str | None = None, password: str | None = None, **extra_fields) -> Any:
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username: str, email: str | None = None, password: str | None = None, **extra_fields) -> Any:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)
    
    
class CustomUser(AbstractUser):
    # Login
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=255, unique=True)

    # for profile
    first_name = models.CharField(max_length=255, null = True, blank=True)
    last_name = models.CharField(max_length=255, null = True, blank=True)

    # Permissions
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()
        
    def __str__(self) -> str:
        return f'{self.username}'
    
    def has_module_perms(self, app_label: str) -> bool:
        return self.is_superuser
    
    def has_perms(self, perm_list: Collection[str]) -> bool:
        return self.is_superuser
    
    