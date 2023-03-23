from django.shortcuts import render
import requests
# from .backend.get_new_products_list import get_categories_products_list

products_url = 'http://127.0.0.1:8000/products'
images_url = 'http://127.0.0.1:8000/images'
category_url = 'http://127.0.0.1:8000/category'


def index(request): 
    new_products = get_new_products_list()
    print(new_products)
    return render(request, 'index.html', {'new_products': new_products})


def get_categories_products_list(url: str, category_id: int):
    """
    Получение списка товаров заданной категории
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



def get_all_categories(url: str):
    """
    Получение списка всех категорий
    Возвращает файл json
    Запрос sql:
        select category_id, title, image FROM categories;
    """
    data = []
    products = requests.get(url).json()
    for row in products:
        data.append(row)
    return data


def get_new_products_list(limit: int = 5):
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
    products = requests.get(products_url).json()
    categories = requests.get(category_url).json()
    images = requests.get(images_url).json()

    for i in range(limit):
        for j in images:
            if j['image_id'] == products[i]['main_image']:
                products[i]['main_image'] = j['url']

        for j in categories:
            if j['category_id'] == products[i]['main_category']:
                products[i]['main_category'] = j['title']
        data.append(products[i])

    return data


def get_manufacters_categories(url: str = None, url_2: str = None, category_id: int = 1):
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
    manufacturers = requests.get(url_2).json()
    for row in products:
        if category_id == row['manufacturer']:
            data.append({'manufacturer_id': row.get('manufacturer')})
    for row in data:
        for manufacture in manufacturers:
            if row.get('manufacturer_id') == manufacture.get('manufacture_id'):
                row['title'] = manufacture.get('title')
    return data


def get_categories_min_max(url: str = None, category_id: int = 1):
    """
    Получение максимальной и минимальной цены в заданной категории
    Возвращает файл json
    Запрос sql:
        SELECT max(products.price), min(products.price)
        FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        Where categories_products.category_id={category_id};
    """
    data = []
    products = requests.get(url).json()
    min_price = int(products[0].get('price'))
    max_price = min_price
    for row in products:
        if row.get("main_category") == category_id:
            if min_price > row.get('price'):
                min_price = row.get('price')
            if max_price < row.get('price'):
                max_price = row.get('price')
    data.append({'min': min_price, 'max': max_price})
    return data
