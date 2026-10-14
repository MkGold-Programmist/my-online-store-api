from app.database.database import SessionLocal, engine
from app.models.user import User
from app.auth import get_password_hash
from app.database.database import Base

Base.metadata.create_all(bind=engine)

db = SessionLocal()

existing_admin = db.query(User).filter(User.username == "admin").first()
if existing_admin:
    print("Admin already exists!")
else:
    admin = User(
        username="admin",
        email="admin@techshop.com",
        hashed_password=get_password_hash("admin123"),
        is_admin=True,
        is_active=True
    )

    db.add(admin)
    db.commit()
    print("✅ Admin created successfully!")
    print("Username: admin")
    print("Password: admin123")
    print("Email: admin@techshop.com")

db.close()
