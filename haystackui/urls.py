from django.conf.urls import patterns, include, url

from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystackui.forms import BrowseFilterSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView, search_view_factory
from haystackui.views import BrowseFilterSearchView


from demo.models import Repo, Author

url_configs = [
    {
        # maps to: /search/repos/<[author,tag]>/
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
    # default haystack search:
    url(r'^repos/$', BrowseFilterSearchView(form_class=BrowseFilterSearchForm, model=Repo, facets=["author", "tag"], results_per_page=3), name='haystack_browse_search'),
    url(r'^repos/(?P<filter>[a-zA-Z0-9-]+)/(?P<filter_value>[a-zA-Z0-9-]+)/$', BrowseFilterSearchView(form_class=BrowseFilterSearchForm, model=Repo, facets=["author", "tag"]), name='haystack_browse_search'),

    url(r'^$', FacetedSearchView(
                        form_class=FacetedSearchForm, 
                        searchqueryset=SearchQuerySet().all().facet("author").facet("tag")),             
            name='haystack_faceted_search'),

    url(r'^autocomplete/$', 'haystackui.views.autocomplete', name='haystack_autocomplete_search'),
)

"""
for url_config in url_configs:

    url_fragment = url_config.get("url_fragment")
    sqs = SearchQuerySet().all().models(url_config.get("obj"))

    for facet in url_config.get("facets",[]):
        sqs = sqs.facet(facet)

    urlpatterns += patterns('',
                    # /<model>/
                    url( r'^%s/$' % url_fragment, FacetedSearchView(
                            form_class=BrowseFilterSearchForm, 
                            searchqueryset=sqs),             
                        name='haystack_%s_faceted_search' % url_fragment)                     
    )
    
"""