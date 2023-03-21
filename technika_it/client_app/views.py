from django.shortcuts import render
import requests
# from .backend.get_new_products_list import get_categories_products_list


def index(request): 
    # a = get_categories_products_list('http://127.0.0.1:8000/products', 1)
    # print(a)
    return render(request, 'index.html') #, {'new_products': new_products_json})


def get_categories_products_list(url: str, category_id: int):
    """
    Получение списка новинок
    Возвращает файл json
    Запрос sql:
        SELECT products.title, image.url,  products.price  FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        Where categories_products.category_id={category_id};
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        if category_id == row['main_category']:
            data.append(row)
    return data
