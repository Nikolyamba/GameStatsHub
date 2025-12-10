from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr, Field

from backend.database.models.user_model import User
from backend.database.session import get_db

u_router = APIRouter()

class UserRegister(BaseModel):
    login: str
    email: EmailStr
    password: Annotated[str, Field(min_length=8, max_length=128)]
    repeat_password: Annotated[str, Field(min_length=8, max_length=128)]

#TODO НАДО СДЕЛАТЬ ХЭШИРОВАНИЕ ПАРОЛЯ А ТАКЖЕ АУТЕНТИФИКАЦИЮ
@u_router.post('/register')
async def register(data: UserRegister, db = Depends(get_db)) -> dict:
    old_user = db.query(User).filter((User.login == data.login) | (User.email == data.email)).first()
    if old_user:
        raise HTTPException(status_code=400, detail='Пользователь с таким login или email уже существует!')
    new_user = User(login = data.login,
                    email = data.email,
                    password = data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {'success': True, 'user': new_user.id}