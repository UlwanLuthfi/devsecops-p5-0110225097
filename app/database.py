from typing import Dict, List, Optional
from app.models import ItemCreate, ItemResponse, ItemStatus


class InMemoryDatabase:
    """Simple in-memory storage for managing items."""

    def __init__(self) -> None:
        self._items: Dict[int, ItemResponse] = {}
        self._counter: int = 1
        self._seed_data()

    def _seed_data(self) -> None:
        initial_items = [
            ItemCreate(
                name="Security Key",
                description="Hardware FIDO2 authenticator",
                price=49.99,
                status=ItemStatus.AVAILABLE,
            ),
            ItemCreate(
                name="Encrypted USB Drive",
                description="AES-256 encrypted storage",
                price=29.99,
                status=ItemStatus.AVAILABLE,
            ),
        ]
        for item in initial_items:
            self.create_item(item)

    def get_all(self) -> List[ItemResponse]:
        return list(self._items.values())

    def get_by_id(self, item_id: int) -> Optional[ItemResponse]:
        return self._items.get(item_id)

    def create_item(self, item: ItemCreate) -> ItemResponse:
        new_item = ItemResponse(id=self._counter, **item.model_dump())
        self._items[self._counter] = new_item
        self._counter += 1
        return new_item

    def delete_item(self, item_id: int) -> bool:
        if item_id in self._items:
            del self._items[item_id]
            return True
        return False


db = InMemoryDatabase()
