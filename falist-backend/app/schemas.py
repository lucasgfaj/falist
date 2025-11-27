from pydantic import BaseModel
from typing import Optional


class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    pass


class ItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


class ItemInDBBase(ItemBase):
    id: int

    class Config:
        orm_mode = True


class Item(ItemInDBBase):
    pass
