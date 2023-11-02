from django.db import models
import datetime
import os
# Create your models here.
def getFileName(request,filename):
    now_time=datetime.datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename="%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)

class StudentDetails(models.Model):
    studentName=models.CharField(blank=False,max_length=30)
    studentRollNumber=models.CharField(blank=False,max_length=30)
    studentMail=models.CharField(blank=False,max_length=30)
    studentPhoneNumber=models.CharField(blank=False,max_length=30)
    parentPhoneNumber=models.CharField(blank=False,max_length=30)
    foodType=models.CharField(blank=False,max_length=30)
    image=models.ImageField(upload_to=getFileName,null=True,blank=True)
    class Meta:
        db_table='studentDetails'

class Count(models.Model):
    totalCount = models.IntegerField(blank=False,default=0)
    class Meta:
        db_table="countTable"

class breakfastCount(models.Model):
    totalCount = models.IntegerField(blank=False,default=0)
    class Meta:
        db_table="breakfastCount" 

   
class lunchCount(models.Model):
    totalCount = models.IntegerField(blank=False,default=0)
    class Meta:
        db_table="lunchCount"    


class dinnerCount(models.Model):
    totalCount = models.IntegerField(blank=False,default=0)
    class Meta:
        db_table="dinnerCount"   

class snacksCount(models.Model):
    totalCount = models.IntegerField(blank=False,default=0)
    class Meta:
        db_table="snacksCount"    
