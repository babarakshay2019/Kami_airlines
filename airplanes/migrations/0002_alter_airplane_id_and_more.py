# Generated by Django 4.2.8 on 2023-12-12 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airplanes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airplane',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='airplane',
            name='passenger_assumptions',
            field=models.IntegerField(),
        ),
    ]
