# Generated by Django 2.1.5 on 2020-07-07 05:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20200705_0719'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('Finance_Manager', 'approve payments to vendor'), ('Analyst', 'process vendor payment'))},
        ),
    ]