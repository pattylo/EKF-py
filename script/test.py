#! /usr/bin/env python3.6
import os

if os.path.exists('/home/patty/python/files/train.txt'):
    os.remove('/home/patty/python/files/train.txt')

imagefiles = []
os.chdir('/home/patty/Downloads/Dataset/train')

for filename in os.listdir(os.getcwd()):
    if filename.endswith("jpg"):
        imagefiles.append(filename)
        print (filename)
    
os.chdir('/home/patty/python/files')
with open("train.txt", "w") as generate:
    for what in imagefiles:
        generate.write("data/obj/" + what)
        generate.write("\n")
    generate.close()


if os.path.exists('/home/patty/python/files/test.txt'):
    os.remove('/home/patty/python/files/test.txt')

imagefiles.clear()
imagefiles = []
os.chdir('/home/patty/Downloads/Dataset/test')

for filename in os.listdir(os.getcwd()):
    if filename.endswith("jpg"):
        imagefiles.append(filename)
        print (filename)
    
os.chdir('/home/patty/python/files')
with open("test.txt", "w") as generate:
    for what in imagefiles:
        generate.write("data/obj/" + what)
        generate.write("\n")
    generate.close()


