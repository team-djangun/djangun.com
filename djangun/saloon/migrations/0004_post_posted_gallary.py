# Generated by Django 3.1.13 on 2021-12-01 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saloon', '0003_gallary_gallary_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted_gallary',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='saloon.gallary'),
            preserve_default=False,
        ),
    ]
