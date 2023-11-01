from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    return render(request,"index.html")


def add(request):
    if request.method=="POST":
        studentDB=StudentDetails()
        name=request.POST.get("name")
        rollNumber=request.POST.get("rollNumber")
        mail=request.POST.get("mail")
        phoneNumber=request.POST.get("phoneNumber")
        parentPhoneNumber=request.POST.get("parentPhoneNumber")
        foodType=request.POST.get("foodType")

        studentDB.studentName=name
        studentDB.studentRollNumber=rollNumber
        studentDB.studentMail=mail
        studentDB.studentPhoneNumber=phoneNumber
        studentDB.parentPhoneNumber=parentPhoneNumber
        studentDB.foodType=foodType

        if(len(request.FILES)!=0):
                studentDB.image=request.FILES['image']
                studentDB.save()
        else:
                print("nope")  
    return render(request,"addStudent.html")


def updateStudent(request,id):
    return render(request,"updateStudent.html")


def search(request):
    studentDB=StudentDetails.objects.all()
    return render(request,"studentDetails.html",{"studentDB":studentDB})

def delete(request,id):
     return redirect("search")
