# Generated by Django 2.0.6 on 2018-07-21 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0003_uniquescan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uniquescan',
            name='user_id',
            field=models.ForeignKey(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, to='testapp.Testuser'),
        ),
    ]
