from django import template
from store.models import Category

register = template.Library()


@register.inclusion_tag('store/categories.html')
def show_categories(menu_class='submenu'):
    categories = Category.objects.all()
    return {'categories': categories, "menu_class": menu_class}
