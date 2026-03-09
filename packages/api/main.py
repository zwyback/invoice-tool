from fastapi import FastAPI
from routers import products, customer
from database import Base, engine

# init db
Base.metadata.create_all(bind=engine)

# init api
app = FastAPI()
app.include_router(products.router)
app.include_router(customer.router)