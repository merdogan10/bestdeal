from django import template
from bestdeal.models import Category,Sub_Category

register = template.Library()

@register.inclusion_tag('menu_items.html', takes_context=True)
def menu_items(context):
    return {'categories': Category.objects.all(), 'sub_categories': Sub_Category.objects.all()}