from django import template
from store.models import Post

register = template.Library()


@register.inclusion_tag('store/top_tips.html')
def show_top_tips(cnt=3):
    posts = Post.objects.order_by('-views')[:cnt]
    return {'posts': posts}
