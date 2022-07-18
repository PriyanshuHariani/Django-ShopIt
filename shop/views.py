from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

# Create your views here.
def index(request):
    params = {}
    products = Product.objects.all()
    params['products'] = products
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("<h1> Shop contact us</h1>")

def tracker(request):
    return HttpResponse("<h1> Shop tracker us</h1>")

def search(request):
    return HttpResponse("<h1> Shop search us</h1>")

def prodView(request):
    return HttpResponse("<h1> Shop product view</h1>")

def checkout(request):
    return HttpResponse("<h1> Shop checkout</h1>")