# Generated by Django 3.1.13 on 2021-11-22 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0002_auto_20211122_1544'),
        ('users', '0002_auto_20210801_0115'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gamificate',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='gamification.gamificationinterface'),
        ),
    ]
