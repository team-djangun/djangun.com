# Generated by Django 3.1.13 on 2021-12-01 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ranch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='hello', max_length=1000),
            preserve_default=False,
        ),
    ]
