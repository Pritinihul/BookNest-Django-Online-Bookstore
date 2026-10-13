from django.contrib import admin

# Register your models here.
from .models import Category, Book


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publisher',
        'price',
        'stock',
        'category',
        'is_available',
    )

    search_fields = (
        'title',
        'author',
        'publisher',
        'isbn',
    )

    list_filter = (
        'category',
        'is_available',
    )