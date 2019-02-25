import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

# When a request fails, you may want your application to retry
# the same request. However, requests will not do this for you
# by default

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use `github_adapter` for all requests to endpoints that start with
# this URL
session.mount('https://api.github.com', github_adapter)

try:
    response = session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)
	
print(type(response))    # Response class
print(response)