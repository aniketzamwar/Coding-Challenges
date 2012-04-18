#!/usr/bin/python

'''Google Code Jam 2012
   Dancing Googlers
   Author: Aniket Zamwar
   email: aniketzamwar@gmail.com'''

import sys

if len(sys.argv) != 2:
    print "Please run program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File could not be opened"
    sys.exit()

if count > 100 or count <= 0:
    print "Error: Number of Test Case cannot be more than 100 or less than 1"
    sys.exit()

outcount = 1

while count > 0:

    line = f.readline() #'3 1 5 15 13 11'
    if not line:
        break
    myinput = line.split()
    del line
    values = myinput[3:]

    numofGooglers = int(myinput[0])
    surpriseCount = int(myinput[1])
    maxVal = int(myinput[2])

    del myinput

    ans = 0

    for val in values:
        val = int(val)
    
        quo = val / 3
        rem = val % 3
    
        if rem == 0:
            if quo >= maxVal:
                ans = ans + 1
            elif surpriseCount > 0 and quo > 0 and quo + 1 >= maxVal:
                ans = ans + 1
                surpriseCount = surpriseCount - 1
        elif rem == 1:
            if quo >= maxVal or quo + 1 >= maxVal:
                ans = ans + 1
            elif surpriseCount > 0 and quo + 1 >= maxVal:
                ans = ans + 1
                surpriseCount = surpriseCount - 1
        elif rem == 2:
            if quo >= maxVal or quo+ 1 >= maxVal:
                ans = ans + 1
            elif surpriseCount > 0 and quo + 2 >= maxVal:
                ans = ans + 1
                surpriseCount = surpriseCount - 1

    print "Case #" + str(outcount) + ": " + str(ans)
    outcount = outcount + 1
    count = count -1

f.close()

