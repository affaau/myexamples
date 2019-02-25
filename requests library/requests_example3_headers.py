import requests

response = requests.get("https://api.github.com")

# instance of 'requests.structures.CaseInsensitiveDict' class
# dictionary like object, allow to access values by keys
headers = response.headers

for key in headers.keys():
    print(f'{key} : {headers[key]}')

# 'content-type'    content type of payload

