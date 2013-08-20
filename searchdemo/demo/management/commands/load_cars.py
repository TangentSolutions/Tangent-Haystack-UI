from django.core.management.base import BaseCommand
import requests
import json
from demo.models import *
import random

class Command(BaseCommand):
    
    def handle(self, *args, **options):
        
        url = "http://www.carqueryapi.com/api/0.3/?cmd=getTrims"
        response = requests.get(url)
        cars = json.loads(response.content).get("Trims")

        for car in cars:

            data = {
                "model_id": car.get("model_id",None),
                "make": car.get("make_display",None),
                "trim": car.get("model_trim",None),
                "name": car.get("model_name",None),
                "body": car.get("model_body",None),
                "year": car.get("model_year",None),
                "seats": car.get("model_seats",None),
                "doors": car.get("model_doors",None),
            }

            obj = Car.objects.create(**data)

            print "Added: %s" % obj.name