# Generated by Django 4.1.7 on 2023-05-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pa', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.CharField(max_length=40),
        ),
    ]
