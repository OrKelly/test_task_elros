# Generated by Django 4.2.10 on 2024-02-17 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='release_ended',
            field=models.DateField(blank=True, null=True, verbose_name='Дата окончания выпуска'),
        ),
        migrations.AlterField(
            model_name='car',
            name='released_at',
            field=models.DateField(null=True, verbose_name='Дата начала выпуска'),
        ),
    ]
