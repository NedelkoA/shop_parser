from .models import ItemModel
from parser_django.celery import app
import json


@app.task
def added_item(item):
    item = json.loads(item)
    ItemModel.objects.get_or_create(
        name=item['name'],
        brand=item['brand'],
        price=''.join(item['price']),
        description=''.join(item['description']),
        size=', '.join(item['size']),
        currency=''.join(item['currency']),
        image=',\n'.join(item['image'])
    )
