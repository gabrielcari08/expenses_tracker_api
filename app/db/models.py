#Este archivo se encarga de definir la estructura de las tablas de la base de datos.

from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy.orm import declarative_base, relationship
from .database import engine

Base = declarative_base()

#Tabla de usuarios.
class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    expenses = relationship("Expense", back_populates="owner")
 
#Tabla de gastos.   
class Expense(Base):
    __tablename__ = "expenses"
    
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    description = Column(String)
    category = Column(String)
    date = Column(DateTime, default=datetime.utcnow)
    
    owner_id = Column(Integer, ForeignKey("user.id")) #Cambio de users.id a user.id 
    
    owner = relationship("User", back_populates="expenses")