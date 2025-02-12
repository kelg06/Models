# Generated by Django 5.1.2 on 2024-10-31 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('author', models.TextField()),
                ('is_checked_out', models.BooleanField(default=False)),
                ('is_favorite', models.BooleanField()),
            ],
        ),
    ]
