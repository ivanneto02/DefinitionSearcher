import sys, getopt, os

class FileInterpreter:
    def __init__(self, inputfile, outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
        self.words = [] 
        self.input() 

    def input(self):  

        if len(self.inputfile) == 0:
            print("did not get set")
        
        ### IF SUCCESSFULLY GOT INPUT/OUTPUT FILE FROM COMMANDLINE
        if len(self.inputfile) > 0:
            while not os.path.exists(self.inputfile): 
                print("Input file is not valid. Please try again. ")
                self.inputfile = input("Input file: ")
        if len(self.outputfile) > 0:
            while os.path.exists(self.outputfile): 
                print("Output file already exists. Override? y/n")
                output_bool = input() 
                if output_bool == "y": 
                    break
                else: 
                    self.outputfile = input("Output file: ")

        ### IF INPUT FILE OR OUTPUT FILE ARE NOT GIVEN 
        if len(self.inputfile) == 0:
            self.inputfile = input("Input file: ")
            while not os.path.exists(self.inputfile): 
                print("Input file is not valid. Please try again. ")
                self.inputfile = input("Input file: ")
        if len(self.outputfile) == 0:
            self.outputfile = input("Output file: ")
            while os.path.exists(self.outputfile): 
                print("Output file already exists. Override? y/n")
                output_bool = input() 
                if output_bool == "y": 
                    break
                else: 
                    self.outputfile = input("Output file: ")
        
        print("Input file is", self.inputfile)
        print("Output file is", self.outputfile)

        with open(self.inputfile) as f: 
            lines = [line.strip() for line in f.readlines()]

        self.words = lines 


