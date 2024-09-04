from django.shortcuts import render
from product.models import *

# Create your views here.

def home(request):
  products = Product.objects.all()[0:8]
  return render(request, 'base/home.html', {'products': products})


def about(request):
  return render(request, 'base/about.html')


def shop(request):
  products = Product.objects.all()
  return render(request, 'base/shop.html', {'products': products})


