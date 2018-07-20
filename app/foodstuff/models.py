from django.db import models


class BaseIce(models.Model):
    ice_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.ice_name


class Source(models.Model):
    source_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.source_name


class Topping(models.Model):
    topping_name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.topping_name


class Size(models.Model):
    FOOD_SIZE = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big'),
    )

    food_size = models.CharField(max_length=1, choices=FOOD_SIZE)

    def __str__(self):
        return self.food_size


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
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

