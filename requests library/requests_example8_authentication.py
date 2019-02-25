import requests
from getpass import getpass

response = requests.get('https://api.github.com/user', auth=('affaau', getpass()))

print(response)
j = response.json()
for key in j.keys():
	print(f'{key} : {j[key]}')

print('\n\n\n')
# reuests actually applying HTTP basic access authentication
# explicitly use it, output same result
#
# there are otherauthenication methods like
# HTTPDigestAuth and HTTPProxyAuth
#
from requests.auth import HTTPBasicAuth

response = requests.get(
	'https://api.github.com/user',
	auth=HTTPBasicAuth('affaau', getpass())
	)
print(response)
j = response.json()
for key in j.keys():
	print(f'{key} : {j[key]}')

#
# github read only token
# 2a614471d6827ddcc35ba75d923deb007885c4e6
#
from requests.auth import AuthBase

read_only_token = '2a614471d6827ddcc35ba75d923deb007885c4e6'

class TokenAuth(AuthBase):
    """Implements a custom authentication scheme."""

    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        """Attach an API token to a custom auth header."""
        r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
        return r

print('\n\n\n')
response = requests.get('https://httpbin.org/get', auth=TokenAuth(read_only_token))

print(response)
j = response.json()

for key in j.keys():
	if key != 'headers':
		print(f'{key} : {j[key]}')
	else:
		for k in j['headers'].keys():
			print("{} : {}".format(k, j['headers'][k]))

#
# The way that you communicate with secure sites over HTTP is by
# establishing an encrypted connection using SSL, which means that
# verifying the target server’s SSL Certificate is critical
# 'requests' does this by default
#

# in case, want to disable SSL certificate verification
# pass False to the verify 
print(requests.get('https://api.github.com', verify=False))
