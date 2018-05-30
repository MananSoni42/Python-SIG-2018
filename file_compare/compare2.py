#!/usr/bin/python3

import sys

if len(sys.argv)!= 4:
    print("Usage: ./compare2.py inFile1 inFile2 OutFile")
    sys.exit(1)

arg1 = open(sys.argv[1], 'r')
arg2 = open(sys.argv[2], 'r')
arg3 = open(sys.argv[3], 'w')

#open all 3 files simultaneously
with arg1 as in1, arg2 as in2, arg3 as out:

    #read all data at once in data1,data2
    #remove all newline characters from each sentence
    #some sentences have them while some don't
    data1 = [ s.rstrip('\r\n') for s in in1.readlines() ]
    data2 = [ s.rstrip('\r\n') for s in in2.readlines() ]
    out_arr = []

    #case 1 - file2 has more(or equal) lines than file1
    if len(data2) >= len(data1):
        #go through file1 line by line
        for i in range(len(data1)):
            #if data2[i] == data1[i]:
            #    out_arr.append(data1[i])
            # if ith line in file1 and not in file2 add '- ' prefix
            if data1[i] not in data2[i]:
                out_arr.append('- ' + data1[i])
            # if ith line not in file1 and in file2 add '- ' prefix
            if data2[i] not in data1[i]:
                out_arr.append('+ ' + data2[i])
        #write all extra lines of fle2 with a '+ ' prefix
        for i in range(len(data2)-len(data1)):
            out_arr.append('+ ' + data2[i])

    if len(data2) < len(data1):
        for i in range(len(data2)):
            #if data2[i] == data1[i]:
            #   out_arr.append(data1[i])
            # if ith line in file1 and not in file2 add '- ' prefix
            if data1[i] not in data2[i]:
                out_arr.append('- ' + data1[i])
            # if ith line not in file1 and in file2 add '- ' prefix
            if data2[i] not in data1[i]:
                out_arr.append('+ ' + data2[i])

    #write out_arr line by line along with a newline
    for line in out_arr:
        if line != '\n':
            out.write(line.rstrip('\r\n')+'\n')
