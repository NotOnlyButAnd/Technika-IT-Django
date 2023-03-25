import json


# @router.get("/new_products/{limit}")
def get_new_products_list(url: str = None, limit: int = 5):
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
    products = Product.objects.select_related('image').order_by('-product.product_id')[:limit]
    for row in products:
        data = [
            {
                'product_id': field.product_id,
                'image': field.image,
                'name': field.name,
                'price': field.price
             }
            for field in row.products.all()
        ]

    return json.dumps(data)
