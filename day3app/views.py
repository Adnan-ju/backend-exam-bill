from django.shortcuts import render
from .models import Book

# Create your views here.

def index(request):
    #context ={}
    books= Book.objects.all()
    #context['all_books']=books
    return render(request,'day3/index.html',{'all_books':books})