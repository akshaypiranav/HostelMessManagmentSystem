from django.shortcuts import render,redirect
from .models import *
import csv


def isRollNumberExists(csv_file, roll_number):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                if row[1] == roll_number:
                    return True
    except FileNotFoundError:
        return False

    return False

def writeData(name, roll_number, parent_number):
    csv_file = 'mess.csv'

    if isRollNumberExists(csv_file, roll_number):
        pass
    else:
        new_data = [
            [name, roll_number, parent_number]
        ]
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)

def index(request):
    if request.method=="POST":
        rollNumber=request.POST.get("rollNumber")
        if(StudentDetails.objects.filter(studentRollNumber=rollNumber.upper()).exists()):
            studentData=StudentDetails.objects.get(studentRollNumber=rollNumber.upper())
            writeData(studentData.studentName,studentData.studentRollNumber,studentData.parentPhoneNumber)
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
            studentDB.studentName=name.upper()
            studentDB.studentRollNumber=rollNumber.upper()
            studentDB.studentMail=mail.upper()
            studentDB.studentPhoneNumber=phoneNumber
            studentDB.parentPhoneNumber=parentPhoneNumber
            studentDB.foodType=foodType.upper()

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
