# Generated by Django 4.0.8 on 2024-02-25 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_alter_advisor_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advisor',
            name='advisor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.staff'),
        ),
    ]
