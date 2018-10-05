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

with open('code_3_op.txt') as fp:
    for i in range(21):
        next(fp) # skipping lines
    for line in fp:
        # take care of edge cases first; note that we need to look for lower case in EXACTLY 3 upper case letters.
        for string in [line[ind:ind+9] for ind in range(len(line)-9)]:
            if (string[0]+string[4]+string[8]).islower() and (string[1:4]+string[5:8]).isupper():
                print(string[1:8])

'''
I got the words (10 of them) - but to get the next level link, you have to form the word from the middle letter of each string you got. 'linkedlist'. Had to look at forums for this.
'''
