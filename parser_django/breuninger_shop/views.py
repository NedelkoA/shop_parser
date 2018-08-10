from django.shortcuts import render, redirect
from django.conf import settings
from django.views.generic import ListView, TemplateView
from .models import ItemModel
import redis

redis_server = redis.Redis(settings.REDIS_HOST, settings.REDIS_PORT)


class ItemsView(ListView):
    model = ItemModel
    template_name = 'breuninger_shop/index.html'


class StartSpiderView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'breuninger_shop/start.html', {})

    def post(self, request):
        if request.method == 'POST':
            redis_server.lpush('breuninger:start_urls', 'https://www.breuninger.com/damen/schuhe')
            return redirect('item_list')
