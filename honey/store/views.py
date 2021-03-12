from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import *

from django.db.models import F

from django.urls import reverse


# Create your views here.

def index(request):
    return render(request, 'store/index.html')


def product(request):
    return render(request, 'store/product.html')


def shop(request):
    return render(request, 'store/shop.html')


def contact(request):
    return render(request, 'store/contact.html')


def blog(request):
    return render(request, 'store/blog.html')


def get_post(request):
    return render(request, 'store/blog.html')


class Tips(ListView):
    model = Post
    template_name = 'store/tips.html'
    context_object_name = 'posts'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tips'
        return context


class GetPost(DetailView):
    model = Post
    template_name = 'store/blog.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context


class Shop(ListView):
    model = Product
    template_name = 'store/shop.html'
    context_object_name = 'products'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Honey Store'
        return context


class ProductByCategory(ListView):
    model = Product
    template_name = 'store/shop.html'
    context_object_name = 'products'
    allow_empty = False
    paginate_by = 6

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class ProductPage(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.object.views = F('views') + 1
        self.object.save()
        self.object.refresh_from_db()
        return context
