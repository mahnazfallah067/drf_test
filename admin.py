from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title']
    def get_tags(self, obj):
        return ",".join(o for o in obj.tags.title())


