from django.db import models

# Create your models here.

class Coin(models.Model):
    name = models.CharField(max_length=100, verbose_name='Coin İsmi')
    symbol = models.CharField(max_length=50, verbose_name='Coin Sembolü')
    image = models.CharField(max_length=200, verbose_name='Coin İconu')
    current_price = models.CharField(max_length=50, verbose_name='Coin Güncel Fiyatı')
    market_cap = models.CharField(max_length=100, verbose_name='Coin Hacmi')

    def __str__(self):
        return self.name

# SELECT * FROM [dbo].[cointracker_coins] MSSQL SORGUSU