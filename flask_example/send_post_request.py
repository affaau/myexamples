'''Test flask server
It works in localhost server (flask_app.py) in Windows

After server is started, then run this client,
$ python send_poset_request.py
'''

import requests
import json

url  = 'https://affaau.pythonanywhere.com/'
#url  = 'http://127.0.0.1:5000/'
payload = {'propertyId': '689686RmA', 'secretKey': 'spacem@p36o'}
headers = {'Content-Type': 'application/json'}

# POST
r = requests.post(url, headers=headers, data=json.dumps(payload))
print(r.text)

# GET
r = requests.get(url)
print(r.text)
