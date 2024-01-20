# Generated by Django 4.0.8 on 2024-01-20 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0007_remove_session_id_alter_session_name'),
        ('accounts', '0009_user_address'),
        ('course', '0002_course_level'),
        ('result', '0009_result_student_class'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='registeredcourse',
            unique_together={('student', 'course', 'session', 'semester')},
        ),
        migrations.AlterUniqueTogether(
            name='result',
            unique_together={('student', 'session', 'semester')},
        ),
    ]
