from decimal import Decimal

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from products.forms import ProductForm, ProductCreate
from products.models import Product


@login_required()
def product_list(request):
    products = Product.objects.all()
    info = ''
    if 'info' in request.GET:
        info = request.GET['info']
    context = {
        'products': products,
        'length': len(products),
        'info': info
    }

    return render(request, 'products/products_list.html', context)


@login_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductCreate(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.price_net = (float(product.cost) * (1 + (float(product.gain) / 100)))
            product.price_gross = float(product.price_net) * (1 + (product.vat_rate.value / 100))
            product.price_vat = product.price_gross - product.price_net
            product.save()
            return HttpResponseRedirect(reverse(product_list) + '?info=success')
        else:
            return render(request, 'products/new_product.html', {'form': form})

    else:
        context = {
            'form': ProductCreate(initial={'quantity_stock': 1})
        }

        return render(request, 'products/new_product.html', context)


@login_required()
def edit_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.price_gross = (product.vat_rate.value / Decimal(100) + Decimal(1)) * product.price_net
            product.price_vat = product.price_gross - product.price_net
            product.save()
            return HttpResponseRedirect(reverse(product_list) + '?info=success-edit')
        else:
            return render(request, 'products/edit_product.html', {'product_name': product.name, 'form': form})
    else:
        context = {
            'product_name': product.name,
            'form': ProductForm(instance=product)
        }
        return render(request, 'products/edit_product.html', context)
