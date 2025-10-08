
from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name + " " + self.last_name



class Student(models.Model):
    name=models.CharField(max_length=50)
    student_id=models.IntegerField()
    section=models.CharField(max_length=5)
    degree=models.CharField(max_length=4)


class Author(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=3)
    birth_date = models.DateField(blank=True, null=True)