# Generated by Django 3.1.7 on 2021-03-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='invoiceCode',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
