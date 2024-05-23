from django.db import models

# Create your models here.

class Student(models.Model):
    roll=models.IntegerField()
    name=models.CharField(max_length=50)
    department=models.CharField(max_length=40)

    def __str__(self):
        return self.name