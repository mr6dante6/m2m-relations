from django.urls import path
from django.contrib import admin
from articles.views import articles_list


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', articles_list, name='articles'),
]
