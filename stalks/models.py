from django.db import models
class merchandise(models.Model):
    merchandisename = models.CharField(max_length=100)
    merchandisetype= models.CharField(max_length=100)
    merchandiseamount = models.IntegerField(null=False, blank=False)


# Create your models here.
