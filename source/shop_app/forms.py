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




    # prod_title = models.CharField(max_length=70, null=False, blank=False, verbose_name="Product Title")
    # prod_desc = models.CharField(max_length=400, null=True, blank=True, verbose_name="Product Description")
    # category = models.ForeignKey("shop_app.Category", on_delete=models.RESTRICT, related_name="shop_app", null=False, blank=False, verbose_name="Product Category")
    # date_of_add = models.DateField(auto_now_add=True, verbose_name="Product Date of Add")
    # price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Product Price")
    # product_image = models.URLField(max_length=400, null=False, blank=False, verbose_name="Product Image")
    # remain = models.IntegerField(default=0, null=True, blank=True, verbose_name="Product Remain")