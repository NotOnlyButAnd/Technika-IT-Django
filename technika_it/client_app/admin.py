from django.contrib import admin
from .models import *

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    model = Image


@admin.register(Manufacture)
class ManufactureAdmin(admin.ModelAdmin):
    model = Manufacture
    #Отображение списка изменений
    list_display = (
        "manufacture_id",
        "title"
    )
    #Встроенный виджет для фильтрации
    list_filter = (
        "title"
    )
    #Строка поиска
    search_fields = (
        "title"
    )

    save_on_top = True


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    model = Categories
    #Отображение списка изменений
    list_display = (
        "category_id",
        "title"
    )
    #Встроенный виджет для фильтрации
    list_filter = (
        "category_id"
    )
    #Строка поиска
    search_fields = (
        "title"
    )

    save_on_top = True

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    model = Products
    #Отображение списка изменений
    list_display = (
        "product_id",
        "title",
        "price",
        "number_of_available",
        "description" #Стоит ли?
    )
    #Встроенный виджет для фильтрации
    list_filter = (
        "product_id",
        "number_of_available",
        "price"
    )
    #Строка поиска
    search_fields = (
        "title"
    )

    save_on_top = True


@admin.register(Images_products)
class ImagesProductsAdmin(admin.ModelAdmin):
    model = Images_products
    #Отображение списка изменений
    list_display = (
        "image_id",
        "product_id"
    )
    #Встроенный виджет для фильтрации
    list_filter = (
        "product_id"
    )

    save_on_top = True


@admin.register(Categories_products)
class CategoriesProductsAdmin(admin.ModelAdmin):
    model = Categories_products
    # Отображение списка изменений
    list_display = (
        "category_id",
        "product_id"
    )
    # Встроенный виджет для фильтрации
    list_filter = (
        "product_id",
        "category_id"
    )

    save_on_top = True
