from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView, search_view_factory

from demo.models import Repo, Author

url_configs = [
    {
        "url_fragment" : "repos",
        "facets" : ["author", "tag"],
        "obj" : Repo
    },
    {
        "url_fragment" : "authors",
        "facets" : [],
        "obj" : Author
    }    
]

urlpatterns = patterns('',
# haystack search:
    
    # /search/<model>/ => include 
    url(r'^$', FacetedSearchView(
                        form_class=FacetedSearchForm, 
                        searchqueryset=SearchQuerySet().all().facet("author").facet("tag")),             
            name='haystack_faceted_search'),

    url(r'^autocomplete/$', 'haystackui.views.autocomplete', name='haystack_autocomplete_search'),
)

for url_config in url_configs:

    url_fragment = url_config.get("url_fragment")
    sqs = SearchQuerySet().all().models(url_config.get("obj"))

    for facet in url_config.get("facets",[]):
        sqs = sqs.facet(facet)

    urlpatterns += patterns('',
                    url( r'^%s/$' % url_fragment, FacetedSearchView(
                            form_class=FacetedSearchForm, 
                            searchqueryset=sqs),             
                        name='haystack_%s_faceted_search' % url_fragment) 
    )
    
