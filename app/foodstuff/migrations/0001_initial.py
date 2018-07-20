# Generated by Django 2.0.7 on 2018-07-20 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseIce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ice_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodStuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_ice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodstuff.BaseIce')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('B', 'Big')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foodstuff.Size'),
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodstuff.Source'),
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodstuff.Topping'),
        ),
    ]
