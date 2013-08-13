from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView, search_view_factory

from demo.models import Repo


urlpatterns = patterns('',
# haystack search:
    
    # /search/<model>/ => include 
    url(r'^$', FacetedSearchView(
                        form_class=FacetedSearchForm, 
                        searchqueryset=SearchQuerySet().all().models(Repo).facet("author").facet("tag")), 
            
            name='haystack_faceted_search'),
)