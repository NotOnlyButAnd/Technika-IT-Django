from . import models
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('image_id', 'url', 'alt')


class ManufactureSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Manufacture
        fields = ('manufacture_id', 'title')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = ('category_id', 'title',)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ('product_id', 'main_image', 'main_category', 'manufacturer',
            'title', 'description', 'price', 'number_of_available')


class ImageProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image_product
        fields = ('image', 'product',)


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category_product
        fields = ('category', 'product',)
