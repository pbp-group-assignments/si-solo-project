# Generated by Django 4.1 on 2022-10-14 17:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pendaftaran_izin_usaha', '0002_alter_pendaftaranusaha_nomorteleponusaha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usaha',
            name='nomorIzinUsaha',
        ),
        migrations.RemoveField(
            model_name='usaha',
            name='usaha',
        ),
        migrations.DeleteModel(
            name='ListPendaftaran',
        ),
        migrations.DeleteModel(
            name='PendaftaranUsaha',
        ),
    ]