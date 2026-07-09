# # from fastapi import FastAPI, Request, Depends, Form
# # from fastapi.responses import RedirectResponse
# # from fastapi.templating import Jinja2Templates
# # from sqlalchemy.orm import Session
# # from datetime import datetime

# # import model
# # from dataBase import engine, get_db
# # from routers import auth, classes, students, fees, expenses

# # model.Base.metadata.create_all(bind=engine)

# # app = FastAPI(title="School Accounting ERP")
# # templates = Jinja2Templates(directory="templates")

# # app.include_router(auth.router, prefix="/api")
# # app.include_router(classes.router, prefix="/api")
# # app.include_router(students.router, prefix="/api")
# # app.include_router(fees.router, prefix="/api")
# # app.include_router(expenses.router, prefix="/api")

# # # ==========================================
# # # FRONTEND ROUTES (UI Pages)
# # # ==========================================

# # @app.get("/")
# # def dashboard_page(request: Request, db: Session = Depends(get_db)):
# #     total_students = db.query(model.Student).count()
# #     total_classes = db.query(model.ClassGrade).count()
# #     total_staff = db.query(model.Employee).count()
    
# #     paid_invoices = db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Paid").all()
# #     fees_collected = sum(inv.total_amount for inv in paid_invoices)
    
# #     unpaid_invoices = db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Unpaid").all()
# #     pending_dues = sum(inv.total_amount for inv in unpaid_invoices)

# #     all_expenses = db.query(model.Expense).all()
# #     total_expenses = sum(exp.amount for exp in all_expenses)

# #     return templates.TemplateResponse("dashboard.html", {
# #         "request": request,
# #         "total_students": total_students,
# #         "fees_collected": fees_collected,
# #         "pending_dues": pending_dues,
# #         "total_classes": total_classes,
# #         "total_staff": total_staff,
# #         "total_expenses": total_expenses
# #     })

# # # --- UI Pages Loading ---
# # @app.get("/classes-page")
# # def classes_page(request: Request, db: Session = Depends(get_db)):
# #     return templates.TemplateResponse("classes.html", {"request": request, "classes": db.query(model.ClassGrade).all()})

# # @app.get("/students-page")
# # def students_page(request: Request, db: Session = Depends(get_db)):
# #     return templates.TemplateResponse("students.html", {"request": request, "students": db.query(model.Student).all(), "classes": db.query(model.ClassGrade).all()})

# # @app.get("/receive-fee-page")
# # def receive_fee_page(request: Request, db: Session = Depends(get_db)):
# #     return templates.TemplateResponse("receive_fee.html", {"request": request, "invoices": db.query(model.FeeInvoice).all()})

# # @app.get("/employees-page")
# # def employees_page(request: Request, db: Session = Depends(get_db)):
# #     return templates.TemplateResponse("employees.html", {"request": request, "employees": db.query(model.Employee).all()})

# # @app.get("/expenses-page")
# # def expenses_page(request: Request, db: Session = Depends(get_db)):
# #     return templates.TemplateResponse("expenses.html", {"request": request, "expenses": db.query(model.Expense).all()})

# # # ==========================================
# # # HTML FORM SUBMISSIONS (Web se data save karna)
# # # ==========================================

# # @app.post("/submit-class")
# # def submit_class(
# #     class_name: str = Form(...),
# #     monthly_tuition_fee: float = Form(...),
# #     db: Session = Depends(get_db)
# # ):
# #     new_class = model.ClassGrade(class_name=class_name, monthly_tuition_fee=monthly_tuition_fee)
# #     db.add(new_class)
# #     db.commit()
# #     # Data save hone ke baad wapis classes page par bhej do
# #     return RedirectResponse(url="/classes-page", status_code=303)

# # @app.post("/submit-student")
# # def submit_student(
# #     first_name: str = Form(...),
# #     last_name: str = Form(...),
# #     roll_number: str = Form(...),
# #     class_id: int = Form(...),
# #     db: Session = Depends(get_db)
# # ):
# #     new_student = model.Student(
# #         first_name=first_name, 
# #         last_name=last_name, 
# #         roll_number=roll_number, 
# #         class_id=class_id
# #     )
# #     db.add(new_student)
# #     db.commit()
# #     # Data save hone ke baad wapis students page par bhej do
# #     return RedirectResponse(url="/students-page", status_code=303)


# from fastapi import FastAPI, Request, Depends, Form
# from fastapi.responses import RedirectResponse
# from fastapi.templating import Jinja2Templates
# from sqlalchemy.orm import Session
# from datetime import datetime

# import model
# from dataBase import engine, get_db
# from routers import auth, classes, students, fees, expenses

# model.Base.metadata.create_all(bind=engine)

# app = FastAPI(title="School Accounting ERP")
# templates = Jinja2Templates(directory="templates")

# # API Routers
# app.include_router(auth.router, prefix="/api")
# app.include_router(classes.router, prefix="/api")
# app.include_router(students.router, prefix="/api")
# app.include_router(fees.router, prefix="/api")
# app.include_router(expenses.router, prefix="/api")

# # ==========================================
# # UI PAGES
# # ==========================================

# @app.get("/")
# def dashboard_page(request: Request, db: Session = Depends(get_db)):
#     # Stats logic
#     return templates.TemplateResponse("dashboard.html", {
#         "request": request,
#         "total_students": db.query(model.Student).count(),
#         "total_classes": db.query(model.ClassGrade).count(),
#         "total_staff": db.query(model.Employee).count(),
#         "fees_collected": sum(inv.total_amount for inv in db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Paid").all()),
#         "pending_dues": sum(inv.total_amount for inv in db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Unpaid").all()),
#         "total_expenses": sum(exp.amount for exp in db.query(model.Expense).all())
#     })

# @app.get("/classes-page")
# def classes_page(request: Request, db: Session = Depends(get_db)):
#     return templates.TemplateResponse("classes.html", {"request": request, "classes": db.query(model.ClassGrade).all()})

# @app.get("/students-page")
# def students_page(request: Request, db: Session = Depends(get_db)):
#     return templates.TemplateResponse("students.html", {"request": request, "students": db.query(model.Student).all(), "classes": db.query(model.ClassGrade).all()})

# @app.get("/receive-fee-page")
# def receive_fee_page(request: Request, db: Session = Depends(get_db)):
#     # Fee page par students bhejna zaruri hai dropdown ke liye
#     return templates.TemplateResponse("receive_fee.html", {
#         "request": request, 
#         "invoices": db.query(model.FeeInvoice).all(),
#         "students": db.query(model.Student).all()
#     })

# @app.get("/employees-page")
# def employees_page(request: Request, db: Session = Depends(get_db)):
#     return templates.TemplateResponse("employees.html", {"request": request, "employees": db.query(model.Employee).all()})

# @app.get("/expenses-page")
# def expenses_page(request: Request, db: Session = Depends(get_db)):
#     return templates.TemplateResponse("expenses.html", {"request": request, "expenses": db.query(model.Expense).all()})

# # ==========================================
# # FORM SUBMISSION HANDLERS
# # ==========================================

# @app.post("/submit-class")
# def submit_class(class_name: str = Form(...), monthly_tuition_fee: float = Form(...), db: Session = Depends(get_db)):
#     db.add(model.ClassGrade(class_name=class_name, monthly_tuition_fee=monthly_tuition_fee))
#     db.commit()
#     return RedirectResponse(url="/classes-page", status_code=303)

# @app.post("/submit-student")
# def submit_student(first_name: str = Form(...), last_name: str = Form(...), roll_number: str = Form(...), class_id: int = Form(...), db: Session = Depends(get_db)):
#     db.add(model.Student(first_name=first_name, last_name=last_name, roll_number=roll_number, class_id=class_id))
#     db.commit()
#     return RedirectResponse(url="/students-page", status_code=303)

# @app.post("/submit-fee")
# def submit_fee(student_id: int = Form(...), month: str = Form(...), amount: float = Form(...), due_date: str = Form(...), status: str = Form(...), db: Session = Depends(get_db)):
#     # Date parsing
#     parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
#     db.add(model.FeeInvoice(student_id=student_id, month=month, total_amount=amount, due_date=parsed_date, status=status))
#     db.commit()
#     return RedirectResponse(url="/receive-fee-page", status_code=303)

# @app.post("/submit-employee")
# def submit_employee(first_name: str = Form(...), last_name: str = Form(...), role: str = Form(...), salary: float = Form(...), db: Session = Depends(get_db)):
#     db.add(model.Employee(first_name=first_name, last_name=last_name, role=role, salary=salary))
#     db.commit()
#     return RedirectResponse(url="/employees-page", status_code=303)

# @app.post("/submit-expense")
# def submit_expense(category_id: int = Form(...), description: str = Form(...), amount: float = Form(...), db: Session = Depends(get_db)):
#     db.add(model.Expense(category_id=category_id, description=description, amount=amount))
#     db.commit()
#     return RedirectResponse(url="/expenses-page", status_code=303)


from fastapi import FastAPI, Request, Depends, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from datetime import datetime

import model
from dataBase import engine, get_db
from routers import auth, classes, students, fees, expenses

# Tables create karna
model.Base.metadata.create_all(bind=engine)

app = FastAPI(title="School Accounting ERP")
templates = Jinja2Templates(directory="templates")

# Routers include karna
app.include_router(auth.router, prefix="/api")
app.include_router(classes.router, prefix="/api")
app.include_router(students.router, prefix="/api")
app.include_router(fees.router, prefix="/api")
app.include_router(expenses.router, prefix="/api")

# --- Dashboard Route ---
@app.get("/")
def dashboard_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("dashboard.html", {
        "request": request,
        "total_students": db.query(model.Student).count(),
        "total_classes": db.query(model.ClassGrade).count(),
        "total_staff": db.query(model.Employee).count(),
        "fees_collected": sum(inv.total_amount for inv in db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Paid").all()),
        "pending_dues": sum(inv.total_amount for inv in db.query(model.FeeInvoice).filter(model.FeeInvoice.status == "Unpaid").all()),
        "total_expenses": sum(exp.amount for exp in db.query(model.Expense).all())
    })

# --- UI Pages ---
@app.get("/classes-page")
def classes_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("classes.html", {"request": request, "classes": db.query(model.ClassGrade).all()})

@app.get("/students-page")
def students_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("students.html", {"request": request, "students": db.query(model.Student).all(), "classes": db.query(model.ClassGrade).all()})

@app.get("/receive-fee-page")
def receive_fee_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("receive_fee.html", {"request": request, "invoices": db.query(model.FeeInvoice).all(), "students": db.query(model.Student).all()})

@app.get("/employees-page")
def employees_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("employees.html", {"request": request, "employees": db.query(model.Employee).all()})

@app.get("/expenses-page")
def expenses_page(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("expenses.html", {"request": request, "expenses": db.query(model.Expense).all()})

# --- Form Handlers ---
@app.post("/submit-class")
def submit_class(class_name: str = Form(...), monthly_tuition_fee: float = Form(...), db: Session = Depends(get_db)):
    db.add(model.ClassGrade(class_name=class_name, monthly_tuition_fee=monthly_tuition_fee))
    db.commit()
    return RedirectResponse(url="/classes-page", status_code=303)

@app.post("/submit-student")
def submit_student(first_name: str = Form(...), last_name: str = Form(...), roll_number: str = Form(...), class_id: int = Form(...), db: Session = Depends(get_db)):
    db.add(model.Student(first_name=first_name, last_name=last_name, roll_number=roll_number, class_id=class_id))
    db.commit()
    return RedirectResponse(url="/students-page", status_code=303)

@app.post("/submit-fee")
def submit_fee(student_id: int = Form(...), month: str = Form(...), amount: float = Form(...), due_date: str = Form(...), status: str = Form(...), db: Session = Depends(get_db)):
    parsed_date = datetime.strptime(due_date, "%Y-%m-%d").date()
    db.add(model.FeeInvoice(student_id=student_id, month=month, total_amount=amount, due_date=parsed_date, status=status))
    db.commit()
    return RedirectResponse(url="/receive-fee-page", status_code=303)

@app.post("/submit-employee")
def submit_employee(
    name: str = Form(...),
    contact_number: str = Form(...),
    designation: str = Form(...),
    basic_salary: float = Form(...),
    db: Session = Depends(get_db)
):

    new_employee = model.Employee(
        name=name,
        contact_number=contact_number,
        designation=designation,
        basic_salary=basic_salary
    )
    db.add(new_employee)
    db.commit()
    return RedirectResponse(url="/employees-page", status_code=303)

@app.post("/submit-expense")
def submit_expense(category_id: int = Form(...), description: str = Form(...), amount: float = Form(...), db: Session = Depends(get_db)):
    db.add(model.Expense(category_id=category_id, description=description, amount=amount))
    db.commit()
    return RedirectResponse(url="/expenses-page", status_code=303)