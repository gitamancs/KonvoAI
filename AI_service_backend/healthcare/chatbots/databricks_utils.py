import requests
import json
import os

def score_model(dataset):
    url = "https://adb-673140172341602.2.azuredatabricks.net/serving-endpoints/healthfaqs/invocations"
    token ="dapi3953314a508e65d3e4166746312f9196-3"
    headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
    data_json = json.dumps({'inputs': dataset})
    response = requests.post(url, headers=headers, data=data_json)
    if response.status_code != 200:
        raise Exception(f'Request failed with status {response.status_code}, {response.text}')
    return response.json()