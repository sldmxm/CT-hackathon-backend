from pprint import pprint

import requests

endpoint = 'http://127.0.0.1:8000/api/v1/students/'

get_response = requests.get(endpoint)

if get_response.headers['content-type'] == 'application/json':
    data = get_response.json()
    pprint(data, sort_dicts=False)
else:
    print('Response is not valid JSON')
