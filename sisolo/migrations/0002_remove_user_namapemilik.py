# Generated by Django 4.1 on 2022-10-25 04:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sisolo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='namaPemilik',
        ),
    ]