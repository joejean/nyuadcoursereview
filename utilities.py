# -*- coding: utf-8 -*-
filename= raw_input('Enter filename: ')

f = open(filename, "r")

mylist=[]

for line in f:
    line2 = line.strip('\n')
    line3 = line2.split(" ")
    line4 = line3[1]+" "+line3[0]
    print line4
    mylist.append(line4)

f.close()
print mylist



##filename= raw_input('Enter filename: ')
##
##f = open(filename, "r")
##
##mylist=[]
##
##for line in f:
##    line2 = line.strip('\n')
##    mylist.append(line2)
##
##f.close()
##print mylist
