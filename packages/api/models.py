from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from database import Base

class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    surname = Column(String)
    forename = Column(String)
    email = Column(String)
    zipCode = Column(String)
    city = Column(String)
    adress = Column(String)

class Invoice(Base):
    __tablename__ = "invoice"
    id = Column(Integer, primary_key=True)
    customerId = Column(Integer, ForeignKey("kunden.id"))
    date = Column(Date)
    status = Column(String)

class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    unit = Column(String)


class RechnungsPosition(Base):
    __tablename__ = "rechnungs_positionen"
    id = Column(Integer, primary_key=True)
    invoiceId = Column(Integer, ForeignKey("rechnungen.id"))
    productId = Column(Integer, ForeignKey("produkte.id"))
    amount = Column(Integer)

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    zipCode = Column(String)
    city = Column(String)
    adress = Column(String)
    iban = Column(String)
    bic = Column(String)
    bankName = Column(String)