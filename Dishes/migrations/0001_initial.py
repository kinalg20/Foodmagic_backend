# Generated by Django 3.1.4 on 2020-12-29 16:48

import Dishes.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('created', models.DateTimeField(auto_created=True)),
                ('dish_id', models.AutoField(default=Dishes.models.random_id_genrate, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField(default=1)),
                ('description', models.TextField(max_length=200)),
                ('is_veg', models.BooleanField(default=False)),
                ('is_available', models.BooleanField(default=False)),
                ('category_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_address', to='category.categories')),
            ],
        ),
    ]
