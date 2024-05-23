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



class Rate(models.Model):
    OPTION_CHOICES = [
        ('Making Question Paper', 'প্রশ্নপত্র প্রণয়ন'),
        ('Evaluating Answer Scripts', 'উত্তরপত্র মূল্যায়ন'),
        ('Lab Exam', 'ব্যবহারিক পরীক্ষা'),
        ('Viva Exam', 'মৌখিক পরীক্ষা'),
        ('Question Moderation', 'প্রশ্নপত্র মডারেশন'),
        ('Stencil', 'স্টেনসিল কাটা'),
        ('Translation', 'অনুবাদ'),
        ('Thesis/Project/Report Evaluation', 'থিসিস/প্রজেক্ট/রিপোর্ট মূল্যায়ন'),
        ('Practice', 'অনুশীলনী'),
        ('Tabulation', 'টেবুলেশন'),
        ('Exam Committee Chief_s Remuneration', 'কমিটির সভাপতির পারিতোষিক'),
        ('Remuneration of Supervisor(M.Phil/PhD)', 'তত্ত্বাবধায়ক সম্মানী(এম. ফিল/ পিএইচ.ডি'),
        # Add more options as needed
    ]

    

    name = models.CharField(max_length=100, choices=OPTION_CHOICES)
    # name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    value = models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):
        return f"{self.name} - {self.category}"
    

class Result(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    courses = models.TextField()  # Store courses as a comma-separated string
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class ExamCommittee(models.Model):
    year=models.CharField(max_length=100)
    session=models.CharField(max_length=100)
    committee_chief = models.CharField(max_length=100)
    member_1=models.CharField(max_length=100)
    member_2=models.CharField(max_length=100)

class Routine(models.Model):
    teacher_name = models.CharField(max_length=100)
    semester = models.CharField(max_length=20)
    courses = models.TextField()  # Comma-separated list of courses

    def __str__(self):
        return f"{self.teacher_name} - {self.semester}"

class YourModel(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)

# class Result(models.Model):
#     name = models.CharField(max_length=100)
#     semester = models.CharField(max_length=20)
#     courses = models.TextField()  # Store courses as a comma-separated string

class Result(models.Model):
    name = models.CharField(max_length=100)
    semester = models.CharField(max_length=100)
    
    results = models.JSONField(default=dict)
    total_result = models.DecimalField(max_digits=10, decimal_places=2)  # Adjust as needed

    def __str__(self):
        return f"{self.name} - {self.semester}"    

##CHANGE##
##CHANGE##
class FacultyMember(models.Model):
    RANK_CHOICES = [
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
    ]

    name = models.CharField(max_length=100)
    image = models.URLField()
    rank = models.CharField(max_length=100, choices=RANK_CHOICES)
    bank_account_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    
    