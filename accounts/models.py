from django.db import models

# Create your models here.

class Accounts(models.Model):
    email = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    coin = models.IntegerField(default=0)

    def addcoin(self):
        self.coin = self.coin + 1
