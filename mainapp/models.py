from django.db import models

class Product(models.Model):
    name = models.CharField(verbose_name='Название', max_length=128)
    quantity = models.PositiveIntegerField(verbose_name='Количество на складе', default=0)
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=0, default=0)
    image = models.ImageField(upload_to='product_images', blank=True)