from django.shortcuts import render,get_object_or_404
from .models import Book,Category
from rest_framework import viewsets,filters,permissions
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from .permissions import IsStaffOrAdminForWrite

# Create your views here.
def home(request):
    books = Book.objects.filter(is_available=True)[:8]
    categories = Category.objects.all()
    category_sections = []

    for category in categories[:2]:
        category_books = Book.objects.filter(
            category=category,
            is_available=True
        )[:5]

        if category_books.exists():
            category_sections.append({
                'category': category,
                'books': category_books
            })

    return render(
        request,
        "books/home.html",
        {
            'books': books,
            'categories': categories,
            'category_sections': category_sections
        }
    )


    

def book_list(request):
    search = request.GET.get('search')
    category = request.GET.get('category')
    books = Book.objects.filter(is_available=True)
    categories = Category.objects.all()
    if search:
        books= books.filter(
             Q(title__icontains=search) |
        Q(author__icontains=search) |
        Q(publisher__icontains=search)
        )

    if category:
            books= books.filter(category_id=category)

    return render(request, 'books/book_list.html', {
        'books': books,
        'search':search, 
        'categories':categories})

def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'books/book_detail.html', {'book': book})

class BookViewSet(viewsets.ModelViewSet):
    queryset= Book.objects.all()
    serializer_class = BookSerializer
    #  for api authentication
    permission_classes = [IsStaffOrAdminForWrite] 
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
        ]
    search_fields = ['title', 'author', 'publisher']
    filterset_fields = ['category']