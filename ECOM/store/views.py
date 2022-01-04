from django.shortcuts import render

from .models import *


# Create your views here.

def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']
    product = Product.objects.all()
    context = {
        'products': product,
        'cartItems': cartItems,
    }

    return render(request, 'store/store.html', context)


def card(request):
    #order = Order.objects.all()
    print(request.user)
    if request.user.is_authenticated:
        customer = request.user.customer
        print(customer)
        order = Order.objects.filter(customer=customer, complete = False).first()
        print(order)
        items = order.orderitem_set.all()
        print(items)
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/card.html', context)


def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order = Order.objects.filter(customer=customer, complete=False).first()
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0,'get_cart_total':0}

    context = {
        'items': items,
        'order': order,
    }
    return render(request, 'store/checkout.html', context)
