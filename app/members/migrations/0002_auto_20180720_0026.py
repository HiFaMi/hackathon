# Generated by Django 2.0.7 on 2018-07-19 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseIce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FoodStuff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_ice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.BaseIce')),
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
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='size',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Size'),
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='source',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Source'),
        ),
        migrations.AddField(
            model_name='foodstuff',
            name='topping',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.Topping'),
        ),
    ]