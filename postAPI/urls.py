from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.views import APIView
from .views import *

patterns = {
    url(r'^posts/', APIView)
}

urlpatterns = format_suffix_patterns(patterns)
