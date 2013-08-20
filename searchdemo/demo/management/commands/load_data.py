from django.core.management.base import BaseCommand
import requests
import json
from demo.models import *
import random

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        headers = {"Accept":"application/vnd.github.preview"}
        url = "https://api.github.com/search/repositories?q=python"
        response=requests.get(url,headers=headers)
        taglist = ["python", "ruby", "django", "php", "ui", "rails", "testing", "TDD", "Agile"] # some random tags

        repos = json.loads(response.content).get("items")        
        # delete:
        for del_repo in Repo.objects.all(): del_repo.delete()
        
        for repo in repos:

            author = Author.objects.create(name=repo.get("owner").get("login"))
            repo = Repo.objects.create(name=repo.get("name"), description=repo.get("description"), author=author)

            for random_tag in taglist:
                if random.choice([True,False]):
                    tag, created = Tag.objects.get_or_create(name=random_tag)
                    repo.tags.add(tag)
