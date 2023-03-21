import json


# @router.get("/new_products/{limit}")
def get_manufacters_categories(url: str = None, category_id: int = None):
    """
    Получение всех производителей заданной категории

    Возвращает файл json

    Запрос sql:
        SELECT DISTINCT manufacturers.manufacturer_id , manufacturers.title  FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        INNER JOIN manufacturers ON manufacturers.manufacturer_id = products.manufacturer_id
        Where categories_products.category_id={category_id}

    """
    data = []
    products = Products.objects.select_related('images').order_by('-products.product_id')
    for row in products:
        data = [
            {
                'manufacturer_id': field.manufacturer_id,
                'title': field.title
             }
            for field in row.products.all()
        ]

    return json.dumps(data)
