from django.db import models
from course.models import *

# Create your models here.
class Trainee (models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    age = models.IntegerField() 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="trainees")
    mentor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name="mentees") 

    def __str__(self):
        return self.name
