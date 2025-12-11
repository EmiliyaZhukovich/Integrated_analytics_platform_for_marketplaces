"""Generate mock marketplace data using Faker."""

import random
from datetime import datetime, timedelta
from typing import List
from faker import Faker

fake = Faker("ru_RU")

# Маркетплейсы
MARKETPLACES = ["Wildberries", "Ozon", "Yandex.Market"]
PLATFORMS = ["Wildberries", "Ozon", "Yandex.Market"]

# Категории товаров
CATEGORIES = [
    {"name": "Электроника", "slug": "electronics"},
    {"name": "Одежда и обувь", "slug": "clothing"},
    {"name": "Книги", "slug": "books"},
    {"name": "Спорт и отдых", "slug": "sports"},
    {"name": "Дом и сад", "slug": "home"},
    {"name": "Красота и здоровье", "slug": "beauty"},
    {"name": "Игрушки", "slug": "toys"},
    {"name": "Автотовары", "slug": "auto"},
]

# Примеры названий товаров по категориям
PRODUCT_NAMES = {
    "electronics": [
        "Смартфон", "Наушники", "Зарядное устройство", "Кабель USB", "Портативная батарея",
        "Планшет", "Смарт-часы", "Монитор", "Клавиатура", "Мышка",
    ],
    "clothing": [
        "Футболка", "Джинсы", "Куртка", "Свитер", "Платье",
        "Рубашка", "Брюки", "Шорты", "Пиджак", "Кардиган",
    ],
    "books": [
        "Роман", "Детектив", "Фантастика", "Поэзия", "История",
        "Биография", "Развитие", "Учебник", "Комикс", "Графический роман",
    ],
    "sports": [
        "Гантели", "Беговая дорожка", "Коврик для йоги", "Скакалка", "Велотренажер",
        "Боксерская груша", "Ролики", "Скейтборд", "Палатка", "Спальный мешок",
    ],
    "home": [
        "Полотенце", "Подушка", "Одеяло", "Скатерть", "Шторы",
        "Лампа", "Вазон", "Кухонный нож", "Кастрюля", "Сковорода",
    ],
    "beauty": [
        "Шампунь", "Кондиционер", "Зубная паста", "Крем", "Маска",
        "Помада", "Тушь", "Тональный крем", "Мыло", "Дезодорант",
    ],
    "toys": [
        "Кубики", "Машинка", "Кукла", "Пазл", "Конструктор",
        "Настольная игра", "Карточная игра", "Робот", "Дрон", "Мяч",
    ],
    "auto": [
        "Автомасло", "Воздушный фильтр", "Щетки стеклоочистителя", "Коврик салона", "Ароматизатор",
        "Аккумулятор", "Колпачок колеса", "Лебедка", "Багажник", "Фара",
    ],
}


def generate_categories() -> List[dict]:
    """Generate category data."""
    return CATEGORIES


def generate_products(num_products: int = 100) -> List[dict]:
    """Generate mock product data."""
    products = []

    for category in CATEGORIES:
        names = PRODUCT_NAMES.get(category["slug"], ["Товар"])

        # 10-15 товаров на категорию
        for _ in range(random.randint(10, 15)):
            product = {
                "name": f"{random.choice(names)} {fake.word()}",
                "category_id": category["slug"],  # Будет заменено на ID при вставке
                "price": round(random.uniform(100, 50000), 2),
                "stock": random.randint(0, 1000),
            }
            products.append(product)

    return products[:num_products]


def generate_orders(num_orders: int = 500, product_ids: List[int] = None) -> List[dict]:
    """Generate mock order data."""
    if product_ids is None:
        product_ids = list(range(1, 101))

    orders = []
    base_date = datetime.now() - timedelta(days=365)

    for _ in range(num_orders):
        order = {
            "product_id": random.choice(product_ids),
            "quantity": random.randint(1, 10),
            "total_price": round(random.uniform(100, 50000), 2),
            "order_date": base_date + timedelta(
                days=random.randint(0, 365),
                hours=random.randint(0, 23),
                minutes=random.randint(0, 59),
            ),
            "marketplace": random.choice(MARKETPLACES),
        }
        orders.append(order)

    return orders


def generate_campaigns(num_campaigns: int = 150, product_ids: List[int] = None) -> List[dict]:
    """Generate mock advertising campaign data."""
    if product_ids is None:
        product_ids = list(range(1, 101))

    campaigns = []

    for _ in range(num_campaigns):
        impressions = random.randint(1000, 100000)
        clicks = random.randint(0, impressions // 10)
        conversions = random.randint(0, clicks // 5)

        campaign = {
            "product_id": random.choice(product_ids),
            "platform": random.choice(PLATFORMS),
            "budget": round(random.uniform(1000, 100000), 2),
            "impressions": impressions,
            "clicks": clicks,
            "conversions": conversions,
        }
        campaigns.append(campaign)

    return campaigns


def generate_all_data(
    num_products: int = 100,
    num_orders: int = 500,
    num_campaigns: int = 150,
) -> dict:
    """Generate all mock data."""
    print("Generating mock data...")

    categories = generate_categories()
    products = generate_products(num_products)

    print(f"✓ Generated {len(categories)} categories")
    print(f"✓ Generated {len(products)} products")

    # Product IDs will be assigned during DB insertion
    orders = generate_orders(num_orders, product_ids=None)
    campaigns = generate_campaigns(num_campaigns, product_ids=None)

    print(f"✓ Generated {len(orders)} orders")
    print(f"✓ Generated {len(campaigns)} campaigns")

    return {
        "categories": categories,
        "products": products,
        "orders": orders,
        "campaigns": campaigns,
    }
