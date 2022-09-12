from DefinitionSearcher import * 
import requests
import json
import sys, getopt


from config import *

def main(argv):
    language = 'en'
    word_id = 'dog'

    inputfile = ""
    outputfile = ""

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print("DefinitionSearcher.py -i <inputfile> -o <outputfile>")
        sys.exit(2)
    
    for opt, arg in opts:
        # -h = help
        if opt == '-h':
            print("DefinitionSearcher.py -i <inputfile> -o <outputfile>")
            sys.exit()
        # -i = input
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        # -o = output
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    interpreter = FileInterpreter(inputfile, outputfile)

    

    # url = f"{API_BASEURL}/entries/{language}/{word_id}"

    # r = requests.get(url, headers = {'app_id': API_ID, 'app_key': API_KEY})

    # json_output = json.loads(r.text)

    # print(json_output)

    # print("Definition:", json_output["results"]["lexicalEntries"][""])

if __name__ == "__main__":
    # main(sys.argv)
    main(sys.argv[1:])
