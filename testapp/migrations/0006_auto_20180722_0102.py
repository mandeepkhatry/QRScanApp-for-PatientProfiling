# Generated by Django 2.0.6 on 2018-07-21 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0005_auto_20180722_0047'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uniquescan',
            old_name='user_id',
            new_name='user',
        ),
    ]
