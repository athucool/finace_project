# Generated by Django 2.1.5 on 2020-07-07 07:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_auto_20200707_1258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('Finance_Manager', 'approve payments to vendor'), ('Analyst', 'process vendor payment'))},
        ),
    ]
