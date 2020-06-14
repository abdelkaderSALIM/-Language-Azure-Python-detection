import requests
# pprint is used to format the JSON response
from pprint import pprint

import os

subscription_key = "d4adcdc709a24e5fb4ec1e7b0cef7f17"
endpoint = "https://ostextanalytics.cognitiveservices.azure.com"

language_api_url = endpoint + "/text/analytics/v2.1/languages"

with open('data.json', encoding='utf-8-sig') as json_data:
    body = json.load(json_data)

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=body)
languages = response.json()
pprint(languages)
