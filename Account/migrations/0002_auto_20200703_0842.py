# Generated by Django 2.1.5 on 2020-07-03 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('Finance Manager', 'approve payments to vendor'), ('Analyst', 'process vendor payment'))},
        ),
    ]