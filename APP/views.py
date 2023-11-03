from django.shortcuts import render,redirect
from .models import *
import csv
import datetime

def getRoutine():
    hour=datetime.datetime.now()
    if(hour.hour>=8 and hour.hour<=12):
        return "BREAKFAST"
    elif(hour.hour>=12 and hour.hour<=14):
        return "LUNCH"
    elif(hour.hour>=17 and hour.hour<=19):
        return "SNACKS"
    else:
        return "DINNER"





def isRollNumberExists(csv_file, roll_number):
    try:
        with open(csv_file, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == roll_number:
                    return True
    except FileNotFoundError:
        return False

    return False


def writeData(name, roll_number, parent_number):
    routine=getRoutine()

    try:
        count = Count.objects.get(id=1)
    except Count.DoesNotExist:
        count = Count(id=1, totalCount=0)
        count.save()
    if routine=="BREAKFAST":
        try:
            breakfastCountValue = breakfastCount.objects.get(id=1)
        except breakfastCount.DoesNotExist:
            breakfastCountValue = breakfastCount(id=1, totalCount=0)
            breakfastCountValue.save()
    elif routine=="LUNCH":
        try:
            lunchCountValue = lunchCount.objects.get(id=1)
        except lunchCount.DoesNotExist:
            lunchCountValue = lunchCount(id=1, totalCount=0)
            lunchCountValue.save()
    elif routine=="SNACKS":
        try:
            snackCountValue = snacksCount.objects.get(id=1)
        except snacksCount.DoesNotExist:
            snackCountValue = snacksCount(id=1, totalCount=0)
            snackCountValue.save()
    
    elif routine=="DINNER":    
        try:
            dinnerCountValue = dinnerCount.objects.get(id=1)
        except dinnerCount.DoesNotExist:
            dinnerCountValue = dinnerCount(id=1, totalCount=0)
            dinnerCountValue.save()
    countValue=count.totalCount


    csv_file1 = 'mess.csv'
    if routine=="BREAKFAST":
        csv_file="breakfast.csv"
    elif routine=="LUNCH":
        csv_file="lunch.csv"
    elif routine=="SNACKS":
        csv_file="snacks.csv"
    elif routine=="DINNER":
        csv_file="dinner.csv"

    if isRollNumberExists(csv_file1, roll_number):
        pass
    else:
        new_data = [
            [name, roll_number, parent_number]
        ]
        with open(csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
            if routine=="BREAKFAST":
                breakfastCountValue.totalCount=breakfastCountValue.totalCount+1
                breakfastCountValue.save()
            elif routine=="LUNCH":
                lunchCountValue.totalCount=lunchCountValue.totalCount+1
                lunchCountValue.save()

            elif routine=="SNACKS":
                snackCountValue.totalCount=snackCountValue.totalCount+1
                snackCountValue.save()
            elif routine=="DINNER":
                dinnerCountValue.totalCount=dinnerCountValue.totalCount+1
                dinnerCountValue.save()
            with open(csv_file1, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(new_data)        

                count.totalCount=countValue+1
                count.save()

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


def send(request):
    
    try:
        totalCount = Count.objects.get(id=1)
    except Count.DoesNotExist:
        totalCount = Count(id=1, totalCount=0)
        totalCount.save()


    try:
        breakfastTotal=breakfastCount.objects.get(id=1)
    except breakfastCount.DoesNotExist:
        breakfastTotal=breakfastCount(id=1,totalCount=1)
        breakfastTotal.save()


    try:
         lunchTotal=lunchCount.objects.get(id=1)
    except lunchCount.DoesNotExist:
        lunchTotal=lunchCount(id=1,totalCount=1)
        lunchTotal.save()


    try:
        snacksTotal=snacksCount.objects.get(id=1)
    except snacksCount.DoesNotExist:
        snacksTotal=snacksCount(id=1,totalCount=1)
        snacksTotal.save()


    try:
        dinnerTotal=dinnerCount.objects.get(id=1)
    except dinnerCount.DoesNotExist:
        dinnerTotal=dinnerCount(id=1,totalCount=1)
        dinnerTotal.save()

    date=datetime.datetime.today()
    currentDate=date.date()
    time=getRoutine()
    total=totalCount.totalCount
    breakfastTotalValue=breakfastTotal.totalCount
    lunchTotalValue=lunchTotal.totalCount
    snacksTotalValue=snacksTotal.totalCount
    dinnerTotalValue=dinnerTotal.totalCount


    if request.method=="POST":
        pass

    return render(request,"send.html",{"total":total,"date":currentDate,"time":time,"breakTotal":breakfastTotalValue,"lunchTotal":lunchTotalValue,"snacksTotal":snacksTotalValue,"dinnerTotal":dinnerTotalValue})


def resetData(request):
    countValue=Count.objects.get(id=1)
    countValue.totalCount=0
    countValue.save()

    try:
        value=breakfastCount.objects.get(id=1)
        value.totalCount=0
        value.save()
    except breakfastCount.DoesNotExist:
        breakfastCountValue = breakfastCount(id=1, totalCount=0)
        breakfastCountValue.save()
    try:
        value=lunchCount.objects.get(id=1)
        value.totalCount=0
        value.save()
    except lunchCount.DoesNotExist:
        breakfastCountValue = lunchCount(id=1, totalCount=0)
        breakfastCountValue.save()
    try:
        value=snacksCount.objects.get(id=1)
        value.totalCount=0
        value.save()
    except snacksCount.DoesNotExist:
        breakfastCountValue = snacksCount(id=1, totalCount=0)
        breakfastCountValue.save()
    try:
        value=dinnerCount.objects.get(id=1)
        value.totalCount=0
        value.save()
    except dinnerCount.DoesNotExist:
        breakfastCountValue = dinnerCount(id=1, totalCount=0)
        breakfastCountValue.save()

    totalCSV = 'mess.csv'
    breakfastCSV="breakfast.csv"
    lunchCSV="lunch.csv"
    snacksCSV="snacks.csv"
    dinnerCSV="dinner.csv"

    # Open the CSV file in write mode to truncate its contents
    with open(totalCSV, 'w', newline='') as totalCSVAlias:
        totalCSVAlias.truncate(0)
    totalCSVAlias.close()



    with open(breakfastCSV, 'w', newline='') as breakfastCSVAlias:
        breakfastCSVAlias.truncate(0)
    breakfastCSVAlias.close()

    with open(lunchCSV, 'w', newline='') as lunchCSVAlias:
        lunchCSVAlias.truncate(0)
    lunchCSVAlias.close()       

    with open(snacksCSV, 'w', newline='') as snacksCSVAlias:
        snacksCSVAlias.truncate(0)
    snacksCSVAlias.close()


    with open(dinnerCSV, 'w', newline='') as dinnerCSVAlias:
        dinnerCSVAlias.truncate(1)
    dinnerCSVAlias.close()


    return redirect("send")


def viewDetail(request,meal):

    data = []  
    with open(f'{meal}.csv', 'r') as file:
        print(file)
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            print(row)
            data.append(row)
    print(data)

    return render(request, 'mealDetails.html', {'data': data,"meal":meal})