from django.db import models

# один class это одна таблица в базе данных
class Product(models.Model):
    name = models.CharField(max_length=100, default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.name