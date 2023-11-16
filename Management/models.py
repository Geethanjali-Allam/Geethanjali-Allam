from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=64)
    Email = models.CharField(max_length=64)
    Password = models.CharField(max_length=64)
    Position = models.CharField(max_length=64)
    Salary = models.IntegerField()


    def __str__(self):
        return f"{self.id}: {self.Name} is {self.Position} with salary of {self.Salary}. Email:{self.Email} and Password:{self.Password}"

class Complaint(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    complaint_type = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.id}: {self.author} - {self.complaint_type} - {self.subject}"