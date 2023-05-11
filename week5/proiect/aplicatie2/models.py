from django.db import models

import aplicatie1


# Create your models here.


class Company(models.Model):
    # active = models.BooleanField(default=1)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey('aplicatie1.Location', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.website} -- {self.name}"


class AuditCompany(models.Model):

    active = models.BooleanField(default=1)
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    location = models.ForeignKey('aplicatie1.Location', on_delete=models.CASCADE)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=90)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=1)

    def __str__(self):
        return f"{self.website} -- {self.name}"
