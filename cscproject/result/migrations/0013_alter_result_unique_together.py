# Generated by Django 4.0.8 on 2024-02-07 20:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0012_alter_result_cgpa_alter_result_gpa'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='result',
            unique_together=set(),
        ),
    ]
