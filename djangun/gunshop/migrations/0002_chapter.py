# Generated by Django 3.1.13 on 2021-11-27 05:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gunshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chaptername', models.CharField(max_length=1000)),
                ('chapter_body', models.TextField()),
                ('is_published', models.BooleanField(default=False)),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gunshop.lecture')),
            ],
        ),
    ]
