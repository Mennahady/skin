# Generated by Django 5.2 on 2025-05-11 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_customuser_username_alter_customuser_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='allergies',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='clinic_address',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='license_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='medical_history',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='profile_picture',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='specialization',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='years_of_experience',
        ),
        migrations.AddField(
            model_name='customuser',
            name='id_number',
            field=models.CharField(blank=True, help_text='National ID or License number', max_length=50),
        ),
    ]
