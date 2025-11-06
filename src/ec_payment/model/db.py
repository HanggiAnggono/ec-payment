from sqlalchemy import create_engine
from sqlmodel import SQLModel

engine = create_engine("sqlite:///ec_payment_dev.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)