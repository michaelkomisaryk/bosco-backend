import random

from django.http import HttpResponse

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
    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>Автозапчастини</title>
    </head>
    <body>
        <h1>Список автозапчастин</h1>
        <table border="1" cellpadding="5">
            <tr>
                <th>Назва</th>
                <th>Марка авто</th>
                <th>Артикул</th>
                <th>Країна походження</th>
                <th>Ціна</th>
            </tr>
    """
    for p in products:
        html += f"""
            <tr>
                <td>{p.name}</td>
                <td>{p.vehicle_brand}</td>
                <td>{p.part_number}</td>
                <td>{p.origin_country}</td>
                <td>{p.price}</td>
            </tr>
        """
    html += """
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)


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
