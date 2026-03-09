from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models import InvoiceItem
from schemas import (
    InvoiceItemResponse, InvoiceItemCreate, InvoiceItemUpdate
)

router = APIRouter(
    prefix="/invoice-items",
    tags=["invoice-items"]
)

@router.get("/{invoice_id}", response_model=list[InvoiceItemResponse])
def get_invoice_items_by_invoice_id(invoice_id: int, db: Session = Depends(get_db)):
    return db.query(InvoiceItem).filter(InvoiceItem.invoiceId == invoice_id).all()

@router.post("/", response_model=InvoiceItemResponse, status_code=201)
def create_invoice_item(invoice_item: InvoiceItemCreate, db: Session = Depends(get_db)):
    db_invoice_item = InvoiceItem(**invoice_item.model_dump())
    db.add(db_invoice_item)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invoice item already exists")
    db.refresh(db_invoice_item)
    return db_invoice_item

@router.put("/{id}", response_model=InvoiceItemResponse)
def update_invoice_item(id: int, data: InvoiceItemUpdate, db: Session = Depends(get_db)):
    db_invoice_item = db.query(InvoiceItem).filter(InvoiceItem.id == id).first()

    if db_invoice_item is None:
        raise HTTPException(status_code=404, detail=f"Invoice item id {id} not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_invoice_item, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invoice item id {id} not changed")
    db.refresh(db_invoice_item)
    return db_invoice_item

@router.delete("/{id}", status_code=204)
def delete_invoice_item(id: int, db: Session = Depends(get_db)):
    db_invoice_item = db.query(InvoiceItem).filter(InvoiceItem.id == id).first()

    if db_invoice_item is None:
        raise HTTPException(status_code=404, detail=f"Invoice item id {id} not found")
    
    db.delete(db_invoice_item)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invoice item id {id} not deleted")