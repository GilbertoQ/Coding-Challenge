#import regex for string manipulation
import re

#this function writes an array of strings to a file
def write_file(file_name,lines):
    with open(file_name,"w") as F:
        for line in lines:
            F.write(line+'\n')

#function to print predefined right aligned format
def proper_print(word,histograph,max_len):
    r_align = "{0:>"+max_len+"}"
    output = ""
    output += r_align.format(word)
    output += " | "
    for i in range(histograph[word]):
        output += "="
    output += " ("
    output += str(histograph[word])
    output += ")"
    return output

#this function reads a file and separates by new line into an array
def read_file(file_name):
    with open(file_name, "r") as F:
        temp = F.readlines() 
    return temp

def create_histograph(lines,unwanted_chars,histograph,max_len):
    #this outer loop looks at every line/string in the array and removes unwanted characters then splits 
    #by a default delimiter of SPACE to get the SPACE seperated words
    for line in lines:
        line = re.sub(unwanted_chars,"",line ).lower().split()
        #the inner loop finds the longest word and also inputs words into dictionary
        #along with corresponding frequency
        for word in line:
            if len(word)>max_len:
                max_len = len(word)
            if word in histograph:
                histograph[word]+=1
            else:
                histograph[word] = 1

    max_len = str(max_len+1)
    return histograph,max_len

def main():
    #variables used
    infile_name = "input.txt"
    outfile_name = "output.txt"
    unwanted_chars = "[\"!?,.]"
    histograph = {}
    max_len = 0
    output = []

    #read file
    lines=read_file(infile_name)

    #create histograph
    histograph,max_len = create_histograph(lines,unwanted_chars,histograph,max_len )

    #sort the dictionary by value then create proper string for output
    for word in sorted(histograph, key=histograph.get, reverse=True):
        output.append(proper_print(word,histograph,max_len))

    #write to file
    write_file(outfile_name,output)

if __name__ == "__main__":
    main()