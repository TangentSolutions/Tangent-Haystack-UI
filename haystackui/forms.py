from haystack.forms import ModelSearchForm, FacetedSearchForm

class BrowseFilterSearchForm(FacetedSearchForm):
    
    def __init__(self, *args, **kwargs):
        self.available_facets = kwargs.pop("available_facets", [])
        self.model = kwargs.pop("model", False)

        self.filter = kwargs.pop("filter", False)        
        self.filter_value = kwargs.pop("filter_value",False)

        super(BrowseFilterSearchForm, self).__init__(*args, **kwargs)

    def search(self):

        sqs = super(BrowseFilterSearchForm, self).search()

        # limit to selected model
        if self.model:
            sqs = sqs.models(self.model)

            # add facets for model
            import importlib
            app = self.model._meta.app_label
            mod = importlib.import_module(app)
            indexes = mod.search_indexes
            index = getattr(indexes, "%sIndex" % self.model._meta.object_name )

            for label, field in index.fields.items():
                if field.faceted:
                    sqs = sqs.facet(label)

        # provide facets
        for facet in self.available_facets:
            sqs = sqs.facet(facet)



        if self.filter and self.filter_value: 
            sqs = sqs.narrow("%s_exact:%s" % (self.filter, self.filter_value) )
        
        return sqs

    def no_query_found(self):
        return self.searchqueryset.all()