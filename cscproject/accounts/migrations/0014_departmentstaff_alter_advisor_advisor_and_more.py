# Generated by Django 4.0.8 on 2024-02-25 13:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_advisor_advisor'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentStaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffid', models.CharField(max_length=12, unique=True)),
                ('designation', models.CharField(choices=[('Mr.', 'Mr.'), ('Mrs.', 'Mrs.'), ('Dr.', 'Dr.'), ('Prof.', 'Prof'), ('Miss', 'Miss'), ('Ms.', 'Ms.')], max_length=10)),
                ('staff', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='advisor',
            name='advisor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.departmentstaff'),
        ),
        migrations.AlterField(
            model_name='departmenthead',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.departmentstaff'),
        ),
        migrations.AlterField(
            model_name='lecturer',
            name='lecturer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.departmentstaff'),
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
