import requests
import json
<<<<<<< HEAD
import os

def score_model(dataset):
    url = "https://adb-673140172341602.2.azuredatabricks.net/serving-endpoints/healthfaqs/invocations"
    token ="dapi3953314a508e65d3e4166746312f9196-3"
=======

def score_model(dataset):
    url = "https://adb-673140172341602.2.azuredatabricks.net/serving-endpoints/healthfaqs/invocations"
    token = "dapi3953314a508e65d3e4166746312f9196-3"
>>>>>>> 5e777a4 (commit)
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data_json = json.dumps({'inputs': dataset})
    response = requests.post(url, headers=headers, data=data_json)
    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}, {response.text}')
<<<<<<< HEAD
    return response.json()
=======
    response_json = response.json()
    print("Databricks raw response:", response_json)  # Debug log
    return response_json
>>>>>>> 5e777a4 (commit)
