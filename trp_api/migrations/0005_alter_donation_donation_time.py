# Generated by Django 4.0.3 on 2022-03-31 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trp_api', '0004_alter_donation_donation_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='donation_time',
            field=models.DateTimeField(verbose_name='%Y-%m-%d || %H:%M:%S'),
        ),
    ]
