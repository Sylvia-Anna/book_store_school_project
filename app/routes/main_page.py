from fastapi import Path, Query, Request, APIRouter, Depends
from fastapi.responses import HTMLResponse

from routes import templates
from services.jwt_handler import decode_token

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request, username: str = Depends(decode_token)):
    return templates.TemplateResponse("main.html", {"request": request, "username": username})

