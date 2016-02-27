from django.contrib import admin

# Register your models here.
from .models import Post# .z bieżącego katalogu z pliku models.py

admin.site.register(Post)# generacja panelu administracyjnego
