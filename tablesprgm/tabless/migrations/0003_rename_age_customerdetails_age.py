# Generated by Django 5.1.4 on 2024-12-12 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tabless', '0002_alter_customerdetails_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetails',
            old_name='Age',
            new_name='age',
        ),
    ]