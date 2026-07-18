from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets

from shop_app.models import Product, Category, Order


class ProductForm(forms.ModelForm):
    remain = forms.IntegerField(min_value=0)
    price = forms.DecimalField(max_digits=7, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Product
        fields = ('prod_title', 'prod_desc', 'category', 'price', 'product_image', 'remain')
        widgets = {
            'prod_desc': widgets.Textarea(attrs={'cols': '40', 'rows': '5'})
        }

class CategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Category
        fields = ('cat_title', 'cat_desc')
        widgets = {
            'cat_desc': widgets.Textarea(attrs={'cols': '40', 'rows': '5'})
        }

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Найти")

class OrderForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Order
        fields = [
            "customer_name",
            "address",
            "phone"
        ]