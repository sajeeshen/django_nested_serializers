from django.contrib import admin
from core.models import Publisher
from core.models import Book
from core.models import Author
# Register your models here.

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Author)
