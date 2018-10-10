import requests
import pprint
import pdb

# Follow the chain. Every new request starting from 12345 will give you a new URL, need to try them sequentially.
url_new = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
next_ = '12345'

for i in range(400):
    url_new = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + next_
    r = requests.get(url_new)
    next_ = (r.content).split()[-1]
    print(next_)

'''
python code_4.py | grep [A-Za-z] gives 'peak.html' as the link to the next challenge.
I could have also used recursive function here.
'''
