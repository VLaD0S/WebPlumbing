from django.db import models
from django import forms

# Create your models here.
class review(models.Model):
    description = models.CharField(max_length=1024)
    author = models.CharField(max_length=1024)
    date = models.CharField(max_length=24)

    def __str__(self):
        return self.description


class contact(models.Model):
    name = models.CharField(max_length=32)
    message = models.TextField(max_length=512)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def clean(self):
        if len(self.phone) > 15:

            raise forms.ValidationError(message="ABORT")


class qualification(models.Model):
    qual = models.CharField(max_length=64)
    rank = models.IntegerField(primary_key=True, editable=True)

    def __str__(self):
        return str(self.rank) + ": " + str(self.qual)


class group(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)


class service(models.Model):
    group = models.ForeignKey(group, on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length=64)

    def __str__(self):
        return str(self.group) + ": " + str(self.service)


class image(models.Model):
    namedesc = models.CharField(max_length=(255))
    img = models.ImageField(upload_to=".", null=False)

    def __str__(self):
        return str(self.img)
