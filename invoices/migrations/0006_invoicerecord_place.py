# Generated by Django 3.1.7 on 2021-03-15 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210315_2159'),
        ('invoices', '0005_auto_20210313_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicerecord',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='places.place'),
        ),
    ]