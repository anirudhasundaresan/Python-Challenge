import requests
import pprint
import pdb

# url1 = "http://www.pythonchallenge.com/pc/def/peak.html"
# after realizing that using 'banner.p' will help us get a pickled (serialized character stream) file.

#url2 = 'http://www.pythonchallenge.com/pc/def/banner.p'
#r = requests.get(url2)
#print(r.content)


# Now, let's open this new file from 'banner.p' using pickle.

import pickle

#file = open('code_5_op2_p', 'wb')
#file2 = open('code_5_op2.pkl', 'wb')
#pickle.dump(r.content, file2)

file1 = open('code_5_op2.pkl', 'rb')
data_ = pickle.load(file1)

print("Showing the pickled data: ")
item_ls = []
for index, item in enumerate(data_):
    item_ls.append(item)


