import requests
import pprint
import pdb
from collections import Counter

# similar flavor to Code_2.
'''
url = "http://www.pythonchallenge.com/pc/def/equality.html"
r = requests.get(url)
print(r.content) # piped and output to code_3_op.txt
'''

char_d = {}
with open('code_3_op.txt') as fp:
    for i in range(21):
        next(fp) # skipping lines
    for line in fp:
        print(line)
        print(len(line))
        pdb.set_trace()
# using Counter on the char_d reveals the letters e.q.u.a.l.i.t.y come up only once.
# Replacing 'ocr' with 'equality' solves this level.
