from django.db import models

# Create your models here.
class Review(models.Model):
    description = models.CharField(max_length=512)
    author = models.CharField(max_length=16)
    date = models.CharField(max_length=16)

    def __str__(self):
        return self.description


class Email(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    email = models.EmailField()


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
