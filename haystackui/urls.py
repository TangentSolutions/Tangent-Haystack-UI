from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystackui.forms import BrowseFilterSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView, search_view_factory
from haystackui.views import BrowseFilterSearchView


urlpatterns = patterns('',
    # default haystack search:
    
    
    # e.g.: /catalog.product/category/watches/
    url(r'^(?P<model>[a-zA-Z0-9-.]+)/(?P<filter>[a-zA-Z0-9-]+)/(?P<filter_value>[a-zA-Z0-9-]+)/$', 
                BrowseFilterSearchView(form_class=BrowseFilterSearchForm), name='haystackui_model_browse_filter'),
    url(r'^(?P<model>[a-zA-Z0-9-.]+)/$', 
                BrowseFilterSearchView(form_class=BrowseFilterSearchForm), name='haystackui_model_browse_filter'),
    
    url(r'^$', FacetedSearchView(form_class=FacetedSearchForm), name='haystack_faceted_search'),

    #url(r'^templatetagexample/$', SimpleSearchView.as_view() , name='haystack_templatetagexample'),
    url(r'^autocomplete/$', 'haystackui.views.autocomplete', name='haystack_autocomplete_search'),
)
