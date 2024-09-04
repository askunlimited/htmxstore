from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def allProductView(request):
  products = Product.objects.all()
  return redirect()
