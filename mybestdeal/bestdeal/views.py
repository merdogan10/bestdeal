from django.http import Http404
from django.shortcuts import render, redirect
from .models import Product, Sub_Category, Category

def index(request):
    all_products = Product.objects.all().order_by('-id')
    return render(request, 'index.html', {"all_products": all_products, 'categories': Category.objects.all(),'number_of_deals':Product.objects.count()})

def search_view(request):
    search_query = request.GET['q']
    if search_query == "":
        return redirect(index)
    all_products = Product.objects.filter(name__contains=search_query).order_by('-id')
    return render(request, 'index.html', {"all_products": all_products, 'categories': Category.objects.all(),'search_query':search_query})

def detail(request, slug, category_name, sub_category_name):
    all_products = Product.objects.all().order_by('-id')
    category_products = Product.objects.filter(sub_category__category__category_name=category_name,
                                               sub_category__sub_category_name=sub_category_name).order_by('-id')
    try:
        product = Product.objects.get(slug=slug)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'detail.html', {"product": product,"category_products": category_products,"all_products": all_products, "category": category_name, "sub_category": sub_category_name})

def category_items(request, category_name):
    all_products = Product.objects.all().order_by('-id')
    category_products = Product.objects.filter(sub_category__category__category_name=category_name).order_by('-id')
    if category_products:
        return render(request, 'index.html', {"category_products": category_products,"all_products": all_products, "category": category_name, 'sub_categories': Sub_Category.objects.all().order_by('sub_category_name')})
    return redirect(index)

def category_sub_category_items(request, category_name, sub_category_name):
    all_products = Product.objects.all().order_by('-id')
    category_products = Product.objects.filter(sub_category__category__category_name=category_name,sub_category__sub_category_name=sub_category_name)
    if category_products:
        return render(request, 'index.html', {"category_products": category_products,"all_products": all_products, "category": category_name, "sub_category": sub_category_name, 'sub_categories': Sub_Category.objects.all().order_by('sub_category_name')})
    return redirect(index)

def privacy_view(request):
    return render(request, 'privacy.html')

def terms_view(request):
    return render(request, 'terms.html')

def contact_view(request):
    return render(request, 'contact.html')