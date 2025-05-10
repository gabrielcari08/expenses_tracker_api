#Este archivo define los esquemas (modelos) de entrada y salida para las rutas de la API.

from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

#Clase que define el esquema para la creacion de usuario.
class UserCreate(BaseModel):
    username: str
    password: str

#Clase que define el esquema la devolucion de usuario.
class UserResponse(BaseModel):
    id: int
    username: str
    
    class Config:
        orm_mode = True
        
#Clase que define el esquema de lo que se le pedira a un usuario cuando inicie sesion.
class UserLogin(UserCreate):
    pass
        
#Clase que define el esquema base de un gasto.
class ExpenseBase(BaseModel):
    amount: int
    description: str
    category: str
    date: Optional[datetime] = None

#Clase que define el esquema de creacion de un gasto (hereda de ExpenseBase).
class ExpenseCreate(ExpenseBase):
    pass

#Clase que define el esquema de actualizacion de un gasto (hereda de ExpenseBase).
class ExpenseUpdate(ExpenseBase):
    pass

#Clase que define la devolucion de gasto.
class ExpenseResponse(ExpenseBase):
    id: int
    owner_id: int
    
    class Config:
        orm_mode = True
        
#Este esquema define cómo será la respuesta con el token  
class Token(BaseModel):
    access_token: str
    token_type: str
      
class TokenData(BaseModel):
    username: Optional[str] = None