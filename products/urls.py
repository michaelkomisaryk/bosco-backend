from django.urls import path

from . import views

urlpatterns = [
    path('products', views.products_list, name='products_list'),
    path('products/add', views.add_product, name='add_product'),
    path('replenish/<int:count>', views.replenish, name='replenish'),
]
