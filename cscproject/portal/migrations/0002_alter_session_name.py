# Generated by Django 4.0.8 on 2023-11-12 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]
