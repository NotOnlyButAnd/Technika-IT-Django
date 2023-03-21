import json


# @router.get("/new_products/{limit}")
def get_categories_min_max(url: str = None, category_id: int = None):
    """
    Получение максимальной и минимальной цены в заданной категории

    Возвращает файл json

    Запрос sql:
        SELECT max(products.price), min(products.price)
        FROM products
        INNER JOIN categories_products ON categories_products.product_id = products.product_id
        Where categories_products.category_id={category_id}
    """
    data = []
    products = Products.objects.select_related('images').order_by('-products.product_id')
    for row in products:
        data = [
            {
                'max': field.max,
                'min': field.min
             }
            for field in row.products.all()
        ]

    return json.dumps(data)
