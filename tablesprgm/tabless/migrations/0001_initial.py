# Generated by Django 5.1.4 on 2024-12-11 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customerdetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('mobile_number', models.CharField(max_length=15)),
                ('place', models.CharField(max_length=20)),
                ('Age', models.CharField(max_length=3)),
            ],
        ),
    ]
