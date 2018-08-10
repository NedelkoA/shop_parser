from django.conf.urls import url
from .views import ItemsView, StartSpiderView


urlpatterns = [
    url(r'index/$', ItemsView.as_view(), name='item_list'),
    url(r'start/$', StartSpiderView.as_view()),
]
