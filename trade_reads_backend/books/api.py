from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Book
from .serializers import BookSerializer

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    
    return JsonResponse({
        'data': serializer.data
    })
