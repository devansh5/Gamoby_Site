from . import views

from django.urls import path

urlpatterns=[
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('logout/',views.logoutuser,name='logout'),
    path('profile/',views.view_profile,name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('profile/passwordchange/',views.password_change,name='password_change'),
    path('like/',views.like,name='like'),
    path('fav/',views.fav,name='fav'),
    path('wishlist/',views.wishlist,name='wishlist'),
    path("productreview/",views.productreview,name="shophome"),
    path('productreview/<int:pk>/',views.detail,name="detailproduct"),
    path('happy/',views.happy,name='happy'),
    path('list/',views.previousorders,name='design_changelist'),
    path('add/',views.upload,name="design_add"),
    path('ajax/load-colors/',views.load_colors,name='ajax_load_colors'),
    path('ajax/load-sizes/',views.load_sizes,name='ajax_load_sizes'),
    path('add/<int:pk>/',views.show,name='show'),
    path('handlerequest',views.handlerequest,name='HndleRequest'),
    path('happylike/',views.happy_like,name='happy_like')
]