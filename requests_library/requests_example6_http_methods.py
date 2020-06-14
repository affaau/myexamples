import requests

# print(requests.post('https://httpbin.org/post', data={'key':'value'}))
# print(requests.put('https://httpbin.org/put', data={'key':'value'}))
# print(requests.delete('https://httpbin.org/delete'))
# print(requests.head('https://httpbin.org/get'))
# print(requests.patch('https://httpbin.org/patch', data={'key':'value'}))
# print(requests.options('https://httpbin.org/get'))

# General post data
response = requests.post('https://httpbin.org/post', data={'key':'value'})
print(response.text)
'''
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "key": "value"
  },
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "9",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.21.0"
  },
  "json": null,
  "origin": "115.66.157.180",
  "url": "https://httpbin.org/post"
}
'''

# To send JSON data, you can use the json parameter. When you pass JSON 
# data via json, requests will serialize your data and add the correct 
# Content-Type header for you.
response = requests.post('https://httpbin.org/post', json={'key':'value'})
json_response = response.json()
print(json_response['data'])
print(json_response['headers']['Content-Type'])

print(response.text)
'''
{
  "args": {},
  "data": "{\"key\": \"value\"}",
  "files": {},
  "form": {},
  "headers": {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "close",
    "Content-Length": "16",
    "Content-Type": "application/json",
    "Host": "httpbin.org",
    "User-Agent": "python-requests/2.21.0"
  },
  "json": {
    "key": "value"
  },
  "origin": "115.66.157.180",
  "url": "https://httpbin.org/post"
}
'''