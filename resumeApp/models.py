from django.db import models
from django import forms
# Create your models here.

class InputForm(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    time_log = models.TimeField()

    def __str__(self):
        return self.first_name
