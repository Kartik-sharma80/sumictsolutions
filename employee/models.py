from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

class EmployeeDetail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, null=True)
    contact = models.CharField(max_length=15, null=True)
    address = models.CharField(max_length=100, null=True)
    joiningdate = models.DateField(null=True)
    empcode = models.CharField(max_length=100, null=True)
    empdept = models.CharField(max_length=100, null=True)
    designation = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

class EmployeeEducation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    coursepg = models.CharField(max_length=100, null=True)
    schoolclgpg = models.CharField(max_length=200, null=True)
    yearpassingpg = models.CharField(max_length=20, null=True)
    percentagepg = models.CharField(max_length=30, null=True)
    coursegra = models.CharField(max_length=100, null=True)
    schoolclggra = models.CharField(max_length=200, null=True)
    yearpassinggra = models.CharField(max_length=20, null=True)
    percentagegra = models.CharField(max_length=30, null=True)
    coursessc = models.CharField(max_length=100, null=True)
    schoolclgssc = models.CharField(max_length=200, null=True)
    yearpassingssc = models.CharField(max_length=20, null=True)
    percentagessc = models.CharField(max_length=30, null=True)
    coursehsc = models.CharField(max_length=100, null=True)
    schoolclghsc = models.CharField(max_length=200, null=True)
    yearpassinghsc = models.CharField(max_length=20, null=True)
    percentagehsc = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.user.username


class EmployeeExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company1name = models.CharField(max_length=100, null=True)
    company1desig = models.CharField(max_length=100, null=True)
    company1salary = models.CharField(max_length=100, null=True)
    company1duration = models.CharField(max_length=100, null=True)
    company2name = models.CharField(max_length=100, null=True)
    company2desig = models.CharField(max_length=100, null=True)
    company2salary = models.CharField(max_length=100, null=True)
    company2duration = models.CharField(max_length=100, null=True)
    company3name = models.CharField(max_length=100, null=True)
    company3desig = models.CharField(max_length=100, null=True)
    company3salary = models.CharField(max_length=100, null=True)
    company3duration = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.user.username

class Career(models.Model):
    email = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=12)
    image = models.FileField(upload_to="Job Application/", max_length=500, null=True, default=None)

    def __str__(self):
        return self.email