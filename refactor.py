#!/usr/bin/python
#coding: utf-8

# Algorithm to separate different classes into different files
import sys,re

filename = sys.argv[1]
file = open(filename, 'r')

imports = ""
line = file.readline()
while line[:5] != "class":
    imports += line
    line = file.readline()
f = False
for line in file:
    if line[:5] == "class":
        firstword = True
        print line
        words = line.split()
        classname = words[1]
        for letter in classname:
            if letter.isupper():
                if firstword:
                    firstword = False
                    classname = classname.replace(letter, letter.lower())
                else:
                    classname = classname.replace(letter, '_'+letter.lower())
            elif letter == '(':
                n = classname.find(letter)
                classname = classname[:n]
        if f:
            f.close()
        f = open(classname+".py", "w")
        f.write(imports)
        f.write(line)
    else:
        if f:
            f.write(line)
file.close()
