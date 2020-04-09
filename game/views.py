from __future__ import unicode_literals
from django.shortcuts import render,redirect,get_object_or_404,reverse
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from .forms import CreateUserForm,EditProfileForm,ProfileUpdate
from django.contrib.auth.decorators import login_required
from .models import *
import json

from django.core.paginator import Paginator
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode





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
    return render(request,'game/index.html') 

def about(request):
    return render(request,'game/about.html')

def contact(request):
    return render(request,'game/contact.html')

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



def wishlist(request):
    user=request.user
    liked_products=user.favs.all()
    context={
        'liked_products':liked_products
    }
    return render(request,'game/wishlist.html',context)