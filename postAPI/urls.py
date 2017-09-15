from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from postAPI import views

router = DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^dates/$', views.PostDateList.as_view()),
]

