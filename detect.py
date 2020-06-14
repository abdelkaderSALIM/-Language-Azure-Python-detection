import requests
# pprint is used to format the JSON response
from pprint import pprint

import os, uuid, json

key_var_name = 'TRANSLATOR_TEXT_SUBSCRIPTION_KEY'
if not key_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(key_var_name))
subscription_key = os.environ[key_var_name]

endpoint_var_name = 'TRANSLATOR_TEXT_ENDPOINT'
if not endpoint_var_name in os.environ:
    raise Exception('Please set/export the environment variable: {}'.format(endpoint_var_name))
endpoint = os.environ[endpoint_var_name]

language_api_url = endpoint + "/text/analytics/v2.1/languages"

with open('data.json', encoding='utf-8-sig') as json_data:
    body = json.load(json_data)

headers = {"Ocp-Apim-Subscription-Key": subscription_key}
response = requests.post(language_api_url, headers=headers, json=body)
languages = response.json()
pprint(languages)
