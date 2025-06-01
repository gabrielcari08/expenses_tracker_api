from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
from db.models import User, Expense
from db import models
from db.database import SessionLocal
from auth.deps import get_current_user
from db.schemas import ExpenseResponse, ExpenseCreate

router = APIRouter(prefix="/expenses", tags=["expenses"])

#Maneja la creacion de la sesion de la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ExpenseResponse])
async def list_expenses(current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    
    expenses = db.query(Expense).filter(Expense.owner_id == current_user.id).all()
        
    return expenses
    
@router.post("/create_expense")
async def create_expense(expense_data: ExpenseCreate,
                        current_user: User = Depends(get_current_user),
                        db: Session = Depends(get_db)):
    
    expense = models.Expense(
        amount = expense_data.amount,
        description = expense_data.description,
        category = expense_data.category,
        date = expense_data.date,
        owner_id = current_user.id
    )
    
    db.add(expense)
    db.commit()
    db.refresh(expense)
    
    return {"message": "Gasto creado con exito!"}

@router.put("/update_expense/{expense_id}", response_model=ExpenseResponse)
async def update_expense(expense_id: int,
                   expense_update: ExpenseCreate,
                   db: Session = Depends(get_db),
                   current_user: User = Depends(get_current_user)):
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    
    if not expense:
        raise HTTPException(status_code=404, detail="Gasto no encontrado")
    
    if expense.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="No tenes permiso para modificar este gasto")
    
    expense.amount = expense_update.amount
    expense.description = expense_update.description
    expense.category = expense_update.category
    
    db.commit()
    db.refresh(expense)
    
    return expense

@router.delete("/delete_expense/{expense_id}")
async def delete_expense(expense_id: int,
                   db: Session = Depends(get_db),
                   current_user : User = Depends(get_current_user)):
    
    expense = db.query(Expense).filter(Expense.id == expense_id).first()
    
    if not expense:
        raise HTTPException(status_code=404, detail="Gasto no enconrado")
    
    if expense.owner_id != current_user.id:
        raise HTTPException(status_code=403, detail="No tienes permiso para eliminar este gasto")
    
    db.delete(expense)
    db.commit()
    
    return {"message": "Gasto eliminado con exito!"}
    
#Lo ultimo que se hizo fue corregir en la linea 24 all por first, esto estaba causando un error 500
#Que hay que hacer ahora: 
#- Hay que seguir creando el crud de expenses (falta, update y delete)
#- Luego de que todo sirva commitear los cambios y subirlos a la rama test
#- El paso que sigue despues de completar esto es hacer el filtrado que pide la consigna.