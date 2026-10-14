import os

print("=== Проверка структуры проекта Tech Shop ===\n")

files_to_check = {
    "Models": [
        "app/models/user.py",
        "app/models/product.py", 
        "app/models/cart.py",
        "app/models/wishlist.py"
    ],
    "Schemas": [
        "app/schemas/user.py",
        "app/schemas/product.py",
        "app/schemas/cart.py",
        "app/schemas/wishlist.py"
    ],
    "Routers": [
        "app/routers/auth.py",
        "app/routers/users.py",
        "app/routers/products.py",
        "app/routers/cart.py",
        "app/routers/wishlist.py"
    ],
    "Core": [
        "app/main.py",
        "app/auth.py",
        "app/config.py",
        "app/database/database.py"
    ],
    "Config": [
        "requirements.txt",
        ".env",
        "run.py",
        "create_admin.py"
    ]
}

all_ok = True
for category, files in files_to_check.items():
    print(f"📁 {category}:")
    for file in files:
        exists = os.path.exists(file)
        status = "✅" if exists else "❌"
        print(f"  {status} {file}")
        if not exists:
            all_ok = False
    print()

if all_ok:
    print("✅ Все файлы на месте!")
else:
    print("❌ Некоторые файлы отсутствуют!")
