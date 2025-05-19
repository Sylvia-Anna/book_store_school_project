from models.user import User
from database.session import session

async def check_user_exists(email: str) -> bool:
    '''Проверка существования пользователя в базе данных'''
    user = session.query(User).filter(User.email == email).first()
    return user is not None

async def create_user(email: str, password: str) -> User:
    '''Создание нового пользователя в базе данных'''
    new_user = User(email=email, password=password)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user

async def get_user_by_email(email: str) -> User:
    '''Получение пользователя по email'''
    ...