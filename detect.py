import requests
# pprint is used to format the JSON response
from pprint import pprint

import os

subscription_key = "d4adcdc709a24e5fb4ec1e7b0cef7f17"
endpoint = "https://api.cognitive.microsofttranslator.com"

language_api_url = endpoint + "/text/analytics/v2.1/languages"

documents = {"documents": [
    {"id": "1", "text": "This is a document written in English."},
    {"id": "2", "text": "Este es un document escrito en Español."},
    {"id": "3", "text": "这是一个用中文写的文件"}
]}

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=documents)
languages = response.json()
pprint(languages)
