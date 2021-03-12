from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='home'),
    path('product/<str:slug>', ProductPage.as_view(), name='product'),
    path('category/<str:slug>', ProductByCategory.as_view(), name='category'),
    path('shop/', Shop.as_view(), name='shop'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('tips/', Tips.as_view(), name='tips'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),

]