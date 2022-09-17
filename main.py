from DefinitionSearcher import * 
import requests
import json
import sys, getopt


from config import *

def main(argv):
    language = 'en'

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

    searcher = DefSearcher( # grab list of words and search
        language=language,
        words=interpreter.words,
        API_BASEURL=API_BASEURL,
        API_ID=API_ID,
        API_KEY=API_KEY
    )
    searcher.search()

    output = AnkiOutput(
        output_file=outputfile,
        json_out=searcher.json_list,
        max_phrases=5,
        max_syn=10
    )
    output.output()

if __name__ == "__main__":
    # main(sys.argv)
    main(sys.argv[1:])
