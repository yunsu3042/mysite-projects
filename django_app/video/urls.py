from django.conf.urls import url
from video import views

urlpatterns = [
    url(r'^bookmark_list/$', views.bookmark_list, name='bookmark_list'),
    url(r'^bookmark_add/$', views.bookmark_add, name='bookmark_add'),
    url(r'^search/$', views.search, name='search'),
    url(r'^bookmark(?P<pk>\d+)/$', views.bookmark_detail,name="bookmark_detail")
]
