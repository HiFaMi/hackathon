from django.db import models


class BaseIce(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Source(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()


class Size(models.Model):
    FOOD_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big'),
    )

    food_size = models.CharField(max_length=1, choices=FOOD_SIZE)


class FoodStuff(models.Model):
    base_ice = models.ForeignKey(
        BaseIce,
        on_delete=models.CASCADE
    )

    source = models.ForeignKey(
        Source,
        on_delete=models.CASCADE
    )

    topping = models.ForeignKey(
        Topping,
        on_delete=models.CASCADE
    )

    size = models.ForeignKey(
        Size,
        on_delete=models.CASCADE
    )

