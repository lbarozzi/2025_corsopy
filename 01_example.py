import os
import tempfile
import os.path
import requests
import json
import dotenv

http_url="https://random-word-api.herokuapp.com/word"

try:
    '''
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

    with tempfile.NamedTemporaryFile(delete=True, mode="w") as tmp_file:
        for w in words:
            tmp_file.write(w + "\n")
        tmp_file.flush()
        print(f"Temp file created : {tmp_file.name}")
    '''
    mypath= os.getcwd()
    print(f"Current working directory : {mypath}")
    (head,tail)= os.path.split(f"{mypath}/")
    print(f"Head : {head} , Tail : {tail}")

    list= os.listdir(mypath)
    for l in list:
        print(l)

    # os.mkdir(f"{mypath}/tempdir")
    # os.remove("filename.txt")
    # os.rename("wordlist.txt", "wordlist.txt.lbak")

    currentpath=os.environ["PATH"]
    print(f"Current path : {currentpath}")
    
    print(f"Path separator : {os.pathsep}")
    print(f"Separator : {os.sep}")

except requests.exceptions.RequestException as ops:
    print(f"Error getting data from {http_url} : {ops}")
