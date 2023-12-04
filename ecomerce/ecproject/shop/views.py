from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import category ,Product


# Create your views here.


def allprodcat(request,c_slug=None):

    c_page=None
    products=None
    if c_slug!=None:
        c_page=get_object_or_404(category,slug=c_slug)
        products=Product.objects.all().filter(category=c_page,available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request,"category.html",{'category': c_page,'products': products})

def prodetail(request,c_slug,product_sulg):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=product_sulg)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})