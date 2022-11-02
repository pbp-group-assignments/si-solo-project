# Generated by Django 4.1 on 2022-11-01 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info_tempat_wisata', '0002_tempatwisata_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='tempatwisata',
            name='wisata_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='tempatwisata',
            name='wisata_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='tempatwisata',
            name='wisata_highlight',
            field=models.TextField(blank=True),
        ),
    ]