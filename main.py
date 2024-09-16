from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"output":""})

@app.post("/calculate",response_class=HTMLResponse)
async def calculate_output(
    request: Request,
    geography: str = Form(...),
    age: int = Form(...),
    gender: str = Form(...),
    tenure: int = Form(...),
    numOfProducts: int = Form(...),
    hasCrCard: int = Form(...),
    isActiveMember: int = Form(...),
    creditScore: int = Form(...),
    estimatedSalary: float = Form(...),
    balance: float = Form(...)):
    output = "left"
    return templates.TemplateResponse("index.html", {"request": request, "output": output })