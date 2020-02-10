# Generated by Django 3.0.2 on 2020-01-27 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('sale', 'sale'), ('rent', 'rent')], max_length=10)),
                ('price', models.PositiveIntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=8)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garages_number', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Property',
                'verbose_name_plural': 'Properties',
            },
        ),
    ]
