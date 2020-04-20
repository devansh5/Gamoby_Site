from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import *
from django.contrib.auth.decorators import login_required
from .models import *
import json
from PayTm import Checksum
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from cloudinary import api
from cloudinary.forms import cl_init_js_callbacks
from django.views.decorators.http import require_POST



def register(request):
    if request.user.is_authenticated:
        return redirect('/')

    if request.POST.get('act') == 'post':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        data = {'username':username,'email':email,'password1':password1,'password2':password2}
        form = CreateUserForm(data=data)
        if form.is_valid():
            
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            return HttpResponse(json.dumps({"message":"Success"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message":form.errors}),content_type="application/json")
    else:
        form=CreateUserForm()
    return HttpResponse(json.dumps({"message":"Denied"}),content_type="application/json")


def login(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.POST.get('action') == 'post':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth_login(request, user)
                    return HttpResponse(json.dumps({"message":"Success"}),content_type="application/json")
            else:
                return HttpResponse(json.dumps({"message":"inactive"}),content_type="application/json")
        else:
            return HttpResponse(json.dumps({"message": "invalid"}),content_type="application/json")
        return HttpResponse(json.dumps({"message":"denied"}),content_type="application/json")

@login_required(login_url='login')
def logoutuser(request):
    logout(request)
    return render(request,'game/index.html')
  

def index(request):
    product=Product.objects.order_by('pub_time')
    params={'product':product}
    return render(request,'game/index.html',params) 

def about(request):
    return render(request,'game/about.html')

def contact(request):
    return render(request,'game/contact.html')
def faq(request):
    return render(request,'game/faq.html')

@login_required(login_url='login')
def view_profile(request):
    args={'user':request.user}
    return render(request,'game/profile.html',args)

@login_required(login_url='login')
def edit_profile(request):
    try:
        user_profile = Profile.objects.get(user=request.user)
    except Profile.DoesNotExist:
        return HttpResponse("invalid user_profile!")


    if request.method == 'POST':
        form = EditProfileForm(request.POST ,instance=request.user)
        profile_form=ProfileUpdate(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            return redirect('profile')
    
    else:
        form = EditProfileForm(instance=request.user)
        profile_form=ProfileUpdate(instance=request.user.profile)
        args = {'form':form,'profile_form':profile_form}
        return render(request,'game/edit.html',args)

@login_required(login_url='login')
def password_change(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'Your Password was successfully updated! ')
            return redirect('profile')
        else:
            return redirect('changepassword')
    else:
        form=PasswordChangeForm(request.user)

        args={'form':form}
        return render(request,'game/passwordchange.html',args)


def productreview(request):
    products=Product.objects.all()
    paginator=Paginator(products,9)
    page=request.GET.get('page')
    products=paginator.get_page(page)
    params={'products':products}
    return render(request,'game/productreview.html',params)


def detail(request,pk):
    product=Product.objects.get(pk=pk)
    is_fav=False
    is_liked=False
    if product.likes.filter(id=request.user.id).exists():
        is_liked=True
    if product.favs.filter(id=request.user.id).exists():
        is_fav=True
    context={'product':product,'is_liked':is_liked,'is_fav':is_fav,'total_likes':product.total_likes()}
    return render(request,'game/productdetail.html',context)


def happy(request):
    happys=Happy.objects.all()
    paginator=Paginator(happys,9)
    page=request.GET.get('page')
    happys=paginator.get_page(page)
    is_happylike=False
    params={'happys':happys}
    return render(request,'game/happycustomer.html',params)

def happy_like(request):
    happy_id=request.POST.get('id')
    action=request.POST.get('action')
    if happy_id and action:
        try:
            happy=Happy.objects.get(id=happy_id)
            if action == 'like':
                happy.happylikes.add(request.user)
            else:
                happy.happylikes.remove(request.user)
            return HttpResponse(json.dumps({"message":"Success"}),content_type="application/json")
        except:
            pass
    return HttpResponse(json.dums({"message":"Error"}),content_type="application/json")



def like(request):
    # product=get_object_or_404(Product,id=request.POST.get('product_id'))
    product=get_object_or_404(Product,id=request.POST.get('id'))
    
    is_liked=False
    if product.likes.filter(id=request.user.id).exists():
        product.likes.remove(request.user)
        is_liked=False
    else:
        product.likes.add(request.user)
        is_liked=True
    context={'product':product,'is_liked':is_liked,'total_likes':product.total_likes()}
    if request.is_ajax():
        html=render_to_string('game/like_section.html',context,request=request)
        return JsonResponse({'form':html})


def fav(request):
    product=get_object_or_404(Product,id=request.POST.get('id'))
    
    is_fav=False
    if product.favs.filter(id=request.user.id).exists():
        product.favs.remove(request.user)
        is_fav=False
    else:
        product.favs.add(request.user)
        is_fav=True
    context={'product':product,'is_fav':is_fav}
    if request.is_ajax():
        html=render_to_string('game/fav_section.html',context,request=request)
        return JsonResponse({'form':html})


@login_required
def wishlist(request):
    user=request.user
    liked_products=user.favs.all()
    context={
        'liked_products':liked_products
    }
    return render(request,'game/wishlist.html',context)

def previousorders(request):
    designs=Design.objects.filter(owner=request.user)
    context={'designs':designs}
    return render(request,'game/design_list.html',context)

@login_required
def upload(request):
    try:
        user_profile=Profile.objects.get(user=request.user)
    except:
        return HttpResponse("need to login")
    context=dict(form=DesignForm())
    if request.method == 'POST':
        design=Design(owner=request.user)
        
        form=DesignForm(request.POST,request.FILES,instance=design)
        if form.is_valid():
            design.save()
            myorder=form.save()
            return redirect('show',pk=myorder.pk)

    else:
        form=DesignForm()
    return render(request,'game/design_form.html',context)

@login_required
def show(request,pk):
    designs=Design.objects.get(pk=pk)
    user=request.user
    order_id=designs.pk
    print(order_id)
    
    amount=1000
    print(amount)
    ICON_EFFECTS=dict(
        format="jpg",
        transformation = [
            dict(height=55,width=50,crop="scale"),
            dict(underlay="shirts",width=200,height=250,crop='crop'),
            dict(crop='scale',gravity="center",y=20,x=-20),
        ]
    )
    if request.method == 'POST':
        param_dict = {
            'MID':'TrFKjj53488482516882',
            'ORDER_ID':str(order_id),
            'TXN_AMOUNT':str(amount),
            'CUST_ID':user.email,
            'INDUSTRY_TYPE_ID':'Retail',
            'WEBSITE':'WEBSTAGING',
            'CHANNEL_ID':'WEB',
            'CALLBACK_URL':'http://127.0.0.8000/handlerequest/',
    }
        param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        return render(request,'game/paytm.html',{'param_dict':param_dict})
     
    context={'designs':designs,'ICON_EFFECTS':ICON_EFFECTS,'user':user}
    return render(request,'game/show.html',context)

@csrf_exempt       
def handlerequest(request):
    return HttpResonse("It's working")
    pass






def load_colors(request):
    item_id = request.GET.get('item')
    colors = Color.objects.filter(item_id=item_id).order_by('name')
    return render(request,'game/color_dropdown_list_options.html',{'colors':colors})


def load_sizes(request):
    color_id = request.GET.get('color')
    sizes = Size.objects.filter(color_id=color_id).order_by('name')
    return render(request,'game/size_dropdown_list_options.html',{'sizes':sizes})



