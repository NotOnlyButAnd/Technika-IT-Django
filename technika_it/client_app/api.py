from rest_framework.generics import ListAPIView
from . import serializers
from . import models


class ImageListAPIView(ListAPIView):
    serializer_class = serializers.ImageSerializer

    def get_queryset(self):
        return models.Image.objects.all()


class ManufactureListAPIView(ListAPIView):
    serializer_class = serializers.ManufactureSerializer

    def get_queryset(self):
        return models.Manufacture.objects.all()


class CategoryListAPIView(ListAPIView):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        return models.Category.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = serializers.ProductSerializer

    def get_queryset(self):
        return models.Product.objects.all()


class ImageProductListAPIView(ListAPIView):
    serializer_class = serializers.ImageProductSerializer

    def get_queryset(self):
        return models.Image_product.objects.all()


class CategoryProductListAPIView(ListAPIView):
    serializer_class = serializers.CategoryProductSerializer

    def get_queryset(self):
        return models.Category_product.objects.all()