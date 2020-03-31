from django.conf.urls import url
from assignment4.views import CardCollection, CardItem, TaskCollection, TaskItem

urlpatterns = [
    url(r'cards/$', CardCollection.as_view(),name=CardCollection.name),
    url(r'cards/(?P<pk>[0-9]+)$', CardItem.as_view()),
    url(r'tasks/$', TaskCollection.as_view()),
    url(r'tasks/(?P<pk>[0-9]+)$', TaskItem.as_view()),
]