import json


# @router.get("/categories/{category_id}")
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
    products = Product.objects.select_related('image').order_by('-product.product_id')
    for row in products:
        data = [
            {
                'product_id': field.product_id,
                'image': field.image,
                'title': field.title,
                'price': field.price
             }
            for field in row.products.all()
        ]
        
    return json.dumps(data)
    