from django import forms
from django.core.validators import MinValueValidator
from django.forms import widgets

from shop_app.models import Product


class ProductForm(forms.ModelForm):
    remain = forms.IntegerField(min_value=0)
    prod_price = forms.DecimalField(max_digits=7, decimal_places=2)

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

