from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.tweets_list, name='tweets_list'),
    url(r'^tweets_list/tweets_print/$',views.tweets_print, name='tweets_print'),
]
