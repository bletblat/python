import requests

host = 'http://wttr.dvmn.org'
get = '/san%20francisco?nTqu&lang=en'
url = host + get

response = requests.get(url)
response.raise_for_status()
print(response.text)