from django.db import models


# Create your models here.
class Review(models.Model):
    description = models.CharField(max_length=512)
    author = models.CharField(max_length=16)
    date = models.CharField(max_length=16)

    def __str__(self):
        return self.description


class Contact(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=512)
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    prefix = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        if self.prefix == 0:
            return str(self.name) + ": " + str(self.prefix) + " " + str(self.phone)
        else:
            return str(self.name) + ": +" + str(self.prefix) + " " + str(self.phone)


class Qualification(models.Model):
    qual = models.CharField(max_length=64)
    rank = models.IntegerField(primary_key=True, editable=True)

    def __str__(self):
        return str(self.rank) + ": " + str(self.qual)


class Group(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=64)

    def __str__(self):
        return str(self.name)


class Service(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True)
    service = models.CharField(max_length=64)

    def __str__(self):
        return str(self.group) + ": " + str(self.service)


class Image(models.Model):
    namedesc = models.CharField(max_length=(255))
    img = models.ImageField(upload_to="static/gallery", null=False)

