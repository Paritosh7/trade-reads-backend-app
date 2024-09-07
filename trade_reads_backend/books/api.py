from django.http import JsonResponse

from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.tokens import AccessToken
from .models import Book
from .serializers import BookSerializer, BookDetailSerializer
from .forms import BookForm
from useraccount.models import User

@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def book_list(request):
    
    try:
        token = request.META['HTTP_AUTHORIZATION'].split('Bearer ')[1]
        token = AccessToken(token)
        print("token ", token)
        user_id = token.payload['user_id']
        
        user = User.objects.get(pk=user_id)
    except Exception as e:
        print(e)
        user = None
    
    
    books = Book.objects.all()
    
    owner_id = request.GET.get('owner_id', '')
    is_wishlist = request.GET.get('is_wishlist', '')
    
    if owner_id:
        books = books.filter(owner_id=owner_id)
        
    if is_wishlist:
        books = books.filter(interested__in=[user])
    
    wishlist = []
    
    if user:
        for book in books:
            if user in book.interested.all():
                wishlist.append(book.id)
                
        
    serializer = BookSerializer(books, many=True)
    
    return JsonResponse({
        'data': serializer.data,
        'wishlist' : wishlist
    })
    
@api_view(["GET"])
@authentication_classes([])
@permission_classes([])
def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    serializer = BookDetailSerializer(book, many=False)
    
    return JsonResponse(serializer.data)


@api_view(['POST', 'FILES'])
def create_book(request):
    form = BookForm(request.POST, request.FILES)

    if form.is_valid():
        book = form.save(commit=False)
        book.owner = request.user
        book.save()
        
        return JsonResponse({'success': True})
    
    else:
        print('error', form.errors, form.non_field_errors)
        return JsonResponse({'errors':form.errors.as_json()}, status = 400)
    
    
@api_view(['POST'])
def toggle_interest(request, pk):
    book = Book.objects.get(pk=pk)
    
    if request.user in book.interested.all():
        book.interested.remove(request.user)
        return JsonResponse({'is_interested' : False})
    
    else:
        book.interested.add(request.user)
        return JsonResponse({'is_interested': True})