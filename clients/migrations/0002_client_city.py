# Generated by Django 3.1.7 on 2021-03-13 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
