import random

from django.http import HttpResponse
from django.shortcuts import render

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


def replenish(request, count):
    for i in range(count):
        Product.objects.create(
            name=random.choice(names),
            vehicle_brand=random.choice(brands),
            part_number=str(random.randint(100000, 999999)),
            origin_country=random.choice(countries),
            price=random.randint(200, 8000),
        )
    return HttpResponse(f"Додано {count} нових записів")
