from typing import Generator
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

engine = create_engine("sqlite:///ec_payment_dev.db")

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session() -> Generator[Session, Session, None]:
    print("Initializing db session")
    with Session(engine) as session:
        yield session