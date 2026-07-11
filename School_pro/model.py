from sqlalchemy import Column,Integer,String,Float,Date,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from dataBase import Base
import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String,unique=True,index=True)
    password_hash = Column(String)
    role = Column(String, default='Admin')
    is_active = Column(Boolean,default=True)

class ClassGrade(Base):
    __tablename__ = "classes"

    id = Column(Integer,primary_key=True,index=True)
    class_name = Column(String,unique=True,index=True)
    monthly_tuition_fee = Column(Float)

    ## Define relationship
    students = relationship("Student" ,back_populates="student_class")

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer,primary_key=True,index=True)
    first_name = Column(String)
    last_name = Column(String)
    roll_number = Column(String,unique=True,index=True)
    enrollment_date = Column(Date,default=datetime.date.today)

    class_id = Column(Integer,ForeignKey("classes.id"))

    ## Relationships

    student_class = relationship("ClassGrade",back_populates="students")
    invoices = relationship("FeeInvoice",back_populates="student")


class FeeCategory(Base):
    __tablename__ = "fee_category"

    id = Column(Integer,primary_key=True,index=True)
    category_name = Column(String,unique=True)

class FeeInvoice(Base):
    __tablename__ = "fee_invoices"

    id = Column(Integer,primary_key=True,index=True)
    student_id = Column(Integer,ForeignKey("students.id"))
    month = Column(String)
    total_amount = Column(Float)
    due_date = Column(Date)
    status = Column(String,default="Unpaid")


    ## Relationships
    student = relationship("Student",back_populates="invoices")
    payments = relationship("FeePayment",back_populates="invoice")


class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("fee_invoices.id"))
    amount_paid = Column(Float)
    payment_date = Column(Date, default=datetime.date.today)
    payment_method = Column(String, default="Cash") # Cash, Bank

    # Relationships
    invoice = relationship("FeeInvoice", back_populates="payments")

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_number = Column(String)
    designation = Column(String)
    basic_salary = Column(Float)
    joining_date = Column(Date, default=datetime.date.today)

class ExpenseCategory(Base):
    __tablename__ = "expense_categories"

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String, unique=True) # Salaries, Bills, Maintenance

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey("expense_categories.id"))
    amount = Column(Float)
    description = Column(String)
    expense_date = Column(Date, default=datetime.date.today)
