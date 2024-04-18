from django.db import models

class Goal(models.Model):
    goal = models.TextField()    
    
    def __str__(self):
        return f'{self.goal}'
    
    
class Objective(models.Model):
    objective = models.TextField()    

    def __str__(self):
        return f'{self.objective}'


class Interest(models.Model):
    interest = models.TextField()    

    def __str__(self):
        return f'{self.interest}'


class Hobby(models.Model):
    hobby = models.TextField()    

    def __str__(self):
        return f'{self.hobby}'
    

class Links(models.Model):
    links = models.URLField()    

    def __str__(self):
        return f'{self.links}'
