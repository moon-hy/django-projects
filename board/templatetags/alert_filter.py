from django.template import Library

register = Library()

@register.filter(name='show_error')
def show_error(dictionary):
    try:
        print(sorted(list(dictionary.items()))[-1])
        return dictionary
    except (TypeError,IndexError,AttributeError):
        return 'tip: try again'