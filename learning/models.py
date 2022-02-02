from django.db import models

# Create your models here.


class signup(models.Model):
    firstname=models.CharField(max_length=25)
    lastname=models.CharField(max_length=25)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    ConfirmPassword=models.CharField(max_length=25)

