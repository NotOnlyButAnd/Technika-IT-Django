from django.shortcuts import render
# from .backend.get_new_products_list import *

def index(request): 
    # new_products_json = get_new_products_list()
    return render(request, 'index.html') #, {'new_products': new_products_json})
