from app.database.database import SessionLocal, engine
from app.models.user import User
from app.auth import get_password_hash
from app.database.database import Base

try:
    # Создаем таблицы в базе данных, если они еще не созданы
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Проверяем, существует ли уже администратор с таким именем
    existing_admin = db.query(User).filter(User.username == "admin").first()

    if existing_admin:
        print("⚠️ Admin already exists!")
    else:
        raw_password = "admin123"

        # Защита от ограничения bcrypt в 72 байта
        safe_password = raw_password[:72]

        admin = User(
            username="admin",
            email="admin@techshop.com",
            hashed_password=get_password_hash(safe_password),
            is_admin=True,
            is_active=True
        )

        db.add(admin)
        db.commit()
        print("✅ Admin created successfully!")
        print("Username: admin")
        print(f"Password: {raw_password}")
        print("Email: admin@techshop.com")

except Exception as e:
    print(f"❌ Произошла ошибка при создании администратора: {e}")
finally:
    # Всегда закрываем сессию базы данных в блоке finally
    db.close()