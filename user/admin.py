from django.contrib import admin

# Register your models here.

from . models import *

class subcategoryAdmin(admin.ModelAdmin):
    list_display = ('name','date','id')
admin.site.register(subcategory,subcategoryAdmin)

class productAdmin(admin.ModelAdmin):
    list_display = ('id','category','subcategory','name','price','dis_price','size','color','descriptions','date','img')
admin.site.register(product,productAdmin)

class contactAdmin(admin.ModelAdmin):
    list_display = ('fname','mob_no','email','msg','id')
admin.site.register(contact_info,contactAdmin)

class addToCartAdmin(admin.ModelAdmin):
    list_display = ('user_id','product_id','status','add_date','id')
admin.site.register(add_to_cart,addToCartAdmin)

class MyOrdersAdmin(admin.ModelAdmin):
    list_display = ('user_id','product_id','status','remark','order_date')
admin.site.register(orders,MyOrdersAdmin)

class sign_upAdmin(admin.ModelAdmin):
    list_display = ('name','mob_no','email','password','img','address')
admin.site.register(sign_up_info,sign_upAdmin)