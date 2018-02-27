from django import template

register=template.Library()

@register.simple_tag
def mymethod(v1):
    result=v1*1000
    return result