from django import template

register = template.Library()

@register.filter(name='to_int')

def to_int(value):
    print(value)
    if value == 'True':
        return 1
    else:
        return 0
