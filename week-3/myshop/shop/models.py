from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=150, null=False)
    last_name = models.CharField(max_length=200, null=False)
    email = models.CharField(max_length=150, null=False)
    address = models.JSONField(null=False)

class Cart(models.Model):
    customer = models.IntegerField(null=False)
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True, null=False)
    expired_in = models.IntegerField(default=60, null=False)

class CartItem(models.Model):
    cart = models.IntegerField(null=False)
    cart = models.ForeignKey("shop.Cart", on_delete=models.CASCADE)
    product = models.IntegerField(null=False)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, null=False)

class Order(models.Model):
    customer = models.IntegerField(null=False)
    customer = models.ForeignKey("shop.Customer", on_delete=models.CASCADE)
    order_date = models.DateField(auto_now_add=True, null=False)
    remark = models.TextField(null=True)
    
    # One-to-One
    payment = models.OneToOneField("shop.Payment", on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.IntegerField(null=False)
    order = models.ForeignKey("shop.Order", on_delete=models.CASCADE)
    product = models.IntegerField(null=False)
    product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)
    amount = models.IntegerField(default=1, null=False)
    
    # One-to-One
    payment_item = models.OneToOneField("shop.PaymentItem", on_delete=models.CASCADE)

class ProductCategory(models.Model):
    name = models.CharField(max_length=150, null=False)

# class product_categories(models.Model):
#     product_category = models.IntegerField(null=False, primary_key=True)
#     product_category = models.ForeignKey("shop.ProductCategory", on_delete=models.CASCADE)
#     product = models.IntegerField(null=False, primary_key=True)
#     product = models.ForeignKey("shop.Product", on_delete=models.CASCADE)

class Product(models.Model):
    name = models.CharField(max_length=150, null=False)
    description = models.TextField(null=True)
    remaining_amount = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    
    # Many-to-Many
    categories = models.ManyToManyField("shop.ProductCategory")

class Payment(models.Model):
    # order = models.IntegerField(null=False)
    # order = models.ForeignKey("shop.Order", on_delete=models.CASCADE)
    
    payment_date = models.DateField(auto_now_add=True, null=False)
    remark = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount =  models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)
    
    # One-to-One
    payment_method = models.OneToOneField("shop.PaymentMethod", on_delete=models.CASCADE)

class PaymentItem(models.Model):
    # payment = models.IntegerField(null=False)
    # payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)
    
    # order_item = models.IntegerField(null=False)
    # order_item = models.ForeignKey("shop.OrderItem", on_delete=models.CASCADE)
    
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    discount =  models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)

class PaymentMethod(models.Model):
    # payment = models.IntegerField(null=False)
    # payment = models.ForeignKey("shop.Payment", on_delete=models.CASCADE)

    QR = "QR"
    CREDIT = "CC"
    PAYMENT_METHODS = {
        QR: "QR Code",
        CREDIT: "Credit Card"
    }

    method = models.CharField(
        max_length=2,
        choices=PAYMENT_METHODS,
        null=False
    )

    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=False)