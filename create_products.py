import requests

API_URL = "https://my-online-store-api.onrender.com/products/"

products = [
    {
        "title": "Mechanical Keyboard Attack Shark R85HE",
        "description": "Magnetic switches, Rapid Trigger, 8K polling rate, RGB backlight.",
        "category": "Keyboards",
        "price": 89.99,
        "old_price": 109.99,
        "stock_quantity": 15,
        "brand": "Attack Shark",
        "image_url": "https://images.unsplash.com/photo-1587829741301-dc798b83add3",
        "is_new": True,
        "is_on_sale": True,
        "discount_percentage": 18,
        "is_active": True,
        "id": 0
    },
    {
        "title": "Wireless Gaming Mouse ATK Dragonfly A9 Pro",
        "description": "PixArt 3953 sensor, ultra-lightweight design, up to 8K polling rate.",
        "category": "Mice",
        "price": 69.99,
        "old_price": 79.99,
        "stock_quantity": 25,
        "brand": "ATK",
        "image_url": "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7",
        "is_new": True,
        "is_on_sale": True,
        "discount_percentage": 12,
        "is_active": True,
        "id": 0
    },
    {
        "title": "Machenike TH66 TWS Earbuds",
        "description": "Active Noise Cancellation, low latency gaming mode, Bluetooth 5.3.",
        "category": "Audio",
        "price": 45.00,
        "old_price": 55.00,
        "stock_quantity": 40,
        "brand": "Machenike",
        "image_url": "https://images.unsplash.com/photo-1590658268037-6bf12165a8df",
        "is_new": False,
        "is_on_sale": True,
        "discount_percentage": 18,
        "is_active": True,
        "id": 0
    },
    {
        "title": "Fast IPS 27 Gaming Monitor 1440p",
        "description": "27-inch QHD display, 240Hz refresh rate, 1ms response time, HDR400.",
        "category": "Monitors",
        "price": 299.99,
        "old_price": 349.99,
        "stock_quantity": 8,
        "brand": "AOC",
        "image_url": "https://images.unsplash.com/photo-1527443224154-c4a3942d3acf",
        "is_new": True,
        "is_on_sale": False,
        "discount_percentage": 0,
        "is_active": True,
        "id": 0
    }
]

# Если для создания товаров требуется авторизация (токен), укажите его ниже в заголовках:
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTc5MjE3MDg4NH0.XZAf9gKUH0hxOxQA0-nbmfN8Pu-JnIHGXokzVCeaaKg"}

for item in products:
    response = requests.post(API_URL, json=item, headers=headers)
    print(f"Status: {response.status_code}, Response: {response.text}")