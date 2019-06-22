#import regex for string manipulation
import re

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
    print(output)

#this function reads a file and separates by new line into an array
def read_file(file_name):
    F = open(file_name, "r") 
    temp = F.readlines() 
    F.close()
    return temp

#variables used
file_name = "input.txt"
unwanted_chars = "[\"!?,.]"
histograph = {}
max_len = 0

#read file
lines=read_file(file_name)

#this outer loop looks at every line/string in the array and removes unwanted characters then splits 
#by a default delimiter of SPACE to get the SPACE seperated words
for line in lines:
    line = re.sub(unwanted_chars,"",line ).lower().split()
    #the inner loop finds longest word and also inputs words into dictionary
    #along with corresponding frequency
    for word in line:
        if len(word)>max_len:
            max_len = len(word)
        if word in histograph:
            histograph[word]+=1
        else:
            histograph[word] = 1

max_len = str(max_len)

#sort the dictionary by value then print
for word in sorted(histograph, key=histograph.get, reverse=True):
    proper_print(word,histograph,max_len)
