from haystack.forms import ModelSearchForm, FacetedSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, FacetedSearchView, search_view_factory

urlpatterns = patterns('',
# haystack search:
    
    # /search/<model>/ => include 
    url(r'^repo/$', FacetedSearchView(
                        form_class=FacetedSearchForm, 
                        template='search/product-search.html', 
                        searchqueryset=SearchQuerySet().all().models(Repo).facet()), 
    name='haystack_product_search'),

   
    (r'^', include('haystack.urls')),
)