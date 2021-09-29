from django.db import models

# Create your models here.

#for sub-category details.....

class subcategory(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=60)
    date = models.DateField()
    def __str__(self):
        return self.name

#for product details......

class product(models.Model):
    id = models.AutoField
    category = models.CharField(max_length=20)
    subcategory = models.ForeignKey(subcategory,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    dis_price = models.FloatField()
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    descriptions = models.CharField(max_length=300)
    date = models.DateField()
    img = models.ImageField(upload_to="static/products/", default="")
    def __str__(self):
        return self.name

class contact_info(models.Model):
    id = models.AutoField
    fname = models.CharField(max_length=70)
    mob_no = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    msg = models.TextField(max_length=1000)
    def __str__(self):
        return self.fname

class add_to_cart(models.Model):
    cart_id = models.AutoField
    product_id = models.IntegerField()
    user_id = models.CharField(max_length=50)
    status = models.BooleanField()
    add_date = models.DateField()
    def __str__(self):
        return self.user_id

class orders(models.Model):
    order_id = models.AutoField
    product_id = models.IntegerField()
    user_id = models.CharField(max_length=50)
    remark = models.TextField(max_length=1000)
    status = models.BooleanField()
    order_date = models.DateField()
    def __str__(self):
        return self.user_id

class sign_up_info(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, primary_key=True)
    mob_no = models.CharField(max_length=25, unique=True)
    img = models.ImageField(upload_to="static/users/",null=True , default="")
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=500, null=True, default="")
    def __str__(self):
        return self.name