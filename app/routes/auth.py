from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from routes import templates

router = APIRouter()

@router.get("/login", response_class=HTMLResponse)
async def login_page(request: Request):
    '''Отображение формы входа в аккаунт'''
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login", response_class=HTMLResponse, name="login")
async def login(request: Request):
    '''Обработка формы входа в аккаунт'''
    form = await request.form()
    username = form.get("email")
    password = form.get("password")
    
    # jwt выдача токена если логин и пароль верные
    
    # if username == "admin" and password == "password":
    #     return templates.TemplateResponse("welcome.html", {"request": request, "username": username})
    
    return templates.TemplateResponse("login.html", {"request": request})


@router.get("/register", response_class=HTMLResponse)
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.post("/register", response_class=HTMLResponse, name="register")
async def register(request: Request):
    form = await request.form()
    username = form.get("username")
    password = form.get("password")
    
    # Здесь должна быть логика регистрации пользователя
    # Например, сохранение пользователя в базе данных
    
    return templates.TemplateResponse("welcome.html", {"request": request})