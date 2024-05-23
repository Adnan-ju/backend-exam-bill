# from django.db import models

# class Choices(models.TextChoices):
#         Theory='Theory' ,'T'
#         Lab='Lab', 'L'
#         Project='Project','P'
       
# # Create your models here.
# class Course(models.Model):

#     course_id=models.CharField(max_length=10)
#     course_name=models.CharField(max_length=40)
#     course_credit=models.DecimalField(max_digits=4,decimal_places=2)
#     tutorial_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
#     att_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
#     final_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
#     choice = models.CharField( max_length=20,choices=Choices.choices,default=Choices.Theory)

          
#     def __str__(self):
#         return self.course_id + " : " + self.course_name

from django.db import models

# Create your models here.

CourseType=( 
    ('Theory', 'Theory'), 
    ('Laboratory', 'Laboratory'), 
    ('Project', 'Project') 
)

class Course(models.Model):
    course_id=models.CharField(max_length=10)
    course_name=models.CharField(max_length=40)
    course_type=models.CharField(choices= CourseType ,max_length=40,default='Theory')
    credit=models.DecimalField(max_digits=4,decimal_places=2)
    tutorial_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    att_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    final_full_marks=models.DecimalField(max_digits=4,decimal_places=2)
    
    def __str__(self):
        return self.course_id + ': ' + self.course_name
class Student(models.Model):
    Stu_id=models.IntegerField(unique=True)
    name=models.CharField(max_length=40)
    stu_exam_roll=models.IntegerField()
    courses = models.ManyToManyField(Course ,blank=True )