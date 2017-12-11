from django.db import models

# Create your models here.
class Review(models.Model):
    description = models.CharField(max_length=512)
    author = models.CharField(max_length=16)
    date = models.CharField(max_length=16)



    def __str__(self):
        return self.description

