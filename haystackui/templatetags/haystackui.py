from django import template
register = template.Library()

@register.assignment_tag
def get_active_facets(request):
    """
    Returns the values that are being used to filter
    """
    return request.GET.getlist("selected_facets")
    
@register.assignment_tag
def get_active_facet_filters(request):
    """
    Returns the values that are being used to filter
    """
    qs_facets = request.GET.getlist("selected_facets")
    return [value.split(":")[1] for value in qs_facets]

@register.filter(name='facet_for_humans')
def facet_for_humans(facet):
    return facet.split(":")[1]


@register.filter(name='remove_facet')
def remove_facet(path, facet):

    try:
        url, qs = path.split("?")
        facet_to_remove = "selected_facets=%s" % facet
        key_values = qs.split("&")
        if facet_to_remove in key_values: key_values.remove(facet_to_remove)

        return "%s?%s" % (url, ("&").join(key_values) )

    except ValueError:
        return path
    
    
    

