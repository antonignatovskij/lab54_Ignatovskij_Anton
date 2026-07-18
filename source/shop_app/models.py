from django.db import models

# Create your models here.

class Category(models.Model):
    cat_title = models.CharField(max_length=70, null=False, blank=False, unique=True, verbose_name="Category Title")
    cat_desc = models.CharField(max_length=200, null=True, blank=True, verbose_name="Category Description")

    def __str__(self):
        return self.cat_title


class Product(models.Model):
    prod_title = models.CharField(max_length=70, null=False, blank=False, verbose_name="Наименование товара")
    prod_desc = models.CharField(max_length=400, null=True, blank=True, verbose_name="Детальное описание")
    category = models.ForeignKey("shop_app.Category", on_delete=models.RESTRICT, related_name="shop_app", null=False, blank=False, verbose_name="Категория")
    date_of_add = models.DateField(auto_now_add=True, verbose_name="Product Date of Add")
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False, verbose_name="Цена")
    product_image = models.URLField(max_length=400, null=False, blank=False, verbose_name="Картинка товара")
    remain = models.IntegerField(default=0, null=True, blank=True, verbose_name="кол-во на складе")

    def __str__(self):
        return self.prod_title

    class Meta:
        db_table = 'Products'
        verbose_name = 'product'

class Cart(models.Model):
    product = models.ForeignKey('shop_app.Product', related_name='cart', on_delete=models.CASCADE, null=False, blank=False, verbose_name="Корзина")
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product} ({self.quantity})"


class Order(models.Model):
    customer_name = models.CharField(max_length=100,verbose_name="Имя пользователя")
    phone = models.CharField(max_length=20,verbose_name="Телефон")
    address = models.CharField(max_length=255,verbose_name="Адрес")
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="Дата создания")
    products = models.ManyToManyField("Product",through="OrderItem",related_name="orders")

    def __str__(self):
        return f"Заказ №{self.id} ({self.customer_name})"

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name="items")
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1,verbose_name="Количество")

    def __str__(self):
        return f"{self.product} x {self.quantity}"