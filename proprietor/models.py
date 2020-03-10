from django.db import models


# Create your models here.
class Person(models.Model):
    firstname = models.CharField(max_length=120)
    lastname = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname}, {self.lastname}"
