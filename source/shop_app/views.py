from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from shop_app.models import Product, Category

from shop_app.forms import ProductForm

# Create your views here.

def products_view(request):
    products = Product.objects.all().order_by('-category','-prod_title')
    products = products.filter(remain__gt=0)
    return render(request, 'shop_app_temp/index.html', {'products': products})

def product_view(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'shop_app_temp/product_detail.html', context)

def category_add_view(request):
    if request.method == 'POST':
        new_category = {
            'title': request.POST.get('cat_title').strip(),
            'desc': request.POST.get('cat_desc')
        }
        if new_category['title'] == '':
            varning = {'varning': 'No title'}
            return render(request, 'shop_app_temp/category_create.html', varning)
        category = Category.objects.create(
            cat_title=new_category['title'],
            cat_desc=new_category['desc']
        )
        return redirect('products_list')
    return render(request, 'shop_app_temp/category_create.html')

def product_add_view(request):
    form = ProductForm()
    if request.method == 'GET':
        return render(request, 'shop_app_temp/product_create.html', {'form': form})
    form = ProductForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('products_list')
    return render(request, 'shop_app_temp/product_create.html', {'form': form})


def product_update_view(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_list')
        return render(request, 'shop_app_temp/product_update.html', {'form': form})
    form = ProductForm(instance=product)
    context = {'form': form, 'action': reverse('product_update', kwargs={'pk': product.pk})}
    return render(request, 'shop_app_temp/product_update.html', context)


def product_delete_view(request, pk, *args, **kwargs):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        return render(request, 'shop_app_temp/product_delete.html')
    if request.method == 'POST':
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        return redirect('products_list')
