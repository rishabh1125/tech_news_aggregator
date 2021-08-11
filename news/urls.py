from django.http.response import HttpResponse
from news.views import *
from django.urls import path
# from news.views import *


urlpatterns = [
  path('scrape/', scrape, name="scrape"),
  path('', news_list, name="home"),
]