import requests
import json

class DefSearcher:
    def __init__(
        self,
        language="en-us",
        words=list(),
        API_BASEURL="none",
        API_ID="none",
        API_KEY="none"
    ):
        self.language = language
        # remove duplicates and convert back to clean list
        self.words = [ word.lower().strip() for word in list(set(words)) ]
        self.API_BASEURL = API_BASEURL
        self.API_ID = API_ID
        self.API_KEY = API_KEY
        self.json_list = []
    
    def search(self):
        # iterate through all the words, call API to grab the word
        for i in range(0, len(self.words)):
            url = f"{self.API_BASEURL}/entries/{self.language}/{self.words[i]}"
            r = requests.get(url, headers = {'app_id': self.API_ID, 'app_key': self.API_KEY})
            self.json_list.append(r.text)