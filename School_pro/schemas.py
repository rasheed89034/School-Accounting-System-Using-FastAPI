from pydantic import BaseModel
from datetime import date
from typing import Optional

class CreateUser(BaseModel):
    username : str
    password_hash : str
    role : Optional[str] = "Admin"

class UserResponse(BaseModel):
    id : int 
    username : str 
    role : str 
    is_active : bool

    class Config:
        from_attributes = True

class ClassGradeCreate(BaseModel):
    class_name: str
    monthly_tuition_fee: float

class ClassGradeResponse(BaseModel):
    id: int
    class_name: str
    monthly_tuition_fee: float

    class Config:
        from_attributes = True


class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    roll_number: str
    class_id: int

class StudentResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    roll_number: str
    status: str
    enrollment_date: date
    class_id: int

    class Config:
        from_attributes = True


class FeeCategoryCreate(BaseModel):
    category_name: str

class FeeCategoryResponse(BaseModel):
    id: int
    category_name: str

    class Config:
        from_attributes = True


class FeeInvoiceCreate(BaseModel):
    student_id: int
    month: str
    total_amount: float
    due_date: date

class FeeInvoiceResponse(BaseModel):
    id: int
    student_id: int
    month: str
    total_amount: float
    due_date: date
    status: str

    class Config:
        from_attributes = True


class FeePaymentCreate(BaseModel):
    invoice_id: int
    amount_paid: float
    payment_method: Optional[str] = "Cash"

class FeePaymentResponse(BaseModel):
    id: int
    invoice_id: int
    amount_paid: float
    payment_date: date
    payment_method: str

    class Config:
        from_attributes = True


class EmployeeCreate(BaseModel):
    name: str
    designation: str
    basic_salary: float

class EmployeeResponse(BaseModel):
    id: int
    name: str
    designation: str
    basic_salary: float
    joining_date: date

    class Config:
        from_attributes = True


class ExpenseCategoryCreate(BaseModel):
    category_name: str

class ExpenseCategoryResponse(BaseModel):
    id: int
    category_name: str

    class Config:
        from_attributes = True


class ExpenseCreate(BaseModel):
    category_id: int
    amount: float
    description: str

class ExpenseResponse(BaseModel):
    id: int
    category_id: int
    amount: float
    description: str
    expense_date: date

    class Config:
        from_attributes = True
