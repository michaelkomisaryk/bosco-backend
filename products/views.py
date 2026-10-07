import random

from django.contrib import messages
from django.shortcuts import redirect, render

from .models import Product

names = [
    "Фільтр масла",
    "Гальмівні колодки",
    "Свічки запалювання",
    "Амортизатор",
    "Повітряний фільтр",
    "Ремень ГРМ",
    "Радіатор охолодження",
    "Генератор",
    "Стартер",
    "Підшипник маточини",
    "Паливний насос",
    "Термостат",
    "Диск зчеплення",
    "Салонний фільтр",
]

brands = [
    "Toyota",
    "Volkswagen",
    "BMW",
    "Mercedes-Benz",
    "Ford",
    "Hyundai",
    "Renault",
    "Skoda",
    "Nissan",
    "Mazda",
]

countries = [
    "Японія",
    "Німеччина",
    "Південна Корея",
    "США",
    "Франція",
    "Чехія",
    "Польща",
    "Китай",
]


def products_list(request):
    products = Product.objects.all()
    return render(request, 'products/products.html', {'products': products})


def add_product(request):
    if request.method == 'POST':
        Product.objects.create(
            name=request.POST.get('name'),
            vehicle_brand=request.POST.get('vehicle_brand'),
            part_number=request.POST.get('part_number'),
            origin_country=request.POST.get('origin_country'),
            price=request.POST.get('price'),
        )
        messages.success(request, 'Товар успішно додано')
        return redirect('products_list')
    return render(request, 'products/add_product.html')


def replenish(request, count):
    for i in range(count):
        Product.objects.create(
            name=random.choice(names),
            vehicle_brand=random.choice(brands),
            part_number=str(random.randint(100000, 999999)),
            origin_country=random.choice(countries),
            price=random.randint(200, 8000),
        )
    messages.success(request, f'Додано {count} нових записів')
    return redirect('products_list')
