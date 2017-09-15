from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as rest_framework_views
from postAPI import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^dates/$', views.PostDateList.as_view()),
    url(r'^get_auth_token/$', rest_framework_views.obtain_auth_token, name='get_auth_token'),
]

