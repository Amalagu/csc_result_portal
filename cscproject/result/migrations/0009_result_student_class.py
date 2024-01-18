# Generated by Django 4.0.8 on 2024-01-16 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_departmentaldues_student'),
        ('result', '0008_rename_course_id_registeredcourse_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='student_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='portal.studentclass'),
        ),
    ]
