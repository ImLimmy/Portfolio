from django.urls import path

from . import views

urlpatterns = [
    # User
    path('create/', views.UserCreate.as_view()),
    path('<int:pk>/', views.UserDetail.as_view()),
    
    # Login and Logout
    path('login/', views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
]