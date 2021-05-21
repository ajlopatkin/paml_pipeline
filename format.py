# @author Emily Huntsman
# @date 12/8/20

# feel free to ignore this file, it was to create a usable textfile based on the conventions we discussed at the beginning of the year
# I don't think it's really necessary given what we ended up doing later down the line but I wanted to include it anyway

import os, sys

# grabs the file name from a command line arg
# if the file is ire1.fa, run the program as python3 format.py ire1.fa
# this will generate an output file of ire1.txt with the correct formatting
file_name = sys.argv[1][:-3]

original = open(sys.argv[1])
data = original.readlines()
os.remove(sys.argv[1])
original.close()

# read in lines, remove ">" characters, add new lines where appropriate
new = open("intermediate.txt","w")
formatted_fa = open(sys.argv[1],"w")
illegal_char = [":", ",", ")", "(", ";", "]", "[", "'"]
count = 0
nt = 0

for i in data:
    if i.startswith(">"):
        #i = i.replace(" ","_")
        i = (''.join(j for j in i if not j in illegal_char)).replace(" ","_")
        # keeping track of the total number of snippets
        count+=1
        new.write("\n")
        for char in i:
            # skips ahead if unnecessary species info is included
            if (char == ":"):
                new.write("\n")
                break
            elif (char != ">"):
                new.write(char)
        formatted_fa.write(i)
    else:
        # counts the number of nucleotides/AA in each block
        if (count == 1):
            for char in i:
                if (char != "\n"):
                    nt+=1
        new.write(i)
        formatted_fa.write(i)
new.close()
formatted_fa.close()

# reads in reformatted data
pre_header = open("intermediate.txt")
formatted_data = pre_header.read()
pre_header.close()

# creates final file with the name specified in command line
final = open(f'{file_name}.txt',"w")
# adds necessary header with species count and nucleotides
final.write("  "+str(count)+"   "+str(nt)+"\n")
final.write(formatted_data)
final.close()

# deletes intermediate textfile from directory
os.remove("intermediate.txt")