from django.db import models
from django.contrib.auth.models import User

# один class это одна таблица в базе данных
class Product(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    name = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')
    image = models.ImageField(blank=True, upload_to='images')

    def __str__(self):
        return self.name