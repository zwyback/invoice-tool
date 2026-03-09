from fastapi import FastAPI
from routers import products, customers, invoices, invoice_items
from database import Base, engine

# init db
Base.metadata.create_all(bind=engine)

# init api
app = FastAPI()
app.include_router(products.router)
app.include_router(customers.router)
app.include_router(invoices.router)
app.include_router(invoice_items.router)