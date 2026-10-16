import asyncio
from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from app.database.database import engine, Base
from app.routers import auth, users, products, cart, wishlist

Base.metadata.create_all(bind=engine)

SELF_URL = "https://my-online-store-api.onrender.com/"


async def keep_alive():
  await asyncio.sleep(10)
  async with httpx.AsyncClient() as client:
    while True:
      try:
        await client.get(SELF_URL)
      except Exception:
        pass
      await asyncio.sleep(600)


@asynccontextmanager
async def lifespan(app: FastAPI):
  task = asyncio.create_task(keep_alive())
  yield
  task.cancel()

app = FastAPI(
    title="Tech Shop API",
    description="API для интернет-магазина техники с регистрацией, корзиной, wishlist и админ-панелью",
    version="1.0.0",
    lifespan=lifespan  # 2. Обязательно передаем lifespan сюда!
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(products.router)
app.include_router(cart.router)
app.include_router(wishlist.router)

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title=app.title,
        version=app.version,
        description=app.description,
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.get("/")
def root():
    return {
        "message": "Welcome to Tech Shop API",
        "docs": "/docs",
        "redoc": "/redoc"
    }