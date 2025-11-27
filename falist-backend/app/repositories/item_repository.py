from sqlalchemy.orm import Session
from ..models import Item
from typing import List, Optional


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get(self, item_id: int) -> Optional[Item]:
        return self.db.query(Item).filter(Item.id == item_id).first()

    def list(self, skip: int = 0, limit: int = 100) -> List[Item]:
        return self.db.query(Item).offset(skip).limit(limit).all()

    def create(self, title: str, description: str = None) -> Item:
        db_item = Item(title=title, description=description)
        self.db.add(db_item)
        self.db.commit()
        self.db.refresh(db_item)
        return db_item

    def update(self, item: Item, title: str = None, description: str = None) -> Item:
        if title is not None:
            item.title = title
        if description is not None:
            item.description = description

        self.db.commit()
        self.db.refresh(item)
        return item

    def delete(self, item: Item) -> None:
        self.db.delete(item)
        self.db.commit()
