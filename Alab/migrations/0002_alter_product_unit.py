# Generated by Django 3.2.6 on 2021-08-18 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Alab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Шт', 'Штук'), ('Кг', 'Килограмм'), ('Л', 'Литров')], max_length=2),
        ),
    ]
