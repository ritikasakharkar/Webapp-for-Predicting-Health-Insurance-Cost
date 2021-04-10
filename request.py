import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'age':2, 'sex':3, 'children':4})

print(r.json())