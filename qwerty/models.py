from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

class Bank(models.Model):
    bankName=models.CharField(max_length=20)
    bankChain=models.CharField(max_length=20)

class Lombard(models.Model):
    LombardName=models.CharField(max_length=20)
    LombardChain=models.CharField(max_length=20)

class Cars(models.Model):
    CarsName=models.CharField(max_length=20)
    CarsChain=models.CharField(max_length=20)

class People(models.Model):
    PeopleName=models.CharField(max_length=20)
    PeopleChain=models.CharField(max_length=20)