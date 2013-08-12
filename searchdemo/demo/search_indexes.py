import datetime
from haystack import indexes
from demo.models import * 


class RepoIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)
    tag = indexes.MultiValueField(faceted=True) # m2m field
    author = indexes.CharField(model_attr='author__name', faceted=True) # fk field
    #meta = indexes.CharField(model_attr='productmeta__value', faceted=True, null=True)
    #date_created = indexes.DateTimeField(model_attr='created')
    
    name_auto = indexes.EdgeNgramField(model_attr='name') # for autocomplete

    def get_model(self):
        return Repo

    def prepare_tag(self, obj):
        return [(tag.name) for tag in obj.tags.all()]

class AuthorIndex(indexes.SearchIndex, indexes.Indexable):

    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return Author