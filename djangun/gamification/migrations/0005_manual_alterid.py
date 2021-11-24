from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0004_manual_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leveldefinition',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]

