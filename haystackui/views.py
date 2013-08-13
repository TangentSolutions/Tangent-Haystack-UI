from django.http import HttpResponse
from haystack.query import SearchQuerySet
import json

def autocomplete(request):
    sqs = SearchQuerySet().autocomplete(name_auto=request.GET.get('q', ''))[:5]
    suggestions = [result.object.name for result in sqs]
    
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')