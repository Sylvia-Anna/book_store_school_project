from fastapi import Path, Query, Request, APIRouter
from fastapi.responses import HTMLResponse

from routes import templates

router = APIRouter()

@router.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

