# HERE THE CUT IS THE CUSTOME FILTER.
from django import template

register = template.Library()
#USING DECORATERS IN PYTHON
@register.filter(name='cut')
def cut(value,arg):

    return value.replace(arg,'')

#register.filter('cut',cut)
