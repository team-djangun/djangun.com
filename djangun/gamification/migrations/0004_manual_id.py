from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamification', '0003_auto_20211124_2339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leveldefinition',
            name='level_phase',
        ),
    ]
