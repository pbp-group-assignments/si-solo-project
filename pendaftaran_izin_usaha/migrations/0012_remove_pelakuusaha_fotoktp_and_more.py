# Generated by Django 4.1 on 2022-10-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_izin_usaha', '0011_pelakuusaha_pesan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pelakuusaha',
            name='fotoKTP',
        ),
        migrations.RemoveField(
            model_name='pelakuusaha',
            name='fotoWajah',
        ),
        migrations.AddField(
            model_name='pelakuusaha',
            name='nik',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]
