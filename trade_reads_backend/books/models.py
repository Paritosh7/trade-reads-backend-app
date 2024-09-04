import uuid
from django.conf import settings
from django.db import models
from useraccount.models import User

#   owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
#    title = models.CharField(max_length=200)
#    author = models.CharField(max_length=200, blank=True)
#    description = models.TextField(blank=True)
#    average_rating = models.FloatField(blank=True, default=0.0) 
#    language = models.CharField(blank=True, max_length=20)
#    pages = models.PositiveIntegerField(blank=True, null=True)
#    publisher = models.CharField(blank = True, max_length=50)
#    published_date = models.DateField(blank=True, null=True)
#    cover_image_url = models.URLField(blank=True, null=True)
#    status = models.CharField(blank=True, max_length=20, choices=[('available', 'Available'), 
#                                                      ('pending', 'Pending'), 
#                                                      ('exchanged', 'Exchanged')], default='available')
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)

# Create your models here.
class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.CharField(max_length=200, blank=True)
    language = models.CharField(blank=True, max_length=20)
    pages = models.PositiveIntegerField(blank=True, null=True)
    publisher = models.CharField(blank = True, max_length=50)
    published_date = models.DateField(blank=True, null=True)
    interested = models.ManyToManyField(User, related_name="wishlist", blank=True)
    image = models.ImageField(upload_to='uploads/books')
    owner = models.ForeignKey(User, related_name='books', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def image_url(self):
        return f'{settings.WEBSITE_URL}{self.image.url}'
    