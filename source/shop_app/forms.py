from django import forms
from django.forms import widgets

from shop_app.models import Product, Category


class ProductForm(forms.ModelForm):
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

