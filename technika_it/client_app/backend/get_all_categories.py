import json


# @router.get("/new_products/{limit}")
def get_all_categories(url: str = None):
    """
    Получение списка всех категорий

    Возвращает файл json

    Запрос sql:
        SELECT category_id, title FROM categories;
    """
    data = []
    products = Products.objects.select_related('images').order_by('-products.product_id')
    for row in products:
        data = [
            {
                'category_id': field.category_id,
                'title': field.title
             }
            for field in row.products.all()
        ]

    return json.dumps(data)
