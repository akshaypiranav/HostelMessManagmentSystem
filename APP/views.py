from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
    if request.method=="POST":
        rollNumber=request.POST.get("rollNumber")
        if(StudentDetails.objects.filter(studentRollNumber=rollNumber).exists()):
            studentData=StudentDetails.objects.get(studentRollNumber=rollNumber)
            print(studentData.image)
            print("HOSTELLER")
            return render(request,"index.html",{"studentData":studentData})
        else:
            print("NO")

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
        if(not(StudentDetails.objects.filter(studentRollNumber=rollNumber).exists())):
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
        else:
             pass
    return render(request,"addStudent.html")


def updateStudent(request,id):
    if(StudentDetails.objects.filter(id=id).exists()):
        studentDB=StudentDetails.objects.get(id=id)

    if request.method=="POST":
        studentDB=StudentDetails.objects.get(id=id)
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
                
        else:
                print("nope")  
        studentDB.save()
        return redirect("search")
    return render(request,"updateStudent.html",{"data":studentDB})


def search(request):
    studentDB=StudentDetails.objects.all()
    return render(request,"studentDetails.html",{"studentDB":studentDB})

def delete(request,id):
     if(StudentDetails.objects.filter(id=id).exists()):
          studentDB=StudentDetails.objects.get(id=id)
          studentDB.delete()
     return redirect("search")
