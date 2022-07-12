# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 18:43:13 2022

@author: Dell
"""

import json
import requests

url = 'http://127.0.0.1:8000/fraudulent_prediction'

input_data_for_model = {
    
    'Time' : 4,
    'V1' : 1.22965763450793,
    'V2' : 0.141003507049326,
    'V3' : 0.0453707735899449,
    'V4' : 1.20261273673594,
    'V5' : 0.191880988597645,
    'V6' : 0.272708122899098,
    'V7' : -0.00515900288250983,
    'V8' : 0.0812129398830894,
    'V9' : 0.464959994783886,
    'V10' : -0.0992543211289237,
    'V11' : -1.41690724314928,
    'V12' : -0.153825826253651,
    'V13' : -0.75106271556262,
    'V14' : 0.16737196252175,
    'V15' : 0.0501435942254188,
    'V16' : -0.443586797916727,
    'V17' : 0.00282051247234708,
    'V18' : -0.61198733994012,
    'V19' : -0.0455750446637976,
    'V20' : -0.21963255278686,
    'V21' : -0.167716265815783,
    'V22' : -0.270709726172363,
    'V23' : -0.154103786809305,
    'V24' : -0.780055415004671,
    'V25' : 0.75013693580659,
    'V26' : -0.257236845917139,
    'V27' : 0.0345074297438413,
    'V28' : 0.00516776890624916,
    'Amount' : 4.99
     
    }

input_json = json.dumps(input_data_for_model)

response = requests.post(url, data=input_json)

print(response.text)