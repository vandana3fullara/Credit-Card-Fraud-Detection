# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 01:29:14 2022

@author: Dell
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Time : float
    V1 : float
    V2 : float
    V3 : float
    V4 : float
    V5 : float
    V6 : float
    V7 : float
    V8 : float
    V9 : float
    V10 : float
    V11 : float
    V12 : float
    V13 : float
    V14 : float
    V15 : float
    V16 : float
    V17 : float
    V18 : float
    V19 : float
    V20 : float
    V21 : float
    V22 : float
    V23 : float
    V24 : float
    V25 : float
    V26 : float
    V27 : float
    V28 : float
    Amount : float
    
# Loading The Saved Model
trained_model = pickle.load(open('trained_model.sav', 'rb'))

@app.post('/fraudulent_prediction')
def fraudulent_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    Time = input_dictionary['Time']
    V1 = input_dictionary['V1']
    V2 = input_dictionary['V2']
    V3 = input_dictionary['V3']
    V4 = input_dictionary['V4']
    V5 = input_dictionary['V5']
    V6 = input_dictionary['V6']
    V7 = input_dictionary['V7']
    V8 = input_dictionary['V8']
    V9 = input_dictionary['V9']
    V10 = input_dictionary['V10']
    V11 = input_dictionary['V11']
    V12 = input_dictionary['V12']
    V13 = input_dictionary['V13']
    V14 = input_dictionary['V14']
    V15 = input_dictionary['V15']
    V16 = input_dictionary['V16']
    V17 = input_dictionary['V17']
    V18 = input_dictionary['V18']
    V19 = input_dictionary['V19']
    V20 = input_dictionary['V20']
    V21 = input_dictionary['V21']
    V22 = input_dictionary['V22']
    V23 = input_dictionary['V23']
    V24 = input_dictionary['V24']
    V25 = input_dictionary['V25']
    V26 = input_dictionary['V26']
    V27 = input_dictionary['V27']
    V28 = input_dictionary['V28']
    Amount = input_dictionary['Amount']
    
    input_list = [Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, V11, V12, V13, V14, V15, V16, V17, V18, V19, V20, V21, V22, V23, V24, V25, V26, V27, V28, Amount]
    
    prediction = trained_model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'The Transaction Is Not Fraudulent'
    else:
        return 'The Transaction Is Fraudulent'