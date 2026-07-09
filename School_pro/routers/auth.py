from fastapi import FastAPI,Depends,HTTPException,APIRouter
from sqlalchemy.orm import Session
import model , schemas 
from dataBase import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register",response_model = schemas.UserResponse)

def register_user(user: schemas.CreateUser, db:Session=Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.username == user.username).first()

    if db_user:
        raise HTTPException(status_code=400, detail="Username Already Exist")

    new_user = model.User(
        username = user.username,
        password_hash = user.password_hash,
        role = user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user