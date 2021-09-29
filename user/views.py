from datetime import datetime
from unicodedata import category

from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from django.db import connection
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    p_data = product.objects.all().order_by("-id")
    sub_cat_data = subcategory.objects.all().order_by("-id")
    num_item = ""
    login_details = ""
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user,status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
    my_dict = {"data": p_data, "sub_data": sub_cat_data, "num_items": num_item, "login_details":login_details}
    return render(request,'user/index.html', context=my_dict)

def mens_product(request):
    s_id = request.GET.get("s_id")
    if s_id==None:
        p_data = product.objects.filter(category='Mens')
    else:
        p_data = product.objects.filter(category='Mens',subcategory=s_id)
    sub_cat_data = subcategory.objects.all().order_by("-id")
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user,status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        my_dict = {"data":p_data,"sub_data":sub_cat_data, "num_items": num_item, "login_details":login_details}
    else:
        my_dict = {"data": p_data, "sub_data": sub_cat_data}
    return render(request,'user/mens_product.html', context=my_dict)

def womens_product(request):
    s_id = request.GET.get("s_id")
    if s_id == None:
        p_data = product.objects.filter(category='Womens')
    else:
        p_data = product.objects.filter(category='Womens', subcategory=s_id)
    sub_cat_data = subcategory.objects.all().order_by("-id")
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user,status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        my_dict = {"data": p_data, "sub_data": sub_cat_data, "num_items": num_item, "login_details":login_details}
    else:
        my_dict = {"data": p_data, "sub_data": sub_cat_data}
    return render(request,'user/womens_product.html', context=my_dict)

def kids_product(request):
    s_id = request.GET.get("s_id")
    if s_id == None:
        p_data = product.objects.filter(category='Kids')
    else:
        p_data = product.objects.filter(category='Kids', subcategory=s_id)
    sub_cat_data = subcategory.objects.all().order_by("-id")
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user,status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        my_dict = {"data": p_data, "sub_data": sub_cat_data, "num_items": num_item, "login_details":login_details}
    else:
        my_dict = {"data": p_data, "sub_data": sub_cat_data}
    return render(request,'user/kids_product.html', context=my_dict)

def view_product(request):
    p_id = request.GET.get("p_id")
    p_data = product.objects.filter(id=p_id)
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user,status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        my_dict = {"data":p_data, "num_items": num_item, "login_details":login_details}
    else:
        my_dict = {"data": p_data}
    return render(request,'user/view_product.html', context=my_dict)

def my_cart(request):
    value = ""
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("Select p.id,p.name,p.img,p.category,p.price,p.dis_price,c.user_id,c.status,c.id from user_product p, user_add_to_cart c where p.id=c.product_id and user_id='"+str(request.user)+"' and status=True order by c.id desc")
        value = cursor.fetchall()
        if request.user.is_authenticated:
            num_item = add_to_cart.objects.filter(user_id=request.user, status=True).count()
            login_details = sign_up_info.objects.filter(email=request.user)
        if request.GET.get('c_id'):
            c_id = request.GET.get('c_id')
            delt = add_to_cart.objects.filter(id=c_id)
            delt.delete()
            return HttpResponse("<script>window.location.href='/my_cart/';</script>")
    return render(request, 'user/my_cart.html', {"value":value, "num_items": num_item, "login_details":login_details})

def my_orders(request):
    value1 = ""
    value2 = ""
    if request.user.is_authenticated:
        cursor = connection.cursor()
        cursor.execute("Select p.id,p.name,p.img,p.category,p.price,p.dis_price,o.user_id,o.status,o.id,o.order_date,o.remark from user_product p, user_orders o where p.id=o.product_id and user_id='"+str(request.user)+"' and status=True and remark='On the way' order by o.id desc")
        value1 = cursor.fetchall()
        cursor.execute("Select p.id,p.name,p.img,p.category,p.price,p.dis_price,o.user_id,o.status,o.id,o.order_date,o.remark from user_product p, user_orders o where p.id=o.product_id and user_id='"+str(request.user)+"' and status=True and remark='Delivered' order by o.id desc")
        value2 = cursor.fetchall()
        num_item = add_to_cart.objects.filter(user_id=request.user, status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        if request.GET.get('c_id'):
            c_id = request.GET.get('c_id')
            delt = orders.objects.filter(id=c_id)
            delt.delete()
            return HttpResponse("<script>window.location.href='/my_orders/';</script>")
    return render(request,'user/my_orders.html', {"value1":value1,"value2":value2, "num_items": num_item, "login_details":login_details})

def my_profile(request):
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user, status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        if request.method=="POST":
            name = request.POST['u_fname']
            mob_no = request.POST['u_mob_no']
            #email = request.POST['u_email']
            img = request.FILES['u_img']
            address = request.POST['u_address']
            res = sign_up_info(email=request.user, name=name, mob_no=mob_no, img=img, address=address)
            res.save()
    return render(request,'user/my_profile.html', {"num_items": num_item, "login_details":login_details})

def contact_us(request):
    status = False
    if request.method == "POST":
        Name = request.POST.get("fname","")
        Mobile = request.POST.get("mob_no", "")
        Message = request.POST.get("msg","")
        Email = request.POST.get("email", "")
        res = contact_info(fname=Name,mob_no=Mobile,email=Email,msg=Message)
        res.save()
        status=True
    if request.user.is_authenticated:
        num_item = add_to_cart.objects.filter(user_id=request.user, status=True).count()
        login_details = sign_up_info.objects.filter(email=request.user)
        return render(request, 'user/contact_us.html', context={"S":status, "num_items": num_item, "login_details":login_details})
    return render(request,'user/contact_us.html', context={"S":status})

def sign_up(request):
    status = ""
    if request.method == "POST":
        if request.POST.get("u_password")==request.POST.get("u_cpassword"):
            Name = request.POST.get("u_name")
            Mob_no  = request.POST.get("u_mob_no")
            Email = request.POST.get("u_email")
            Img = request.FILES.get("u_img")
            Password = request.POST.get("u_password")
            Address = request.POST.get("u_address")
            res = sign_up_info(name=Name,email=Email,mob_no=Mob_no,img=Img,password=Password,address=Address)
            res.save()
            myuser = User.objects.create_user(Email,Email,Password)
            myuser.first_name = Name
            myuser.last_name = Name
            myuser.save()
            status = "Registration Successfully."
        else:
            status="Password and Confirm password does not matched."
    return render(request,'user/sign_up.html', context={"S":status})

def sign_in(request):
    if request.user.is_authenticated:
        product_id = request.GET.get('p_id')
        page = request.GET.get('page')
        username = request.user
        if page == 'cart':
            check_item = add_to_cart.objects.filter(product_id=product_id,user_id=username,status=True)
            if check_item:
                return render(request, 'user/sign_in.html', context={"already_added":True})
            save_to_cart = add_to_cart(product_id=product_id,user_id=username,status=True,add_date=datetime.now().date())
            save_to_cart.save()
        elif page == 'order':
            save_to_order = orders(product_id=product_id,user_id=username,remark="On the way",status=True,order_date=datetime.now().date())
            save_to_order.save()
            delt = add_to_cart.objects.filter(product_id=product_id,user_id=username,status=True)
            delt.delete()
            return HttpResponse("<script>alert('Order is Confirmed.');window.close();</script>")
        #return HttpResponse("<script>location.replace('/index/');</script>")
        return render(request,'user/sign_in.html', context={"al_logged_in":True})
    else:
        return render(request,'user/sign_in.html')

def signin(request):
    if request.method == 'POST':
        Email = request.POST.get("u_email", "")
        Password = request.POST.get("u_password", "")
        user = auth.authenticate(username=Email, password=Password)
        #print(user)
        if user is not None:
            login(request,user)
            return render(request, 'user/sign_in.html', context={"User":True})
        else:
            return render(request,'user/sign_in.html', context={"NoUser":True})

def log_out(request):
    logout(request)
    return render(request,'user/index.html')