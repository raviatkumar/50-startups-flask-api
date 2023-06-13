import requests, json

url = 'http://0.0.0.0:5000/api/'

data = [[165349.20,136897.80,471784.10,192261.83]]

j_data = json.dumps(data)

headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}

r = requests.post(url, data=j_data, headers=headers)

print(r,r.text)