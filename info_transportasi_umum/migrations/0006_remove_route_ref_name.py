# Generated by Django 4.1 on 2022-11-02 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_transportasi_umum', '0005_route_ref_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route',
            name='ref_name',
        ),
    ]
