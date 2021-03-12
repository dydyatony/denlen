from django.contrib import admin
from django import forms
from django.utils.safestring import mark_safe

from ckeditor_uploader.widgets import CKEditorUploadingWidget

# Register your models here.

from .models import *


# это служебный класс. не трогать
class PostAdmin(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class ProductAdmin(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class PostTagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdmin
    list_display = ('id', 'title', 'slug', 'created_at', 'get_photo')
    save_on_top = True
    list_display_links = ('id', 'title', 'slug')
    search_fields = ('title',)
    # list_filter = ('tags')
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'author', 'created_at', 'content', 'first_photo', 'views', 'tags',
              'as_published',)
    save_as = True

    def get_photo(self, obj):
        if obj.first_photo:
            return mark_safe(f'<img src="{obj.first_photo.url}" width ="50">')
            # return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = ProductAdmin
    list_display = ('id', 'title', 'slug', 'real_price', 'views', 'bought')
    save_on_top = True
    list_display_links = ('id', 'title', 'slug')
    readonly_fields = ('views', 'bought', 'get_photo')

    def get_photo(self, obj):
        if obj.first_photo:
            return mark_safe(f'<img src="{obj.first_photo.url}" width ="50">')
            # return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'photo'


admin.site.register(PostTag, PostTagAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
