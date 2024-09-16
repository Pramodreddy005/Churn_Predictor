from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import joblib 
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request,"output":""})

@app.post("/calculate",response_class=HTMLResponse)
async def calculate_output(request: Request,
    age: int = Form(...),
    geography: str = Form(...),
    gender: int = Form(...),
    tenure: int = Form(...),
    numOfProducts: int = Form(...),
    hasCrCard: int = Form(...),
    isActiveMember: int = Form(...),
    creditScore: int = Form(...),
    estimatedSalary: int = Form(...),
    balance: int = Form(...)):
    
    # Importing Model and Performing Prediction
    model=joblib.load("churn_predictor.pkl")
    '''feature_names=['Geography_Germany', 'Geography_Spain', 'Age', 'Gender', 'Tenure',
       'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'CreditScore',
       'EstimatedSalary', 'Balance']'''
    
    if geography=="France":
        x=[0,0]
    elif geography=="Germany":
        x=[1,0]
    else:
        x=[0,1]
    
    input=[[x[0],x[1],age,gender,tenure,numOfProducts,hasCrCard,isActiveMember,creditScore,estimatedSalary,balance]]
    #print(input)
    result=model.predict(input)
    if result[0]==0:
        output="Yes"
    else:
        output="No"
        
    return templates.TemplateResponse("index.html", {"request": request, "output": output })