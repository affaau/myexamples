import requests

response = requests.post('https://httpbin.org/post', json={'key':'value'})

print(response.request.headers['Content-Type'])
# application/json

print(response.request.url)
# https://httpbin.org/post

print(response.request.body)
# b'{"key": "value"}'
