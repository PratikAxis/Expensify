import pandas as pd
import numpy as np
from prophet import Prophet
import joblib
from pathlib import Path

file_path = Path('model.pkl')

if file_path.is_file():
    print(f"file path {file_path} already exist")

else:
    df_raw = pd.read_csv('/home/pratik/ML and DL projects/expense-predictor/backend/configs/data/student_expenses.csv')
    df = df_raw.drop(['Notes', 'Type', 'Category'], axis=1)
    
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.set_index('Date').resample('D').sum().fillna(0).reset_index() 
      
    df = df.rename(columns={'Date': 'ds', 'Amount': 'y'})

    model = Prophet(interval_width=0.5)
    model.fit(df)

    joblib.dump(model, '/main/backend/src/model/model.pkl')

    
