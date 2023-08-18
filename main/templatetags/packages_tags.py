from django import template
from django.template.loader import render_to_string


register = template.Library()


@register.inclusion_tag("main/packages_tag.html")
def render_packages(packages):
    return {"packages": packages}
