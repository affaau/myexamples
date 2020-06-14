import requests

response = requests.get("https://api.github.com")

# .content gives you RAW content
#print(response.content)        # bytes type

# convert to string, e.g. using UTF-8 encoding
# requests will try to guess the encoding based on the response’s headers
#print(response.text)           # str type

# alternatively, explicitly set encoding method
response.encoding = "utf-8"
print(response.text, '\n')

# response.text is actually serialized JSON content
# .json() convert to dictionary
j = response.json()             # dict type
for key in j.keys():
    print(f'{key}')

