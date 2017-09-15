from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from postAPI import views

patterns = {
    url(r'^posts/$', views.PostList.as_view()),
    url(r'^dates/$', views.PostDateList.as_view()),
    url(r'^posts/(?P<pk>[0-9]+)/$', views.PostList.as_view()),
    url(r'^authors/$', views.AuthorList.as_view()),
    url(r'^authors/(?P<pk>[0-9]+)/$', views.AuthorDetail.as_view()),
}


urlpatterns = format_suffix_patterns(patterns)
