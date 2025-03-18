import os
import requests
import json

http_url="https://random-word-api.herokuapp.com/word"

try:
    res= requests.get(http_url)
    res.raise_for_status()
    print(f"{res.status_code} - {res.reason}")
    words = json.loads(res.text)

    for w in words:
        print(w)

except requests.exceptions.RequestException as ops:
    print(f"Error getting data from {http_url} : {ops}")
