# Generated by Django 3.1.7 on 2021-03-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20210313_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Czy aktywny?'),
        ),
    ]
