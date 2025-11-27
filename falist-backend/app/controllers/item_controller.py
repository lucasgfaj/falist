from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..repositories.item_repository import ItemRepository
from ..services.item_service import ItemService
from .. import schemas


router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=schemas.Item)
def create_item(payload: schemas.ItemCreate, db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    service = ItemService(repo)
    return service.create_item(payload)


@router.get("/", response_model=list[schemas.Item])
def list_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    service = ItemService(repo)
    return service.list_items(skip, limit)


@router.get("/{item_id}", response_model=schemas.Item)
def get_item(item_id: int, db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    service = ItemService(repo)
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/{item_id}", response_model=schemas.Item)
def update_item(item_id: int, payload: schemas.ItemUpdate, db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    service = ItemService(repo)
    item = service.get_item(item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return service.update_item(item, payload)


@router.delete("/{item_id}")
def delete_item(item_id: int, db: Session = Depends(get_db)):
    repo = ItemRepository(db)
    service = ItemService(repo)
    item = service.get_item(item_id)  # <-- corrigido: antes estava service.get(...)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    service.delete_item(item)
    return {"ok": True}
