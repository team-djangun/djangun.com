# Generated by Django 3.1.13 on 2021-12-01 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saloon', '0002_auto_20211126_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallary',
            name='gallary_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='saloon.salooncategory'),
        ),
    ]
