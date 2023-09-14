import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
host = 'http://wttr.dvmn.org'
get = '/san%20francisco?nTqu&lang=en'
url = host + get

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)
response = session.get(url)
response.raise_for_status()

print(response.text)