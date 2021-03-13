from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from products.forms import ProductCreate
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
            product.save()
            return HttpResponseRedirect(reverse(product_list) + '?info=success')
        else:
            return render(request, 'products/new_product.html', {'form': form})

    else:
        context = {
            'form': ProductCreate()
        }

        return render(request, 'products/new_product.html', context)
