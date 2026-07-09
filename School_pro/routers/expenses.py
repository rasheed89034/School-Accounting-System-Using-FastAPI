from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import model, schemas
from dataBase import get_db

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses Management"]
)


@router.post("/category", response_model=schemas.ExpenseCategoryResponse)
def create_category(category: schemas.ExpenseCategoryCreate, db: Session = Depends(get_db)):
    new_category = models.ExpenseCategory(category_name=category.category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category


@router.post("/", response_model=schemas.ExpenseResponse)
def create_expense(expense: schemas.ExpenseCreate, db: Session = Depends(get_db)):
    db_cat = db.query(model.ExpenseCategory).filter(model.ExpenseCategory.id == expense.category_id).first()
    if not db_cat:
        raise HTTPException(status_code=404, detail="First add Expense Category!")
        
    new_expense = model.Expense(
        category_id=expense.category_id,
        amount=expense.amount,
        description=expense.description
    )
    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)
    return new_expense