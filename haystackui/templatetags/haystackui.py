from django import template
register = template.Library()
from django.template import RequestContext, Context


@register.assignment_tag
def get_active_facets(request):
    """
    Returns the values that are being used to filter
    """
    
    selected_facets = request.GET.getlist("selected_facets")
    return [(facet.split(":")[0].replace("_exact",""), facet.split(":")[1], 0) for facet in selected_facets]
    
@register.assignment_tag
def get_active_facet_filters(request):
    """
    Returns the values that are being used to filter
    """
    qs_facets = request.GET.getlist("selected_facets")
    return [value.split(":")[1] for value in qs_facets]

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

@register.simple_tag(takes_context=True)
def render_result(context):

    try:
        result = context["result"]
    except ValueError:
        raise Exception ("We need a SearchResult object in context")


    template_name = "search/components/%s.html" % result.content_type().replace(".", "/")
    request = context['request']
    
    try:

        template_to_render = template.loader.get_template(template_name)
        return template_to_render.render(Context(RequestContext(request, {"result" : result.object }), autoescape=context.autoescape))
    except template.TemplateDoesNotExist:
        return result.object

@register.inclusion_tag('search/components/activefacettags.html', takes_context=True)
def render_active_facet_tags(context):
    return context

@register.inclusion_tag('search/components/pagination.html', takes_context=True)
def pagination(context):
    return context

@register.simple_tag(takes_context=True)
def render_facets(context, variation="default"):

    try:
        facets = context["facets"]
    except ValueError:
        raise Exception ("We need a SearchResult object in context")

    template_name = "search/components/facetlist.%s.html" % variation
    request = context['request']
    
    template_to_render = template.loader.get_template(template_name)
    return template_to_render.render(Context(RequestContext(request, context), autoescape=context.autoescape))

@register.assignment_tag(takes_context=True)
def get_facet_url(context):

    try:
        facet_key = context["facet_key"]
    except ValueError:
        raise Exception("variable facet_key (e.g.: category) needs to be in context")

    try:
        facet_value = context["facet_value"]
    except ValueError:
        raise Exception("variable facet_value (e.g.: cars) needs to be in context")

    try:
        facet_count = context["facet_count"]
    except ValueError:
        raise Exception("variable facet_count (e.g.: 10) needs to be in context")

    request = context.get("request")
    path = request.get_full_path()

    this_facet = "%s_exact:%s" % ( facet_key, facet_value ) # e.g.: tag_exact:mytag
    this_facet_qs_key_value = "selected_facets=%s" % (this_facet)

    result = {
        "active" : False
    }

    # find the url this facet should link to:
    try:
        # get the current situation:
        url, qs = path.split("?")        
        qs_fragments = qs.split("&")

        for fragment in qs_fragments:

            this_facet_is_active = this_facet_qs_key_value == fragment
            
            if this_facet_is_active: # remove from qs. 
                qs_fragments.remove( this_facet_qs_key_value )
                result["active"] = this_facet_is_active
            
        if not result["active"]:
            qs_fragments.append(this_facet_qs_key_value)


        # put it back together
        result["url"] = "%s?%s" % ( url, ("&").join(qs_fragments) )

    except ValueError:
        result["url"] =  "%s?%s" % ( path, this_facet_qs_key_value )
    

    return result

    
    
    

