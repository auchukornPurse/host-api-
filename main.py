from fastapi import  Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from model.model import SessionLocal
from passlib.context import CryptContext

import model.model

app = FastAPI()

pwd_context  = CryptContext(schemes=["bcrypt"],deprecated = "auto")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/createuser/")
def create_user(user: model.model.UserCreate, db: Session = Depends(get_db)):
    checkUser = db.query(model.model.User).filter(user.username == model.model.User.username).first()
    db_user = model.model.User(**user.dict())
    if checkUser is None:
        db_user.password = pwd_context.hash(user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return {"suceess" : True , "massage" : "Succes"}
    else:
        return {"suceess" : False , "massage" : "Username already exist"}


@app.post("/login/")
def login_user(user: model.model.UserCreate, db: Session = Depends(get_db)):
    checkUsername  = db.query(model.model.User).filter(user.username == model.model.User.username).first()
   
    if (checkUsername is not None) :
        getPass = pwd_context.verify(user.password, checkUsername.password)
        if getPass:
             return {"suceess" : True , "massage" : "Succes"}
        else :
             return {"suceess" : False , "massage" : "Password missmatch"}
    else :
        return {"suceess" : False , "massage" : "Username missmatch"}