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


def get_new_products_list(url: str, limit: int = 5):
    """
    Получение списка новинок
    Возвращает файл json
    Запрос sql:
        SELECT products.product_id, images.url, products.name, products.price, products.number_of_available
        FROM products
        INNER JOIN images ON images.image_id = products.main_image_id
        ORDER BY products.product_id DESC
        LIMIT {limit};
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        data.append(row)

    return data


def get_manufacters_categories(url: str = None, category_id: int):
    """
    Получение всех производителей заданной категории
    Возвращает файл json
    Запрос sql:
        SELECT DISTINCT manufacturers.manufacturer_id , manufacturers.title
        FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        INNER JOIN manufacturers ON manufacturers.manufacturer_id = products.manufacturer_id
        Where categories_products.category_id={category_id};
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        data.append(row)

    return data


def get_categories_min_max(url: str = None, category_id: int):
    """
    олучение максимальной и минимальной цены в заданной категории
    Возвращает файл json
    Запрос sql:
        SELECT max(products.price), min(products.price)
        FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        Where categories_products.category_id={category_id};
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        data.append(row)

    return data


def get_all_categories(url: str):
    """
    Получение списка всех категорий
    Возвращает файл json
    Запрос sql:
        SELECT category_id, title FROM categories;
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        data.append(row)

    return data