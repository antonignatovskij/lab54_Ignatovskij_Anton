from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect

from shop_app.models import Product, Category

from shop_app.prod_validation import PrdVld

# Create your views here.

def products_view(request):
    products = Product.objects.all()
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
    context = {'categories': Category.objects.all()}
    if request.method == 'POST':
        print(1231231212)
        new_product = {
            'title': request.POST.get('title').strip(),
            'desc': request.POST.get('desc').strip(),
            'category': request.POST.get('category'),
            'price': request.POST.get('price').strip(),
            'image': request.POST.get('img').strip()
        }
        print(new_product)
        flag = PrdVld.validate(new_product)
        print(11111)
        print(flag)
        if flag == True:
            product = Product.objects.create(
                prod_title = new_product['title'],
                prod_desc = new_product['desc'],
                price = new_product['price'],
                product_image = new_product['image'],
                category_id = int(new_product['category']),
            )
        else:
            varning = {'varning': flag}
            print(1233213212)
            print(varning)
            return render(request, 'shop_app_temp/product_create.html', varning)
        return redirect('product_detail', pk=product.pk)
    return render(request, 'shop_app_temp/product_create.html', context)

