
# Generated by Django 4.1 on 2022-11-02 05:43

from django.db import migrations, models
import django.db.models.deletion

# Generated by Django 4.1 on 2022-11-02 10:08

from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [

        ('pendaftaran_izin_usaha', '0013_usaha_alasanditolak'),

    ]

    operations = [
        migrations.CreateModel(

            name='KebutuhanPokok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namaKebutuhan', models.CharField(blank=True, max_length=150)),
                ('hargaKebutuhan', models.CharField(blank=True, max_length=50)),
                ('deskripsiKebutuhan', models.CharField(blank=True, max_length=150)),
                ('tokoKebutuhan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pendaftaran_izin_usaha.usaha')),

            name='Kebutuhan_Pokok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=100)),
                ('harga', models.IntegerField()),
                ('image', models.URLField()),

            ],
        ),
    ]
