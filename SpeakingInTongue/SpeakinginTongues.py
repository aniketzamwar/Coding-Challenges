#!/usr/bin/python

'''Google Code Jam 2012
   Problem 1: Speaking in Tongues
   Author: Aniket Zamwar
   email: aniketzamwar@gmail.com'''

'''Output:For each test case, output one line containing "Case #X: S" where X is the case number and S is the string that becomes G in Googlerese.
   Limits: Max number of lines 30, G contains at most 100 characters, None of the text is guaranteed to be valid English.'''


import sys

myinput = 'ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv de kr kd eoya kw aej tysr re ujdr lkgc jv y e q z'

output = 'our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up so it is okay if you want to just give up a o z q'

dict = {}

for val in myinput:
    dict[val] = output[myinput.index(val)]

dict['\n'] = ''

f = open(sys.argv[1],'r');

line = f.readline()
val = int(line)

if val <= 30:
    ind = 1
    while ind <= val:
        mytext = 'Case #' + str(ind) + ': '
        line = f.readline()
        if not line:
            break
        for val in line:
            mytext = mytext + dict[val]
        print mytext
        ind = ind + 1;

f.close()









