from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas
from dataBase import get_db

router = APIRouter(
    prefix="/classes",
    tags=["Classes Management"]
)


@router.post("/", response_model=schemas.ClassGradeResponse)
def create_class(class_data: schemas.ClassGradeCreate, db: Session = Depends(get_db)):

    db_class = db.query(model.ClassGrade).filter(model.ClassGrade.class_name == class_data.class_name).first()
    if db_class:
        raise HTTPException(status_code=400, detail="Class Already Exist")
    

    new_class = model.ClassGrade(
        class_name=class_data.class_name,
        monthly_tuition_fee=class_data.monthly_tuition_fee
    )
    db.add(new_class)
    db.commit()
    db.refresh(new_class)
    
    return new_class


@router.get("/", response_model=list[schemas.ClassGradeResponse])
def get_classes(db: Session = Depends(get_db)):
    classes = db.query(model.ClassGrade).all()
    return classes