from django import template


register = template.Library()

@register.filter
def precio_bs(value):
	return "{0} BsS".format(value)
