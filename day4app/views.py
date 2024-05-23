from django.shortcuts import render,redirect
from .models import FacultyMember, Student,Course,Result
from .forms import CourseForm, FacultyMemberForm,StudentForm,ExamCommitteeForm
from django.shortcuts import redirect, get_object_or_404
from .models import Rate,ExamCommittee
from .forms import RateForm
from django.http import JsonResponse
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import YourModel
from .serializer import YourModelSerializer,ResultSerializer
import csv

from rest_framework.decorators import api_view

# Create your views here.
def home(request):
    # context={}
    stus=Student.objects.all()
    # context['all_books']=books
    return render(request,'day4/home.html',{'all_student':stus})


def Chome(request):
    # context={}
    courses=Course.objects.all()
    # context['all_books']=books
    return render(request,'day4/chome.html',{'all_courses':courses})


def Rate_List(request):
    rates = Rate.objects.all()
    return render(request, 'rate_list.html', {'all_rates': rates})


def search_student(request):
    student_id = request.GET.get('student_id')
    student = None
    if student_id:
        try:
            student = Student.objects.get(Stu_id=student_id)
        except Student.DoesNotExist:
            pass
    return render(request, 'day4/search_student.html', {'student': student})



def register(request, student_id):
    from django.shortcuts import render, redirect 
from .models import Student, Course

def register(request, student_id):
    try:
        student = Student.objects.get(Stu_id=student_id)
    except Student.DoesNotExist:
        return redirect('home')  

    if request.method == 'POST':
        selected_courses_ids = request.POST.getlist('courses')
        selected_courses = Course.objects.filter(id__in=selected_courses_ids)
        student.courses.add(*selected_courses)
        return render(request, 'day4/search_student.html', {'student': student})
    else:
        registered_course_ids = student.courses.values_list('id', flat=True)
        remaining_courses = Course.objects.exclude(id__in=registered_course_ids)
        return render(request, 'day4/registration.html', {'student': student, 'remaining_courses': remaining_courses})


def remove(request,id):
    c=Course.objects.get(id=id)
    c.delete()
    return redirect(Chome)

def edit(request,id):
    course=Course.objects.get(id=id)
    cfrm = CourseForm(instance=course)
    #print('-----------'+request.method+'------------')
    if request.method=="POST":
        frm = CourseForm(request.POST, instance=course)
        if frm.is_valid():
            frm.save()
        return redirect(Chome)
    return render(request,'day4/edit.html',{'form':cfrm})

def add(request):
    frm = CourseForm()
    return render(request,'day4/add.html',{'form':frm})

def save(request):
    if request.method == 'POST':
        frm = CourseForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect(Chome)
    return redirect(Chome)
    
def remove_stu(request,id):
    c=Student.objects.get(id=id)
    c.delete()
    return redirect(home)

def edit_stu(request,id):
    s=Student.objects.get(id=id)
    sfrm = StudentForm(instance=s)
    #print('-----------'+request.method+'------------')
    if request.method=="POST":
        frm = StudentForm(request.POST, instance=s)
        if frm.is_valid():
            frm.save()
        return redirect(home)
    return render(request,'day4/edit_stu.html',{'form':sfrm})

def add_stu(request):
    frm = StudentForm()
    return render(request,'day4/add_stu.html',{'form':frm})

def save_stu(request):
    if request.method == 'POST':
        frm = StudentForm(request.POST)
        if frm.is_valid():
            frm.save()
            return redirect(home)
    return redirect(home)    


def remove_course(request, student_id, course_id):
    student = get_object_or_404(Student, id=student_id)
    course = get_object_or_404(Course, id=course_id)
    
    # Remove the course from the student's courses
    student.courses.remove(course)
    
    return render(request, 'day4/search_student.html', {'student': student})
def main(request):
    return render(request, 'day4/main.html')

def get_course_data(request):
    # Retrieve course data from the database
    courses = Course.objects.all().values()

    # Serialize the data into JSON format
    serialized_courses = list(courses)

    # Return the serialized data as a JSON response
    return JsonResponse(serialized_courses, safe=False)

# def get_courses(request):
#     if request.method == 'GET':
#         teacher_name = request.GET.get('teacher')
#         semester = request.GET.get('semester')
#         print(f"Received data - Teacher: {teacher_name}, Semester: {semester}")

#         courses = []

#         # Read the CSV file and filter the data based on the selected teacher's name and semester
#         with open('C:\\project_3_2\\web_lab\\myproject\\routine.csv', newline='') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
               
#                 print(row) 
#                 if row["Teacher's Name"] == teacher_name and row['Semester'] == semester:
#                     courses.extend(row['Courses'].split(','))

#         return JsonResponse({'courses': courses})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
# def get_courses(request):
#     if request.method == 'GET':
#         teacher_name = request.GET.get('teacher')
#         semester = request.GET.get('semester')
        

#         courses = []

       
#         with open('C:\\project_3_2\\routine.txt', 'r') as txtfile:
#             for line in txtfile:
#                 row = line.strip().split(',')  # Assuming the data is comma-separated
             
#                 if len(row) >= 3 and row[0] == teacher_name and row[1] == semester:
#                     courses.extend(row[2:])

#         return JsonResponse({'courses': courses})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})

def get_courses(request):
    if request.method == 'GET':
        teacher_name = request.GET.get('teacher')
        semester = request.GET.get('semester')

        courses = []

        # Read the TXT file and filter the data based on the selected teacher's name and semester
        with open('C:\\project_3_2\\routine.txt', 'r') as txtfile:
            for line in txtfile:
                row = line.strip().split(',')  # Assuming the data is comma-separated
             
                if len(row) >= 3 and row[0] == teacher_name and row[1] == semester:
                    courses.extend(filter(lambda x: x.strip() != '', row[2:]))

        return JsonResponse({'courses': courses})
    else:
        return JsonResponse({'error': 'Invalid request method'})


def get_rates_data(request):
    # Retrieve course data from the database
    rates = Rate.objects.all().values()

    # Serialize the data into JSON format
    serialized_rates = list(rates)

    # Return the serialized data as a JSON response
    return JsonResponse(serialized_rates, safe=False)   

def rate_list(request):
    rates = Rate.objects.all()
    return render(request, 'day4/rate_list.html', {'rates': rates})

def add_rate(request):
    if request.method == 'POST':
        form = RateForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('rate_list')
        if form.is_valid():
            # Check if the entered data matches any existing data
            name = form.cleaned_data['name']
            category = form.cleaned_data['category']
            value = form.cleaned_data['value']
            if Rate.objects.filter(name=name, category=category).exists():
                error_message = "Data already exists. Please enter unique values."
                return render(request, 'day4/add_rate.html', {'form': form, 'error_message': error_message})
            else:
                form.save()
                return redirect('rate_list')
    else:
        form = RateForm()
    return render(request, 'day4/add_rate.html', {'form': form})





def edit_rate(request, id):
    rate = get_object_or_404(Rate, id=id)
    if request.method == 'POST':
        form = RateForm(request.POST, instance=rate)
        if form.is_valid():
            form.save()
            return redirect('rate_list')
    else:
        form = RateForm(instance=rate)
    return render(request, 'day4/edit_rate.html', {'form': form})


def delete_rate(request, id):
    rate = get_object_or_404(Rate, id=id)
    rate.delete()
    return redirect('rate_list')


def get_committee_data(request):
    # Retrieve course data from the database
    committee = ExamCommittee.objects.all().values()

    # Serialize the data into JSON format
    serialized_rates = list(committee)

    # Return the serialized data as a JSON response
    return JsonResponse(serialized_rates, safe=False)

def committee_list(request):
    committee = ExamCommittee.objects.all()
    return render(request, 'day4/committee_list.html', {'committee': committee})

def add_committee(request):
    if request.method == 'POST':
        form = ExamCommitteeForm(request.POST)
        # if form.is_valid():
        #     form.save()
        #     return redirect('rate_list')
        if form.is_valid():
            # Check if the entered data matches any existing data
            year=form.cleaned_data['year']
            session=form.cleaned_data['session']
            if ExamCommittee.objects.filter( year= year,session=session).exists():
                error_message = "ExamCommittee for this session already exists. Please enter unique values."
                return render(request, 'day4/add_committee.html', {'form': form, 'error_message': error_message})
            else:
                form.save()
                return redirect('committee_list')
    else:
        form = ExamCommitteeForm()
    return render(request, 'day4/add_committee.html', {'form': form})

def edit_committee(request, id):
    committee = get_object_or_404(ExamCommittee, id=id)
    if request.method == 'POST':
        form = ExamCommitteeForm(request.POST, instance=committee)
        if form.is_valid():
            form.save()
            return redirect('committee_list')
    else:
        form = ExamCommitteeForm(instance=committee)
    return render(request, 'day4/edit_committee.html', {'form': form})


def delete_committee(request, id):
    committee = get_object_or_404(ExamCommittee, id=id)
    committee.delete()
    return redirect('committee_list')



class YourView(APIView):
    def post(self, request, format=None):
        serializer = YourModelSerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def display_data(request):
    # Retrieve data from YourModel
    data = YourModel.objects.all()
    # Pass the data to the template
    for item in data:
        faculty_member = FacultyMember.objects.filter(name=item.name).first()
        item.image = faculty_member.image if faculty_member else None
        
    return render(request, 'day4/ExamBill_list.html', {'data': data})

class SaveResult(APIView):
    def post(self, request, format=None):
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##CHANGE##
##CHANGE##
##CHANGE##


def faculty_list(request):
    faculty = FacultyMember.objects.all()
    serialized_data = list(faculty.values())  # Convert queryset to list of dictionaries
    return JsonResponse(serialized_data, safe=False)

def faculty_members(request):
    all = FacultyMember.objects.all()
    return render(request,'day4/faculty_list.html',{'all':all})


def edit_faculty(request, id):
    faculty_member = get_object_or_404(FacultyMember, id=id)
    form = FacultyMemberForm(instance=faculty_member)
    if request.method == 'POST':
        form = FacultyMemberForm(request.POST, instance=faculty_member)
        if form.is_valid():
            form.save()
            return redirect('faculty_members')
    return render(request, 'day4/edit_faculty.html', {'form': form})

def remove_faculty(request, faculty_id):
    faculty_member = get_object_or_404(FacultyMember, id=faculty_id)
    faculty_member.delete()
    return redirect('faculty_members')

def add_faculty(request):
    if request.method == 'POST':
        form = FacultyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('faculty_members')  # Redirect to the faculty list page after adding a faculty member
    else:
        form = FacultyMemberForm()
    return render(request, 'day4/add_faculty.html', {'form': form})

##
def teacher_profile(request):
    name = request.GET.get('name')
    teacher = get_object_or_404(FacultyMember, name=name)
    results = YourModel.objects.filter(name=name)
    return render(request, 'day4/teacher_profile.html', {'teacher': teacher, 'results': results})


def save_results(request):
    if request.method == 'POST':
        serializer = ResultSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data saved successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)