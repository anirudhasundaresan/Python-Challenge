import requests
import pprint
import pdb
from collections import Counter

'''
url = "http://www.pythonchallenge.com/pc/def/ocr.html"
r = requests.get(url)
print(r.content) # piped and output to code_2_op.txt
'''

char_d = {}
with open('code_2_op.txt') as fp:
    for i in range(37):
        next(fp) # skipping lines
    for line in fp:
        for char in line:
            if char not in char_d:
                char_d[char] = 1
            else:
                char_d[char] += 1


# using Counter on the char_d reveals the letters e.q.u.a.l.i.t.y come up only once.
# Replacing 'ocr' with 'equality' solves this level.
