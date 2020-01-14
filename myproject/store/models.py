from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=240)
    pic = models.ImageField(upload_to='store/')
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Background(models.Model):

    name = models.CharField(max_length=240)
    pic = models.ImageField(upload_to='background/store/')

    def __str__(self):
        return self.name
# Create your models here.
