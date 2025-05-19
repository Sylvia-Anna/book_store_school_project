from crud.user import check_user_exists, create_user
from models.user import User
from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def register_user(username: str, password: str) -> ValueError | None:
    '''Регистрация пользователя'''
    user_exists: bool = check_user_exists(username)
    
    if user_exists:
        raise ValueError("Пользователь с таким именем уже существует")
    else:
        hashed_password = pwd_context.hash(password)
        new_user = create_user(username, hashed_password)

async def login_user(username: str, password: str) -> User:
    '''Авторизация пользователя'''
    ...


# Проверка что такой пользователь не существует
# Хэширование пароля
# Сохранение пользователя в базе данных