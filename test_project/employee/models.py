from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

GENDER=[
    ('W',('Woman')),
    ('M',('Man')),
]
RECORD_TYPE=[
    (0,('Active')),
    (1,('Inactive')),
]

class EmployeeProfile(models.Model):
    profession = models.CharField(max_length = 100, default='-')
    date_posted = models.DateTimeField(default = timezone.now)
    worker = models.ForeignKey(User, on_delete = models.CASCADE)
    EmployeeID = models.IntegerField(default=0)
    First_Name = models.CharField(max_length=200, verbose_name='First Name', default='-')
    Middle_Name = models.CharField(max_length=200, verbose_name='Middle Name',default='-')
    Last_Name = models.CharField(max_length=200, verbose_name='Last Name', default='-')
    Prefix = models.CharField(max_length=200, verbose_name='Prefix', default='-')
    Nickname = models.CharField(max_length=200, verbose_name='Nickname', default='-')
    Gender = models.CharField(max_length=1, verbose_name='Gender', choices=GENDER, default=GENDER[0][0])
    Birth_date = models.DateField(default=timezone.now)
    Passport_Surname = models.CharField(max_length=200, verbose_name='Passport Surname', default='-')
    Passport_Given_Name = models.CharField(max_length=200, verbose_name='Passport Given Name', default='-')
    Job_Title = models.CharField(max_length=200, verbose_name='Job Title', default='-')
    Business_Phone = models.CharField(max_length=12, verbose_name='Business Phone', default='-')
    Location = models.CharField(max_length=200, verbose_name='Location', default='-')
    Hire_Date = models.DateField(default=timezone.now)
    Record_Status = models.IntegerField(choices=RECORD_TYPE, verbose_name='Record Status', default=RECORD_TYPE[0][0])

class EmployeeGoals(models.Model):
    worker = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
    GoalsName = models.CharField(max_length=200, verbose_name='GoalsName', default='-')
    Metrics = models.CharField(max_length=100, verbose_name='GoalsName', default='-')
    Percent = models.FloatField(max_length=100, verbose_name='Percent', default=0.0)
    Weight = models.FloatField(max_length=100, verbose_name='Weight', default=0.0)
    StartDate= models.DateField(default=timezone.now)
    Status= models.IntegerField(verbose_name='Status', default=0)
    Actual = models.CharField(max_length=100, verbose_name='Actual', default='-')
    Target = models.TextField(default='-')
        
class Note(models.Model):
    note = models.CharField(max_length=300, verbose_name='note', default=' ')
    author = models.ForeignKey(User, on_delete = models.CASCADE, default=1)
