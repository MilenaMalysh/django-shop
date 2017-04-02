from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.utils import timezone


class AdditionalFunction(models.Model):
    name = models.CharField(max_length=40)


class Instrument(models.Model):
    name = models.CharField(max_length=20)
    created_date = models.DateTimeField(default=timezone.now)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    resolution = models.CharField(max_length=15)
    zoom = models.PositiveSmallIntegerField
    additional_functions = models.ManyToManyField(AdditionalFunction)
    photo = models.ImageField(upload_to="images")


class Basket(models.Model):
    user = models.OneToOneField(User)
    products = models.ManyToManyField(Instrument)

