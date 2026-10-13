from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('add/<int:book_id>/',views.add_to_cart,name='add_to_cart'),
    path('',views.cart_view,name='cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('checkout/',views.checkout_view,name='checkout'),
    path('order-confirmation/<int:order_id>/',views.order_confirmation,
    name='order_confirmation'),
    path('orders/',views.order_history,name='order_history'),
    path(
    'orders/<int:order_id>/',
    views.order_detail,
    name='order_detail'
),

] 