from fastapi import FastAPI
import uvicorn
from fastapi.staticfiles import StaticFiles

from routes import main_page as main_page_router 
from routes import auth as auth_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_page_router.router, prefix="/main", tags=["main"])
app.include_router(auth_router.router, prefix="/auth", tags=["auth"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

'''
Запус приложения 
    uvicorn main:app --reload


FastAPI — бэкенд

SQLite + SqlAlchemy — база данных

Jinja2 шаблоны + Bootstrap — фронтенд

(опционально) HTMX или Alpine.js — для динамичности без SPA


app/
├── routes/
│   └── auth.py         ← маршруты (FastAPI роуты)
├── services/
│   └── auth_service.py ← логика (валидация пароля, регистрация)
├── models/
│   └── user.py         ← модели SQLAlchemy или Pydantic
├── schemas/
│   └── user_schema.py  ← Pydantic-схемы для входных/выходных данных
├── database/
│   ├── db.py          ← Файл базы данных (SQLAlchemy)
│   └── create_db.py    ← Файл для создания базы данных и таблиц
├── templates/          ← HTML-шаблоны (Jinja2)
├── static/            ← Статические файлы (CSS, JS, изображения)
├── main.py            ← Главный файл приложения (FastAPI)
├── crud/
│   ├── user.py          ←  Crud операции (создание, чтение, обновление, удаление) для пользователей
│   
'''