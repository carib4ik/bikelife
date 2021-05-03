from django import template

from mainapp.models import Article, Category

register = template.Library()


# @register.simple_tag()
# def get_articles_service():
#     return Article.objects.filter(category=2)
#
# @register.simple_tag()
# def get_articles_travel():
#     return Article.objects.filter(category=1)

@register.simple_tag()
def get_categories():
    return Category.objects.all()


# @register.inclusion_tag('mainapp/navbar_menu_tpl.html')
# def show_menu(menu_class='menu'):
#     articles = Article.objects.all()
#     return {'articles': articles, 'menu_class': menu_class}
