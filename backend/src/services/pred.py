import pandas as pd
import joblib

from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent.parent / "model" / "model.pkl"
model = joblib.load(MODEL_PATH)

def pred(f1, f2):
    input = [[f1, f2]]
    df_input = pd.DataFrame(input, columns = ['ds', 'y'])
    pred = model.predict(df_input)
    pred['yhat_lower'] = pred['yhat_lower'].apply(lambda x: max(0, x)) 
    result_value = float(pred['yhat'].iloc[0])
  
    return result_value*29
    