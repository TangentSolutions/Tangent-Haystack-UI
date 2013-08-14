Tangent-Haystack-UI
===================



Is a thin wrapper around [HayStack](http://django-haystack.readthedocs.org/). Basically it just provides a concrete implementation of the various uses outlined in the docs. 

## Features:

- [ ] Full-text search with autocomplete
- [x] Search grouped by model
- [x] Browse by category with filter/narrow by many facets
- [x] A bunch of templatetags 


## Installation: 

	pip install -e git+ssh://git@github.com/TangentSolutions/Tangent-Haystack-UI.git#egg=haystackui


## Configuration: 

Basically we're going to go through [getting started](https://django-haystack.readthedocs.org/en/v2.1.0/tutorial.html) from the haystack docs with some small caveats.

#### Setup your backend:



#### Create Indexes:



#### Add to `INSTALLED_APPS`

    ..
	'haystack',
    'haystackui',
    ..

#### Create your indexes 

Create a file in:

	import datetime
	from haystack import indexes
	from myapp.models import Note

	class NoteIndex(indexes.SearchIndex, indexes.Indexable):
		text = indexes.CharField(document=True, use_template=True)
		author = indexes.CharField(model_attr='user')
		pub_date = indexes.DateTimeField(model_attr='pub_date')

		def get_model(self):
			return Note


##### Some notes:

Some additional behaviour you might be interested in:

###### Add a m2m field:
	

To do this you use the `MultiValueField`. In your index class:

	#add field:
	...
	tag = indexes.MultiValueField(faceted=True)

	...

	# prepare data:
    def prepare_tag(self, obj):
        return [(tag.name) for tag in obj.tags.all()]


###### Add an ngram field for autocomplete:
	
	from haystack import indexes
	..
	name_auto = indexes.EdgeNgramField(model_attr='name')

	
#### Add index data templates at `search/indexes/myapp/<model>_text.txt`

	{{object.name}}
	{{object.description}}
	{{object.author.name}}

#### Build your index:

	python manage.py rebuild_index

#### Include search in your urls: 

    ..

## Customization


