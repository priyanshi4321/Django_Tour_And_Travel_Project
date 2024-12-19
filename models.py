from django.db import models

# Create your models here.
class Employeedata(models.Model):
    emp_name= models.CharField(max_length=10)
    emp_pwd= models.CharField(max_length=10)
    emp_email=models.EmailField(max_length=10)
    emp_mob=models.BigIntegerField()
    emp_dept=models.CharField(max_length=10)
    emp_dob=models.DateField()
    emp_img=models.ImageField(upload_to='uploadedFiles',null=True)