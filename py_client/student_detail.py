from pprint import pprint

import requests

student_id = input('Введите id студента \n')

try:
    student_id = int(student_id)
except TypeError:
    student_id = None
    print(f'{student_id} - неверный тип значения')

if student_id:
    endpoint = f'http://127.0.0.1:8000/api/v1/students/{student_id}/'


get_response = requests.get(endpoint)
if get_response.headers['content-type'] == 'application/json':
    data = get_response.json()
    pprint(data, sort_dicts=False)
else:
    print('Response is not valid JSON')
