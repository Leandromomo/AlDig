# Generated by Django 3.2.5 on 2021-12-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Valsinaapp', '0002_auto_20211213_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicidad',
            name='slogan',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='publicidad',
            name='telefono',
            field=models.CharField(max_length=20),
        ),
    ]