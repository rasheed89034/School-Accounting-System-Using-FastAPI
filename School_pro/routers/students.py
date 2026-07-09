from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas
from dataBase import get_db

router = APIRouter(
    prefix="/students",
    tags=["Students Management"]
)


@router.post("/", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
   
    db_class = db.query(model.ClassGrade).filter(models.ClassGrade.id == student.class_id).first()
    if not db_class:
        raise HTTPException(status_code=404, detail="Class Not Found")


    db_student = db.query(model.Student).filter(model.Student.roll_number == student.roll_number).first()
    if db_student:
        raise HTTPException(status_code=400, detail="RollNumber Already exist!")
    
   
    new_student = model.Student(
        first_name=student.first_name,
        last_name=student.last_name,
        roll_number=student.roll_number,
        class_id=student.class_id
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    
    return new_student


@router.get("/", response_model=list[schemas.StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(model.Student).all()