# Generated by Django 2.2.13 on 2022-04-19 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trp_api', '0009_userinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='description',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='education',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='image',
        ),
    ]
