# Generated by Django 4.1 on 2022-10-27 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TempatWisata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wisata_title', models.CharField(max_length=255)),
                ('wisata_description', models.TextField()),
                ('wisata_highlight', models.TextField()),
            ],
        ),
    ]
