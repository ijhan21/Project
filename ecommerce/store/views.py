from django.shortcuts import render
from .models import *

# Create your views here.
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)
    
def cart(request):
    if request.user.is_authenticated:
        print("request###################",request.user)
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        #Create empty cart for now for non-logged in user
        print("request###################",request.user)
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
    context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context={}
    return render(request, 'store/checkout.html', context)
