import requests
from requests.exceptions import HTTPError

# GET request 1
response = requests.get("https://www.decozy.com.sg/keyboxcall_affa.php")
print(type(response))  # instance of 'requests.models.Response' class
print(response)        # show returned status code, e.g. 200


# GET request 2
response = requests.get('https://api.github.com')
if response.status_code == 200:
    print('Success!')
elif response.status_code == 404:
    print('Not Found.')


# if status_code is between 200 to 400, 'response' is True!
if response:
    print('Success!')
else:
    print('An error has occurred.')


# raise exception when unsuccessful
for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)

        # If the response was successful, no Exception will be raised
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
        print('Success!')

