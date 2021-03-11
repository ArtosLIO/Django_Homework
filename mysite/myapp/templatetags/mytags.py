from django import template
from random import randint, choice
from string import ascii_letters

register = template.Library()

@register.filter(name='random_int')
def random_int(value):
    return randint(0, 100)

@register.filter(name='random_slug')
def random_slug(value):
    str = ascii_letters + '0123456789'
    slug = ''
    iter = randint(5, 10)
    for i in range(0, iter):
        slug += choice(str)
        if i+1 == iter//2:
            slug += '-'
    return slug

