# Generated by Django 4.1.2 on 2022-10-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='rollno',
            field=models.IntegerField(),
        ),
    ]
