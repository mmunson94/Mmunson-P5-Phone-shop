from django.shortcuts import render, get_object_or_404
from .cart import Cart
from website.models import Product
from django.http import JsonResponse


# Create your views here
def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants
    total_quantity = len(cart)
    return render(request, 'cart_summary.html',
         {'cart_products': cart_products, 'quantities': quantities, 'total_quantity': total_quantity})

def cart_add(request):
    print('inside the cart add function')
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        cart_quantity = cart.__len__()
        response = JsonResponse({'Product name': product.name, 'qty': cart_quantity })
        return response


def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        print('------ post content -------')
        print(request.POST)
        print('------ end post content ------')
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})

        return response

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product=product_id)

        response = JsonResponse({'product': product_id})
        return response