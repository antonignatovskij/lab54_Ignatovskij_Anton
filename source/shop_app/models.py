from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=70, null=False, blank=False, unique=True, verbose_name="Category Title")
    cat_desc = models.CharField(max_length=200, null=True, blank=True, verbose_name="Category Description")


class Product(models.Model):
    prod_title = models.CharField(max_length=70, null=False, blank=False, verbose_name="Product Title")
    prod_desc = models.CharField(max_length=400, null=True, blank=True, verbose_name="Product Description")
    category = models.ForeignKey("shop_app.Category", on_delete=models.RESTRICT, related_name="shop_app", null=False, blank=False, verbose_name="Product Category")
    date_of_add = models.DateField(auto_now_add=True, verbose_name="Product Date of Add")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Product Price")
    product_image = models.URLField(max_length=400, null=False, blank=False, verbose_name="Product Image")

    def __str__(self):
        return self.prod_title

    class Meta:
        db_table = 'Products'
        verbose_name = 'product'
