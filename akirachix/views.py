from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.

def welcome(request):
    return render(request,'welcome_students.html')
def students(request):
    students = Student.objects.all()
    
    context = {
        'students':students
    }
    return render(request,'listing_students.html',context)