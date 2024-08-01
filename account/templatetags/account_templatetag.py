from django import template

register = template.Library()

# Navbar
@register.inclusion_tag('partials/Navbar.html')
def show_navbar(count=5):
    return {'section': 'dashboard', 'on': True}
