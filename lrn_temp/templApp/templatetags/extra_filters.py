from django import template

register = template.Library()

@register.filter(name='cut')
def my_cut(value,arg):
    """
    This cuts out all values of 'arg' from the the string
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
