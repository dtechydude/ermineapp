# Generated by Django 5.1.6 on 2025-03-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='merchant',
            name='acc_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='merchant',
            name='acc_no',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='merchant',
            name='bank_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
