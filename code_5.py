import requests
import pprint
import pdb

#url1 = "http://www.pythonchallenge.com/pc/def/peak.html"
# after realizing that using 'banner.p' will help us get a pickled (serialized character stream) file.

url2 = 'http://www.pythonchallenge.com/pc/def/banner.p'
r = requests.get(url2)
x = r.content.decode('UTF-8')


# Now, let's open this new file from 'banner.p' using pickle.

import pickle
#file2 = open('code_5_op2.pkl', 'wb')
#store the op2 as pkl and read it as binary.

# Since pickle is a form of compression and serializing, the list ouptut after following operation makes sense. On printing, it finally reads 'channel'.

file1 = open('code_5_op2.pkl', 'rb')
data_ = pickle.load(file1)

#print("Showing the pickled data: ")
#item_ls = []
for index, item in enumerate(data_):
    print('\n')
    for it in item:
        char, num = it
        for i in range(int(num)):
            print(char, end='')




