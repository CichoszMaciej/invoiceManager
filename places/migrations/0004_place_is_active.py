# Generated by Django 3.1.7 on 2021-03-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210315_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
