# Generated by Django 5.1.2 on 2024-10-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_favorite',
            field=models.BooleanField(),
        ),
    ]
