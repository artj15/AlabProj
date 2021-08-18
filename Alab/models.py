from django.db import models


# Create your models here.

class Product(models.Model):
    unit_of_measurement = [
        ('Шт', "Штук"),
        ('Кг', 'Килограмм'),
        ('Л', 'Литров')
    ]
    name = models.CharField(max_length=1000)
    quantity = models.PositiveIntegerField()
    unit = models.CharField(max_length=2, choices=unit_of_measurement)
    price = models.PositiveIntegerField()
    data = models.DateField()

    def __str__(self):
        return f'{self.name} {self.quantity} {self.price}'


    class Meta:
        ordering = ['name', 'quantity']
        verbose_name = 'Products'