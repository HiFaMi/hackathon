# Generated by Django 2.0.7 on 2018-07-20 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20180720_0026'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodstuff',
            name='base_ice',
        ),
        migrations.RemoveField(
            model_name='foodstuff',
            name='size',
        ),
        migrations.RemoveField(
            model_name='foodstuff',
            name='source',
        ),
        migrations.RemoveField(
            model_name='foodstuff',
            name='topping',
        ),
        migrations.DeleteModel(
            name='BaseIce',
        ),
        migrations.DeleteModel(
            name='FoodStuff',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.DeleteModel(
            name='Source',
        ),
        migrations.DeleteModel(
            name='Topping',
        ),
    ]
