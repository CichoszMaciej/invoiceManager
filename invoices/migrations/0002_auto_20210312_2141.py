# Generated by Django 3.1.7 on 2021-03-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sales_date',
            field=models.DateField(null=True),
        ),
    ]
