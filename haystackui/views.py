from django.http import HttpResponse
from haystack.query import SearchQuerySet
from haystack.views import FacetedSearchView
from django.db.models.loading import get_model

import json
import importlib
from django.views.generic.base import TemplateView

class BrowseFilterSearchView(FacetedSearchView):
    """
    parameters:

    model. Will limit search results to specified model. If not supplied no limit is applied
    facets. Specifies which facets results should be faceted on 
    """

    def __init__(self, *args, **kwargs):

        self.model = kwargs.pop("model", False)        
        self.facets = kwargs.pop("facets",[])

        self.filter = kwargs.pop("filter", False)        
        self.filter_value = kwargs.pop("filter_value",False)

        super(BrowseFilterSearchView, self).__init__(*args, **kwargs)
        

    def build_form(self, form_kwargs=None):
        
        if form_kwargs is None:
            form_kwargs = {}

        form_kwargs['model'] = self.model
        form_kwargs['available_facets'] = self.facets

        if self.filter:
            form_kwargs['filter'] = self.filter

        if self.filter_value:
            form_kwargs['filter_value'] = self.filter_value

        return super(BrowseFilterSearchView, self).build_form(form_kwargs)
        
    def __call__(self, *args, **kwargs):
        
        model_string = kwargs.pop("model", False)        
        app,model = model_string.split(".")
        self.model = get_model(app,model)
        self.filter = kwargs.pop("filter", False)        
        self.filter_value = kwargs.pop("filter_value",False)

        return super(BrowseFilterSearchView, self).__call__(*args, **kwargs)


def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(name_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.object.name for result in sqs]
    
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')



