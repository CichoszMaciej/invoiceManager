# Generated by Django 3.1.7 on 2021-03-13 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20210313_1228'),
        ('invoices', '0004_invoicetype_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clients.client', verbose_name='Klient'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(null=True, verbose_name='Data wystawienia faktury'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_nr',
            field=models.CharField(max_length=128, null=True, verbose_name='Numer Faktury'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoices.invoicestatus', verbose_name='Status faktury'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='invoices.invoicetype', verbose_name='Typ faktury'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='month',
            field=models.IntegerField(null=True, verbose_name='Miesiąc'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid',
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='Ile zapłacono'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='payment_date',
            field=models.DateField(null=True, verbose_name='Data zapłaty'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price_gross',
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='Cena brutto'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price_net',
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='Cena netto'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='price_vat',
            field=models.DecimalField(decimal_places=2, max_digits=16, null=True, verbose_name='Wartość VAT'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='sales_date',
            field=models.DateField(null=True, verbose_name='Data sprzedaży'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='year',
            field=models.IntegerField(null=True, verbose_name='Rok'),
        ),
    ]
