from django.urls import path
from .views import *

urlpatterns =[
    path('', index, name='home'),
    path('product/', product, name='product'),
    path('shop/', shop, name='shop'),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('tips/', Tips.as_view(), name='tips'),
    path('post/<str:slug>', GetPost.as_view(), name='post'),

]