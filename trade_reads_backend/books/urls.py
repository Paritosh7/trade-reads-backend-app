from django.urls import path

from . import api

urlpatterns =  [
    path('', api.book_list, name = 'api_book_list'), 
]