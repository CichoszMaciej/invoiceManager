# Generated by Django 3.1.7 on 2021-03-21 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_place_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='nip',
            field=models.CharField(max_length=64, null=True, verbose_name='NIP'),
        ),
        migrations.AlterField(
            model_name='place',
            name='address',
            field=models.CharField(max_length=255, null=True, verbose_name='Adres'),
        ),
        migrations.AlterField(
            model_name='place',
            name='invoice_code',
            field=models.CharField(max_length=5, null=True, verbose_name='Kod faktury'),
        ),
        migrations.AlterField(
            model_name='place',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Czy aktywny?'),
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name='Nazwa'),
        ),
    ]
