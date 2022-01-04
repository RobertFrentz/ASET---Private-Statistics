from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


class Patient(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.CharField(max_length=300)
    age_bit_length = models.IntegerField()
    weight = models.CharField(max_length=300)
    weight_bit_length = models.IntegerField()
    height = models.CharField(max_length=300)
    height_bit_length = models.IntegerField()
    hospital = models.CharField(max_length=200)





