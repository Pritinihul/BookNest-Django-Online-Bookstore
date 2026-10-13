from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    
    

]
