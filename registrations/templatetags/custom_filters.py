from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter
def add_placeholder(field, placeholder_text):
    return field.as_widget(attrs={"placeholder": placeholder_text, "class": "form-control"})

