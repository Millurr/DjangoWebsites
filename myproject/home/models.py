from django.db import models


class Background(models.Model):

    name = models.CharField(max_length=240)
    pic = models.ImageField(upload_to='background/home/')

    def __str__(self):
        return self.name
# Create your models here.
