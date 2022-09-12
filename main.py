import DefinitionSearcher
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

    ### IF SUCCESSFULLY GOT INPUT/OUTPUT FILE FROM COMMANDLINE
    if len(inputfile) > 0:
        while not os.path.exists(inputfile): 
            print("Input file is not valid. Please try again. ")
            inputfile = input("Input file: ")
    if len(outputfile) > 0:
        while os.path.exists(outputfile): 
            print("Output file already exists. Override? y/n")
            output_bool = input() 
            if output_bool == "y": 
                break
            else: 
                outputfile = input("Output file: ")

    ### IF INPUTFILE OR OUTPUT FILE ARE NOT GIVEN 
    if len(inputfile) == 0:
        inputfile = input("Input file: ")
        while not os.path.exists(inputfile): 
            print("Input file is not valid. Please try again. ")
            inputfile = input("Input file: ")
    if len(outputfile) == 0:
        outputfile = input("Output file: ")
        while os.path.exists(outputfile): 
            print("Output file already exists. Override? y/n")
            output_bool = input() 
            if output_bool == "y": 
                break
            else: 
                outputfile = input("Output file: ")
    
    print("Input file is", inputfile)
    print("Output file is", outputfile)

    with open(inputfile) as f: 
        lines = [line.strip() for line in f.readlines()]

    print(lines) 

    # url = f"{API_BASEURL}/entries/{language}/{word_id}"

    # r = requests.get(url, headers = {'app_id': API_ID, 'app_key': API_KEY})

    # json_output = json.loads(r.text)

    # print(json_output)

    # print("Definition:", json_output["results"]["lexicalEntries"][""])

if __name__ == "__main__":
    main(sys.argv[1:])
