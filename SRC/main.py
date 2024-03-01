from typing import Annotated
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from convert import contacts

app = FastAPI()
templates = Jinja2Templates(directory="templates")

#No volver a poner @app.mount
app.mount("/static", StaticFiles(directory="static"), name = "Static")


@app.get("/Home", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("INDEX.HTML", {"request": request})


@app.get("/Home/About", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("ABOUT.HTML", {"request": request})


@app.get("/Home/Proyects", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("PROYECTS.HTML", {"request": request})


@app.get("/Home/Skills", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("TECNOLOGIES.HTML", {"request": request})


@app.get("/Home/Tecnologies", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("SKILLS.HTML", {"request": request})


@app.get("/Home/Contact", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("CONTACT.HTML", {"request": request})


@app.post("/Home/Contact/Form")
async def contact(request:Request, name: Annotated[str, Form()], email: Annotated[str, Form()], message: Annotated[str, Form()]):
    data = {"name":name,"email":email,"message":message}
    contacts(data)
    return templates.TemplateResponse("response.html", {"request": request})