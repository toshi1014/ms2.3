# Generated by Django 3.0.7 on 2020-06-29 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mypage',
            name='gender',
            field=models.TextField(choices=[('male', 'male'), ('female', 'female')], null=True),
        ),
        migrations.AddField(
            model_name='mypage',
            name='grade',
            field=models.TextField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], null=True),
        ),
    ]
