from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from . import api


app_name = 'client_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('images', api.ImageListAPIView.as_view(), name='api_images'),
    path('manufacturers', api.ManufactureListAPIView.as_view(), name='api_manufacturers'),
    path('category', api.CategoryListAPIView.as_view(), name='api_categories'),
    path('products', api.ProductListAPIView.as_view(), name='api_products'),
    path('images_products', api.ImageProductListAPIView.as_view(), name='api_images_products'),
    path('category_products', api.CategoryProductListAPIView.as_view(), name='api_category_products'),
]