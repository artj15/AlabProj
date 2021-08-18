# Generated by Django 3.2.6 on 2021-08-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('quantity', models.PositiveIntegerField()),
                ('unit', models.CharField(blank=True, choices=[('Шт', 'Штук'), ('Кг', 'Килограмм'), ('Л', 'Литров')], max_length=2)),
                ('price', models.PositiveIntegerField()),
                ('data', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Products',
                'ordering': ['name', 'quantity'],
            },
        ),
    ]