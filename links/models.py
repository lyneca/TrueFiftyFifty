from django.db import models


# Create your models here.
class Link(models.Model):
    display = models.TextField()
    address = models.URLField()
    risk = models.IntegerField()

    def __str__(self):
        return self.display