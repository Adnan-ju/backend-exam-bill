from django import forms
from .models import Student,Course,Rate,ExamCommittee,FacultyMember
from django.forms import ChoiceField

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields= '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields= '__all__'        
        

class RateForm(forms.ModelForm):
    class Meta:
        model = Rate
        fields = '__all__'

class ExamCommitteeForm(forms.ModelForm):
    class Meta:
        model = ExamCommittee
        fields = '__all__'    

##CHANGE

class FacultyMemberForm(forms.ModelForm):
    class Meta:
        model = FacultyMember
        fields = '__all__'        