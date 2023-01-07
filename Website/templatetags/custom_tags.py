from django import template

register = template.Library()

def a_tag(text):
    return text.replace('<a' , '<a target="_blank" rel="noopener noreferrer" class="link-warning"')

a_tag = register.filter(a_tag, is_safe = True)