from django.shortcuts import render, get_object_or_404
from django.urls import is_valid_path
from .models import Product
from category.models import Category 
# Create your views here.


def index(request):
    products = Product.objects.filter(is_available= True)
    context ={
        "products" : products,
    }
    # return render(request,'index.html')#, context)
    return render(request,'index.html', context)


def store(request,category_slug=None):

	# Define categories and products are None
	categories = None
	products   = None

	# What if categories slug are NOT None or exist
	# Return the slugs if they  exist, or
	# return 404 error if they do not exist
	if category_slug != None:
		categories = get_object_or_404(Category, slug=category_slug)
		products   = Product.objects.filter(category=categories, is_available=True)

		# Product count
		product_count = products.count()

	else:

		# Get all the available products
		products = Product.objects.all().filter(is_available=True)

		# Counting the products
		product_count = products.count()

	# Put the available products into context dictionary
	context = {
		'products':products, # <-- 'products'  as variable
		'product_count':product_count,
	}	

	return render(request, 'store.html', context)



def detail_page(request,category_slug,product_slug):

	# Get the slug from Category model and slug from the Product model
	try: 
		single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
		
	except Exception as e: 
		raise e

	# Put the available products into context dictionary
	context = {
		'single_product':single_product, # <-- 'single_product'  as variable
	}	

	return render(request, 'detail-page.html', context)	