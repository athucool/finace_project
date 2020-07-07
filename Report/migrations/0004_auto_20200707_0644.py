# Generated by Django 2.1.5 on 2020-07-07 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Report', '0003_auto_20200705_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finance_report',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='finance_report',
            name='payment',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='finance_report',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
