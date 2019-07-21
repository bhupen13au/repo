from django.contrib import admin

# Register your models here.

from books.models import *

admin.site.register(Book)