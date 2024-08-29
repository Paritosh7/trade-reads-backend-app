from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes

from .models import Book
from .serializers import BookSerializer
from .forms import BookForm

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def book_list(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    
    return JsonResponse({
        'data': serializer.data
    })


@api_view(['POST', 'FILES'])
def create_book(request):
    form = BookForm(request.POST, request.FILES)

    if form.is_valid():
        book = form.save(commit=False)
        book.owner = request.user
        book. save()
        
        return JsonResponse({'success': True})
    
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors':form.errors.as_json()}, status = 400)