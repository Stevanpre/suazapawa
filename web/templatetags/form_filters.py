from django import template
from django.forms.boundfield import BoundField

register = template.Library()

@register.filter
def add_class(field, css_class):
    if not isinstance(field, BoundField):
        return field
    existing = field.field.widget.attrs.get("class", "")
    return field.as_widget(attrs={"class": f"{existing} {css_class}".strip()})
