import requests

# By default, requests will wait indefinitely on the response,
# so you should almost always specify a timeout duration to 
# prevent these things from happening.

# set timeout in 1 seconds
print(requests.get('https://api.github.com', timeout=1))
# set timeout in 3.05 seconds
print(requests.get('https://api.github.com', timeout=3.05))

# example:
# If the request establishes a connection within 2 seconds and
# receives data within 5 seconds of the connection being established,
# then the response will be returned as it was before. If the request
# times out, then the function will raise a Timeout exception.
print(requests.get('https://api.github.com', timeout=(2, 5)))

# example:
from requests.exceptions import Timeout

try:
    response = requests.get('https://api.github.com', timeout=1)
except Timeout:
    print('The request timed out')
else:
    print('The request did not time out')
	
