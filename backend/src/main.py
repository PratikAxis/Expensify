import joblib
import pandas as pd
from src.services.transaction import get_all_transactions, new_transaction
from src.services.pred import pred
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    
    amount: float 
    type: str
    category: str
    Date: date = Field(default_factory=date.today)
    notes: Optional[str] = None

@app.get("/transactions/view")
def transactions():
    return get_all_transactions()

@app.post("/transactions")
def add_transaction(transactions: Transaction):
    data_dict = transactions.model_dump()
    data_dict['Date'] = str(data_dict['Date'])
    new_transaction(data_dict)
    return data_dict

@app.post("/predict")
async def predict_expanse(transaction: Transaction):
    f1 = transaction.Date
    f2 = str(transaction.amount)
    result = pred(f1, f2)
    return result
