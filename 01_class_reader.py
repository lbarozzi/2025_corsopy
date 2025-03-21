import os
import sys
import tempfile
import os.path
import requests
import json
import dotenv

http_url="https://random-word-api.herokuapp.com/word"

class ListReader:
    def __init__(self,filename="wordlist.txt"):
        self.filename=filename
        self.wordlist=[]
        # self.load()

    def create(self, len=20000):
        try:
            p={"number":len} 
            res= requests.get(http_url, params=p)
            res.raise_for_status()

            print(f"{res.status_code} - {res.reason}")
            words = json.loads(res.text)
            with open(self.filename, 'a') as f:
                for word in words:
                    f.write(f"{word}\n")
            
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def load(self):
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    self.wordlist.append(line.strip())

        except Exception as e:
            print(f"Error: {e}")
            return False
        
    def getUnique(self):
        # tmp_list=list(dict.fromkeys(self.wordlist))
        tmp_list = [*{*self.wordlist}]

        return (tmp_list, len(tmp_list),len(self.wordlist))
    
    def shortLong(self):
        # shortest word
        # longest word
        # mean len
        tmp_list,a,b= self.getUnique()
        tmp_list.sort(key=len)
        # print(f"Shortest: {tmp_list[0]} - {len(tmp_list[0])}")

        tot_len = sum(len(x) for x in tmp_list)
        # print(f"Mean: {tot_len/len(tmp_list)}")

        return (tmp_list[0],tmp_list[-1],tot_len/len(tmp_list))

def main():
    myobj= ListReader()
    myobj.create()
    myobj.load()
    (list,uni,all)=myobj.getUnique()
    print(f"Unique: {uni} - All: {all}")
    (short,long,mean)=myobj.shortLong()
    print(f"Shortest: {short} - Longest: {long} - Mean: {mean}")
    pass 

if __name__== "__main__":
    #Do Main loop
    main()
    print("Done")