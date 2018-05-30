#!/usr/bin/python3
import sys

if len(sys.argv)!= 4:
    print("Usage: ./compare1.py inFile1 inFile2 OutFile")
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
    out_arr = [] # final output stored here
    neg_ind = [] # stores indexes(out_arr) of lines in data1 but not in data2

    #add lines that are only in data1 to out_arr with a '- ' prefix
    for line in data1:
        #if line in data2:
        #    out_arr.append(line)
        if line not in data2:
            out_arr.append('- ' + line)
            neg_ind.append(len(out_arr)-1)

    #insert lines only in data2 in out_arr with a '+ ' prefix
    #count number of '- ' and add one '+ ' after each
    count = 0
    for line in data2:
        if line not in data1:
            #if correct position is not within bounds => append
            #EAFP
            try:
                out_arr.insert(neg_ind[count]+1+count,'+ ' + line)
            except IndexError:
                out_arr.append('+ ' + line)
            count+=1

    #write out_arr line by line along with a newline
    for line in out_arr:
        out.write(line+'\n')
