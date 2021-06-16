from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=50)


class Address(models.Model):
    models.ForeignKey(City, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
