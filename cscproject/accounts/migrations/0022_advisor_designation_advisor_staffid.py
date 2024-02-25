# Generated by Django 4.0.8 on 2024-02-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_remove_advisor_designation_remove_advisor_staffid'),
    ]

    operations = [
        migrations.AddField(
            model_name='advisor',
            name='designation',
            field=models.CharField(blank=True, choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='advisor',
            name='staffid',
            field=models.CharField(default='default', max_length=12, unique=True),
        ),
    ]