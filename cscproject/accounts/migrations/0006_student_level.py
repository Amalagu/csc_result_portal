# Generated by Django 4.0.8 on 2023-11-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_student_student_class'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('100 LEVEL', '100 LEVEL'), ('200 LEVEL', '200 LEVEL'), ('300 LEVEL', '300 LEVEL'), ('400 LEVEL', '400 LEVEL'), ('500 LEVEL', '500 LEVEL')], max_length=25, null=True),
        ),
    ]
