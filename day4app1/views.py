from django.shortcuts import render,redirect
from .models import Course
from .forms import CourseForm
from django.http import JsonResponse
# Create your views here.

# Create your views here.

def home(request):
    #context ={}
    all=Course.objects.all()
    #context['all_books']=books
    return render(request,'day4/home.html',{'all_courses':all})

def remove(request,id):
    c=Course.objects.get(id=id)
    c.delete()
    return redirect(home)

def edit(request,id):
    c=Course.objects.get(id=id)
    cform=CourseForm(instance=c)
    print("+++++++" + request.method + "---------")
    if request.method=="POST":
        frm=CourseForm(request.POST, instance=c)
        if frm.is_valid():
            frm.save()
            return redirect(home)
        return render(request,'day4/edit.html',{'form':frm})
def add(request):
    frm=CourseForm()
    return render(request,'day4/add.html',{'form':frm})
def save(request):
    if request.method=="POST" :
        frm=CourseForm(request.POST)
        frm.save
        return redirect(home)
    return redirect(home)

def get_course_data(request):
    # Retrieve course data from the database
    courses = Course.objects.all().values()

    # Serialize the data into JSON format
    serialized_courses = list(courses)

    # Return the serialized data as a JSON response
    return JsonResponse(serialized_courses, safe=False)