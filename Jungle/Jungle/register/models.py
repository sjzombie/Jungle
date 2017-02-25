from django.db import models

class User(models.Model):
    NAME = models.CharField(max_length=250)
    MIDDLENAME = models.CharField(max_length=250)
    SURNAME = models.CharField(max_length=250)
    MOBILE = models.IntegerField
    EMAIL = models.CharField(max_length=250)
