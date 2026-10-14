from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.models.user import User
from app.models.wishlist import WishlistItem
from app.models.product import Product
from app.schemas.wishlist import WishlistItemCreate, WishlistItemResponse
from app.auth import get_current_active_user

router = APIRouter(prefix="/wishlist", tags=["Wishlist"], include_in_schema=True )

@router.get("/", response_model=list[WishlistItemResponse])
def get_wishlist(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Получить список желаний текущего пользователя"""
    wishlist_items = db.query(WishlistItem).filter(
        WishlistItem.user_id == current_user.id
    ).all()
    return wishlist_items

@router.post("/", response_model=WishlistItemResponse, status_code=status.HTTP_201_CREATED)
def add_to_wishlist(
    item: WishlistItemCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Добавить товар в список желаний"""
    product = db.query(Product).filter(Product.id == item.product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    existing_item = db.query(WishlistItem).filter(
        WishlistItem.user_id == current_user.id,
        WishlistItem.product_id == item.product_id
    ).first()

    if existing_item:
        raise HTTPException(
            status_code=400,
            detail="Product already in wishlist"
        )

    new_item = WishlistItem(
        user_id=current_user.id,
        product_id=item.product_id
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_from_wishlist(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Удалить товар из списка желаний"""
    wishlist_item = db.query(WishlistItem).filter(
        WishlistItem.id == item_id,
        WishlistItem.user_id == current_user.id
    ).first()

    if not wishlist_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found")

    db.delete(wishlist_item)
    db.commit()
    return None

@router.delete("/product/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_product_from_wishlist(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Удалить товар из списка желаний по ID товара"""
    wishlist_item = db.query(WishlistItem).filter(
        WishlistItem.product_id == product_id,
        WishlistItem.user_id == current_user.id
    ).first()

    if not wishlist_item:
        raise HTTPException(status_code=404, detail="Product not in wishlist")

    db.delete(wishlist_item)
    db.commit()
    return None

@router.delete("/", status_code=status.HTTP_204_NO_CONTENT)
def clear_wishlist(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Очистить весь список желаний"""
    db.query(WishlistItem).filter(
        WishlistItem.user_id == current_user.id
    ).delete()
    db.commit()
    return None

@router.get("/check/{product_id}", response_model=dict)
def check_in_wishlist(
    product_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Проверить, находится ли товар в списке желаний"""
    exists = db.query(WishlistItem).filter(
        WishlistItem.user_id == current_user.id,
        WishlistItem.product_id == product_id
    ).first() is not None

    return {"in_wishlist": exists}
