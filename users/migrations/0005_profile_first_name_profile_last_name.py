# Generated by Django 4.2.2 on 2023-06-21 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_course_profile_school_alter_profile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default=False, max_length=30),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default=False, max_length=30),
        ),
    ]