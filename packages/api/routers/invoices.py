from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models import Invoice
from schemas import (
    InvoiceResponse, InvoiceCreate, InvoiceUpdate
)

router = APIRouter(
    prefix="/invoices",
    tags=["invoices"]
)

@router.get("/", response_model=InvoiceResponse)
def get_all_invoices(db: Session = Depends(get_db)):
    return db.query(Invoice).all()


@router.get("/{id}", response_model=InvoiceResponse)
def get_invoice_by_id(id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == id).first()

    if invoice is None:
        raise HTTPException(status_code=404, detail=f"Invoice id {id} not found")
    return invoice

@router.post("/", response_model=InvoiceResponse, status_code=201)
def create_invoice(invoice: InvoiceCreate, db: Session = Depends(get_db)):
    db_invoice = Invoice(**invoice.model_dump())
    db.add(db_invoice)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Invoice already exists")
    db.refresh(db_invoice)
    return db_invoice

@router.put("/{id}", response_model=InvoiceResponse)
def update_invoice(id: int, data: InvoiceUpdate, db: Session = Depends(get_db)):
    db_invoice = db.query(Invoice).filter(Invoice.id == id).first()

    if db_invoice is None:
        raise HTTPException(status_code=404, detail=f"Invoice id {id} not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_invoice, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invoice id {id} not changed")
    db.refresh(db_invoice)
    return db_invoice

@router.delete("/{id}", status_code=204)
def delete_invoice(id: int, db: Session = Depends(get_db)):
    db_invoice = db.query(Invoice).filter(Invoice.id == id).first()

    if db_invoice is None:
        raise HTTPException(status_code=404, detail=f"Invoice id {id} not found")
    
    db.delete(db_invoice)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Invoice id {id} not deleted")
    