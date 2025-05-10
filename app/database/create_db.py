# Файл для создания базы данных SQLite и таблиц
from db import Base, engine

# Создание всех таблиц в базе
Base.metadata.create_all(bind=engine)