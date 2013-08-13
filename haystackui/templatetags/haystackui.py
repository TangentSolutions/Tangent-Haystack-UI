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
    
    

