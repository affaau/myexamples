import requests

# Search GitHub's repositories for requests
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'})

print(response)

j = response.json()
for key in j.keys():
	print(f'{key}')

print(j['total_count'])
print(j['incomplete_results'])

# Inspect some attributes of the `requests` repository
repository = j['items'][0]
print(f'Repository name: {repository["name"]}')  # Python 3.6+
print(f'Repository description: {repository["description"]}')  # Python 3.6+


# alternative, pass the values as bytes
reponse = requests.get(
	'https://api.github.com/search/repositories',
	params=b'q=requests+language:python')

print(response)