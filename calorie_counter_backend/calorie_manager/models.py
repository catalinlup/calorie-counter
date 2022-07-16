from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=100)

class UserData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birthdate = models.DateField()
    height = models.FloatField()
    weight = models.FloatField()
    desired_daily_calorie = models.FloatField()


class UserDailyConsumption(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    calorie_value = models.FloatField()
    product_name = models.CharField(max_length=100)