# Generated by Django 4.2.2 on 2023-06-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='course',
            field=models.CharField(default='Course', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(default='First Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=30),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='default.jpeg', upload_to='profile_pictures'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(default='School', max_length=100),
        ),
    ]
