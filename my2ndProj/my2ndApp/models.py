from django.db import models

# Create your models here.
class MyUser(models.Model):
    fName = models.CharField(max_length=10)
    lName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30,unique=True)
