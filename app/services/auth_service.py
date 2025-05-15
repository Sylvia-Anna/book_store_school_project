from crud.user import check_user_exists, create_user
from models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(username: str, password: str):
    '''Регистрация пользователя'''
    user_exists: bool = check_user_exists(username)
    if user_exists:
        raise ValueError("Пользователь с таким именем уже существует")
    else:
        hashed_password = pwd_context.hash(password)
        


# Проверка что такой пользователь не существует
# Хэширование пароля
# Сохранение пользователя в базе данных