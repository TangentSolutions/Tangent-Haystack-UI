from haystack import indexes
from django.db import models

class Repo(models.Model):
    
    author = models.ForeignKey("Author")
    tags = models.ManyToManyField("Tag", blank=True, null=True)
    name = models.CharField(max_length=80,db_index=True)
    description = models.TextField()

    last_edited = models.DateTimeField(auto_now=True,db_index=True)        
    created = models.DateTimeField(auto_now_add=True,db_index=True)  

    def __unicode__(self):
        return self.name

class Author(models.Model):

    name = models.CharField(max_length=100,db_index=True)

    last_edited = models.DateTimeField(auto_now=True,db_index=True)        
    created = models.DateTimeField(auto_now_add=True,db_index=True)  

    def __unicode__(self):
        return self.name

class Tag(models.Model):

    name = models.CharField(max_length=100,db_index=True)

    last_edited = models.DateTimeField(auto_now=True,db_index=True)        
    created = models.DateTimeField(auto_now_add=True,db_index=True)  

    def __unicode__(self):
        return self.name
