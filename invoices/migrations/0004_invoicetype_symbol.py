# Generated by Django 3.1.7 on 2021-03-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0003_auto_20210313_1136'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicetype',
            name='symbol',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
