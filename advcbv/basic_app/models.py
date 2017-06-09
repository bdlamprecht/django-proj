from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=50)
    princial = models.CharField(max_length=20)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School,related_name='students')

    def __str__(self):
        return self.name
