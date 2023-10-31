from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")


def add(request):
    return render(request,"addStudent.html")


def updateStudent(request):
    return render(request,"updateStudent.html")
