from . import views

from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('',views.index,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),
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
    path('happy/<int:id>',views.happy_like,name='happylike'),
    path('handlerequest',views.handlerequest,name='HndleRequest'),
]