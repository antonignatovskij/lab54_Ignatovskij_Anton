from urllib.parse import urlencode

from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from shop_app.models import Product, Category, Cart

from shop_app.forms import ProductForm, CategoryForm, SearchForm

# Create your views here.

class ProductListView(ListView):
    template_name = 'shop_app_temp/index.html'
    context_object_name = 'products'
    model = Product
    queryset = Product.objects.all().filter(remain__gt=0)
    paginate_by = 6

    def dispatch(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_form'] = SearchForm()
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            queryset = queryset.filter(
                Q(prod_title__icontains=self.search_value) | Q(prod_desc__icontains=self.search_value))
        return queryset

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']


class ProductDetailView(DetailView):
    template_name = 'shop_app_temp/product_detail.html'
    model = Product


class CategoryCreateView(CreateView):
    template_name = 'shop_app_temp/category_create.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products_list')

class ProductCreateView(CreateView):
    template_name = 'shop_app_temp/product_create.html'
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductUpdateView(UpdateView):
    template_name = 'shop_app_temp/product_update.html'
    model = Product
    form_class = ProductForm
    context_object_name = 'product'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})


class ProductDeleteView(DeleteView):
    template_name = 'shop_app_temp/product_delete.html'
    model = Product
    context_object_name = 'product'
    success_url = reverse_lazy('products_list')



class CartAddView(CreateView):
    model = Cart
    fields = []

    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, pk=self.kwargs["pk"])

        if product.remain == 0:
            return redirect("products_list")

        item = Cart.objects.filter(product=product).first()
        if item:
            if item.quantity < product.remain:
                item.quantity += 1
                item.save()
        else:
            Cart.objects.create(
                product=product,
                quantity=1
            )
        return redirect("products_list")


class CartListView(ListView):
    model = Cart
    template_name = "shop_app_temp/cart.html"
    context_object_name = "items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        total = 0
        for item in context["items"]:
            total += item.product.price * item.quantity

        context["total"] = total
        return context


class CartDeleteView(DeleteView):
    template_name = 'shop_app_temp/cart.html'
    model = Cart
    success_url = reverse_lazy("cart_list")