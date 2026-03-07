from pydantic import BaseModel
from typing import Optional
from datetime import date

# customer schemas

class CustomerBase(BaseModel):
    surname: str
    forename: str
    email: str
    zipCode: str
    city: str
    adress: str

class CustomerCreate(CustomerBase):
    pass

class CustomerUpdate(CustomerBase):
    surname: Optional[str] = None
    forename: Optional[str] = None
    email: Optional[str] = None
    zipCode: Optional[str] = None
    city: Optional[str] = None
    adress: Optional[str] = None

class CustomerResponse(CustomerBase):
    id: int
    
    class Config:
        from_attributes = True
    
# invoice schemas

class InvoiceBase(BaseModel):
    date: date
    status: str

class InvoiceCreate(InvoiceBase):
    customer_id: int

class InvoiceUpdate(InvoiceBase):
    date: Optional[date] = None
    status: Optional[str] = None
    customerId: Optional[int] = None

class InvoiceResponse(InvoiceBase):
    customerId: int

    class Config:
        from_attributes = True

# product schemas

class ProductBase(BaseModel):
    name: str
    price: float
    unit: str

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None
    unit: Optional[str] = None

class ProductResponse(ProductBase):
    id: int

    class Config:
        from_attributes = True