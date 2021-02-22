from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import ListView, DetailView
from .models import *


from django.db.models import F

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

