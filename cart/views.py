from django.shortcuts import get_object_or_404, redirect,render
from django.contrib.auth.decorators import login_required
# Create your views here.
from books.models import Book
from .models import Cart,CartItem,Address,Order,OrderItem
from .forms import AddressForm

@login_required
def add_to_cart(request,book_id):
    book= get_object_or_404(Book, id=book_id)

    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        book=book
    )
    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('book_detail', book_id=book.id)

@login_required
def cart_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)

    cart_items = cart.items.select_related('book')

    subtotal = sum(
        item.book.price * item.quantity
        for item in cart_items
    )
    total = subtotal

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'subtotal': subtotal,
        'total': total,
    })

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.delete()

    return redirect('cart')

def increase_quantity(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    cart_item.quantity += 1
    cart_item.save()

    return redirect('cart')

def decrease_quantity(request, item_id):
    cart_item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if cart_item.quantity > 1:
     cart_item.quantity -= 1
     cart_item.save()
    else:
        cart_item.delete()

    return redirect('cart')

@login_required
def checkout_view(request):
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.select_related('book')
                
    subtotal = sum(
                    item.book.price * item.quantity
                    for item in cart_items
                    )
    total = subtotal

    addresses = Address.objects.filter(user=request.user)


    if request.method=='POST':
        if 'save_address' in request.POST:
         form = AddressForm(request.POST)

         if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.save()
            return redirect('checkout')
        elif 'place_order' in request.POST:
            address_id = request.POST.get('address_id')

            address = get_object_or_404(
                Address,
                id=address_id,
                user=request.user
            )
            for item in cart_items:
             if item.quantity > item.book.stock:
              return render(request, 'cart/checkout.html', {
                'cart_items': cart_items,
                'subtotal': subtotal,
                'total': total,
                'form': AddressForm(),
                'addresses': addresses,
                'error': f"Only {item.book.stock} copies of '{item.book.title}' are available."
            })


            order = Order.objects.create(
                user=request.user,
                address=address,
                total_amount=total
            )

            for item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    book=item.book,
                    quantity=item.quantity,
                    price=item.book.price
                )
                 # Reduce stock
                item.book.stock -= item.quantity
                item.book.save()


            cart_items.delete()

            return redirect('order_confirmation', order_id=order.id)

    else:
     form= AddressForm
                
    return render(request, 'cart/checkout.html', {
                        'cart_items': cart_items,
                        'subtotal': subtotal,
                        'total': total,
                        'addresses': addresses,
                        'form': form,
                    })

@login_required
def order_confirmation(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(request, 'cart/order_confirmation.html', {
        'order': order
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(request, 'cart/order_history.html', {
        'orders': orders
    })

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(
        Order.objects.prefetch_related('items__book'),
        id=order_id,
        user=request.user
    )

    return render(request, 'cart/order_detail.html', {
        'order': order
    })