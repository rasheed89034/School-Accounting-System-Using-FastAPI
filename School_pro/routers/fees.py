from fastapi import FastAPI, APIRouter,Depends,HTTPException
import model,schemas
from sqlalchemy.orm import Session
from dataBase import get_db

router = APIRouter(
    prefix="/fees",
    tags=["Fees Management"]
)

@router.post("/invoice",response_model=schemas.FeeInvoiceResponse)
def creat_invoice(invoice : schemas.FeeInvoiceCreate , db:Session = Depends(get_db)):
    db_student = db.query(model.Student).filter(model.Student.id == invoice.student_id).first()
    if not db_student:
        raise HTTPException(status_code=404, detail="Student Not Found!")

    new_invoice = model.FeeInvoice(
        student_id=invoice.student_id,
        month=invoice.month,
        total_amount=invoice.total_amount,
        due_date=invoice.due_date,
        status="Unpaid"
    )

    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice

@router.get("/invoice", response_model=list[schemas.FeeInvoiceResponse])
def get_all_invoices(db: Session = Depends(get_db)):
    return db.query(model.FeeInvoice).all()