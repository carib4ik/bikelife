from django import template
from mainapp.models import Article


register = template.Library()

@register.simple_tag()
def get_articles_service():
    return Article.objects.filter(category=2)

@register.simple_tag()
def get_articles_travel():
    return Article.objects.filter(category=1)




