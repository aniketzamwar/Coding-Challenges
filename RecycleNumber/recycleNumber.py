#!/usr/bin/python

import sys

if len(sys.argv) != 2:
    print "Please pass command Line argument to run the program: python file.py inputFilename"
    sys.exit()

try:
    f = open(sys.argv[1],'r')
    count = int(f.readline())
except IOError:
    print "Input File Could not be opened"
    sys.exit()

i = 1

while True:
    
    line = f.readline()
    if not line:
        break
    (A,B) = line.split(' ')

    intB = int(B)
    intA = int(A)
    myans = 0

    while intA < intB:
    
        A = str(intA)
        A = A[-1] + A[0:len(A)-1]
        mystr = str(A)
        val = int(mystr) 

        while val != intA:
            if val > intA and val <= intB:
                myans = myans + 1
            A = A[-1] + A[0:len(A)-1]
            mystr = str(A)
            val = int(mystr)

        intA = intA + 1

    print "Case #%d: %d" % (i,myans)
    i = i + 1

f.close()
