from django.db import models

# Create your models here.
class Review(models.Model):
    description = models.CharField(max_length=1024)
    author = models.CharField(max_length=256)
    date = models.CharField(max_length=256)



    def __str__(self):
        return self.author



