import os
import tempfile
import os.path
import requests
import json

http_url="https://random-word-api.herokuapp.com/word"

try:
    p={"number":"10"}
    res= requests.get(http_url, params=p)
    res.raise_for_status()

    print(f"{res.status_code} - {res.reason}")
    words = json.loads(res.text)

    for w in words:
        print(w)

    tmp_file= open("wordlist.txt", "a") # default "r" #"w" write #"x" create #"a" append
    for w in words:
        tmp_file.write(w + "\n")

    tmp_file.close()

    with tempfile.NamedTemporaryFile(delete=False, mode="w") as tmp_file:
        for w in words:
            tmp_file.write(w + "\n")
        tmp_file.flush()
        print(f"Temp file created : {tmp_file.name}")


except requests.exceptions.RequestException as ops:
    print(f"Error getting data from {http_url} : {ops}")
