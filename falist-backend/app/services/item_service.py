from typing import List
from ..repositories.item_repository import ItemRepository
from ..schemas import ItemCreate, ItemUpdate


class ItemService:
    def __init__(self, repo: ItemRepository):
        self.repo = repo

    def get_item(self, item_id: int):
        return self.repo.get(item_id)

    def list_items(self, skip: int = 0, limit: int = 100):
        return self.repo.list(skip, limit)

    def create_item(self, payload: ItemCreate):
        return self.repo.create(
            title=payload.title,
            description=payload.description
        )

    def update_item(self, item, payload: ItemUpdate):
        return self.repo.update(
            item,
            title=payload.title,
            description=payload.description
        )

    def delete_item(self, item):
        return self.repo.delete(item)
