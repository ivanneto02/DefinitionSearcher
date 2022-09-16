import DefinitionSearcher
import requests
import json

from .config import *

def main():
    language = 'en'
    word_id = 'dog'

    url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/' + language + '/' + word_id.lower()

    r = requests.get(url, headers = {'app_id': app_id, 'app_key': app_key})

if __name__ == "__main__":
    main()