from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from routes import templates

from services.auth_service import register_user, login_user
from services.jwt_handler import create_access_token, decode_token

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
    
    try: 
        await register_user(username, password)
        # jwt выдача токена если логин и пароль верные
        access_token = create_access_token(data={"sub": username})
        
        redirect = RedirectResponse(url="/", status_code=303)
        redirect.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,  # Защита от JS
            max_age=1800,
            path="/main",
            samesite="lax",
        )
        return redirect
    
    except ValueError as e:
        return templates.TemplateResponse("register.html", {"request": request, "error": str(e)})
    
    
    #return templates.TemplateResponse("welcome.html", {"request": request})