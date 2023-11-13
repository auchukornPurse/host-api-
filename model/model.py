from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

DATABASE_URL = "postgresql+psycopg2://test_api_se65_user:cXRT7TOB6O8NXx1NGQLrzIUAJ8XpMTeQ@dpg-cl8ov7qvokcc73b22ip0-a.singapore-postgres.render.com/test_api_se65"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "user_table"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    fname = Column(String)
    lname = Column(String)

Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    username: str
    password: str
    fname: str
    lname: str