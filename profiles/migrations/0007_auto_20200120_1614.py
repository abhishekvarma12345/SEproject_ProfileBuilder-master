# Generated by Django 3.0.2 on 2020-01-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_auto_20200116_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultyprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='staff_pics'),
        ),
        migrations.AlterField(
            model_name='studentprofile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='student_pics'),
        ),
    ]
