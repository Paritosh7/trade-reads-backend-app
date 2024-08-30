from django.urls import path

from . import api

urlpatterns =  [
    path('', api.book_list, name = 'api_book_list'), 
    path('create/', api.create_book, name='api_create_book'),
    path('<uuid:pk>', api.book_detail, name='api_book_detail') 
]