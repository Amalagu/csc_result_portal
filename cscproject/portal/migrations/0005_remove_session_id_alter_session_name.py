# Generated by Django 4.0.8 on 2024-01-19 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_session_id_alter_session_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='id',
        ),
        migrations.AlterField(
            model_name='session',
            name='name',
            field=models.CharField(max_length=9, primary_key=True, serialize=False, unique=True),
        ),
    ]
