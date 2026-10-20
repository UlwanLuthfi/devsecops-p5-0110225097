from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ItemStatus(str, Enum):
    AVAILABLE = "available"
    OUT_OF_STOCK = "out_of_stock"


class ItemBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=255)
    price: float = Field(..., gt=0)
    status: ItemStatus = ItemStatus.AVAILABLE


class ItemCreate(ItemBase):
    pass


class ItemResponse(ItemBase):
    id: int
