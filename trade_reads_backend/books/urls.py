from django.urls import path

from . import api

urlpatterns =  [
    path('', api.book_list, name = 'api_book_list'), 
    path('create/', api.create_book, name='api_create_book')
]