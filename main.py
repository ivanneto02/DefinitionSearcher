import DefinitionSearcher
import requests
import json

from config import *

def main():
    language = 'en'
    word_id = 'dog'

    url = f"{API_BASEURL}/entries/{language}/{word_id}"

    r = requests.get(url, headers = {'app_id': API_ID, 'app_key': API_KEY})

    json_output = json.loads(r.text)

    print(json_output)

    print("Definition:", json_output["results"]["lexicalEntries"][""])

if __name__ == "__main__":
    main()