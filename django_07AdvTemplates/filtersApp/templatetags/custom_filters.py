from django import template
register = template.Library()

def first_eight_upper(value):
    return value[:8].upper()

register.filter('f8upper',first_eight_upper)

@register.filter(name='fnlower')
def first_n_lower(value,index):
    return value[:index].lower()+value[index:]