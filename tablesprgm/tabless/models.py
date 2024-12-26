from django.db import models

class Customerdetails(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=15)
    place = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return self.username

