import requests
import pprint
import pdb

#url1 = "http://www.pythonchallenge.com/pc/def/channel.html"

#r = requests.get(url1)
#x = r.content.decode('UTF-8')
#print(x)

## This challenge has nothing to do with 'zip' command; but only with zipped files.

'''
import sys
import os
file_no = '90052'
fname =  'code_6/90052.txt'

sys.stdout = open('code_6_op2.txt', 'w')
def read_zip(fname):
    with open(fname, 'r') as fp:
        for line in fp:
            print(line)
            next_ = 'code_6/'+line.split()[-1]+'.txt'
            print(next_)
            if not line.split()[-1].isdigit():
                break
            else:
                read_zip(next_)

read_zip(fname)
'''
# Now, it says: 'Read the comments.' Later realized after looking at the forum that zip files have comments embedded into them and we need to extract them and see.
# Accessible using Python ZipFile objects (just like 'open').

fname = '90052.txt'
from zipfile import ZipFile
def read_zip_(fname):
    with ZipFile('code_6/code_6_channel.zip', 'r') as myzip:
        with myzip.open(fname) as myfile:
            next_ = myfile.read().decode('UTF-8')
            print(myzip.getinfo(fname).comment.decode('UTF-8'), end='')
            if next_.split()[-1].isdigit():
                read_zip_(next_.split()[-1]+'.txt')
            else:
                exit()
read_zip_(fname)

# you'll get the enlarged text which reads: HOCKEY all written using O, X, Y, G, E, N.
# go to next level by using 'oxygen.html'

