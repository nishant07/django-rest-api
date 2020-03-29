from django.conf.urls import url
from assignment1.views import CardCollection, CardItem

urlpatterns = [
    url(r'cards/$', CardCollection.as_view()),
    url(r'cards/(?P<pk>[0-9]+)$', CardItem.as_view()),
]