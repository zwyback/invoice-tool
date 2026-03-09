from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from database import get_db
from models import Customer
from schemas import (
    CustomerResponse, CustomerCreate, CustomerUpdate
)

router = APIRouter(
    prefix="/customers",
    tags=["customers"]
)

@router.get("/", response_model=list[CustomerResponse])
def get_all_customer(db: Session = Depends(get_db)):
    return db.query(Customer).all()

@router.get("/{id}", response_model=CustomerResponse)
def get_customer_by_id(id: int, db: Session = Depends(get_db)):
    customer = db.query(Customer).filter(Customer.id == id).first()

    if customer is None:
        raise HTTPException(status_code=404, detail=f"Customer id {id} not found")
    return customer

@router.post("/", response_model=CustomerResponse, status_code=201)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    db_customer = Customer(**customer.model_dump())
    db.add(db_customer)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Customer already exists")
    db.refresh(db_customer)
    return db_customer

@router.put("/{id}", response_model=CustomerResponse)
def update_customer(id: int, data: CustomerUpdate, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == id).first()

    if db_customer is None:
        raise HTTPException(status_code=404, detail=f"Customer id {id} not found")
    
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(db_customer, key, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Customer id {id} not changed")
    db.refresh(db_customer)
    return db_customer

@router.delete("/{id}", status_code=204)
def delete_customer(id: int, db: Session = Depends(get_db)):
    db_customer = db.query(Customer).filter(Customer.id == id).first()

    if db_customer is None:
        raise HTTPException(status_code=404, detail=f"Customer id {id} not found")
    
    db.delete(db_customer)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Customer id {id} not deleted")
    return db_customer