from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active_class(context, url_name_or_path):
    """Return 'text-indigo-600 font-semibold' when the current request path starts with the given path or matches url_name_or_path."""
    request = context.get('request')
    if not request:
        return ''
    path = request.path
    # allow passing in either a path prefix like '/customer' or a full path
    if not url_name_or_path:
        return ''
    if url_name_or_path.endswith('/'):
        check = url_name_or_path
    else:
        check = url_name_or_path
    if path.startswith(check):
        return 'text-indigo-600 font-semibold'
    return ''
