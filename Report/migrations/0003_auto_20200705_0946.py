# Generated by Django 2.1.5 on 2020-07-05 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0002_auto_20200705_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_report',
            name='investment',
            field=models.IntegerField(null=True, verbose_name='investment'),
        ),
        migrations.AlterField(
            model_name='finance_report',
            name='salary',
            field=models.IntegerField(null=True, verbose_name='salary'),
        ),
        migrations.AlterField(
            model_name='finance_report',
            name='total',
            field=models.IntegerField(null=True, verbose_name='total'),
        ),
        migrations.AlterField(
            model_name='finance_report',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
