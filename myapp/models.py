from django.db import models

# Create your models here.

class studentsmodel(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()


    def __str__(self):
        return self.first_name +'' +self.last_name

class StudentsDetails(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, null=True, blank=True)
    address = models.CharField(max_length=50)
    dob = models.DateField()
    gender = models.CharField(max_length=18,choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='M')

class Meta:
    db_table = 'students'