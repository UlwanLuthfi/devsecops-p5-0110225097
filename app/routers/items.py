from typing import List
from fastapi import APIRouter, HTTPException, status
from app.database import db
from app.models import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["Items"])


@router.get("", response_model=List[ItemResponse])
def list_items() -> List[ItemResponse]:
    """Retrieve all inventory items."""
    return db.get_all()


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int) -> ItemResponse:
    """Retrieve a specific item by ID."""
    item = db.get_by_id(item_id)
    if not item:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
    return item


@router.post("", response_model=ItemResponse, status_code=status.HTTP_201_CREATED)
def create_item(item: ItemCreate) -> ItemResponse:
    """Create a new item entry."""
    return db.create_item(item)


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    """Remove an item by ID."""
    if not db.delete_item(item_id):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Item not found"
        )
