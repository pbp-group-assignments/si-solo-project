# Generated by Django 4.1 on 2022-10-14 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_izin_usaha', '0004_usaha_alamatpemilik_usaha_alamatusaha_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usaha',
            name='statusPendaftaran',
            field=models.TextField(blank=True, default='Diajukan'),
        ),
    ]
