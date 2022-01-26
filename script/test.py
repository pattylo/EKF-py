#! /usr/bin/env python3.6
import os

path = '/home/patty/darknet/data/obj'

imagefiles = []
os.chdir(path)

for filename in os.listdir(os.getcwd()):
    if filename.endswith("jpg"):
        imagefiles.append(filename)
        print (filename)
    
os.chdir('/home/patty/python/files')
with open("test.txt", "w") as generate:
    for what in imagefiles:
        generate.write(what)
        generate.write("\n")
    generate.close()


