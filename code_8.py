import requests
import pprint
import pdb

'''
url1 = "http://www.pythonchallenge.com/pc/def/integrity.html"

r = requests.get(url1)
x = r.content.decode('UTF-8')
print(x)
'''
# Now, let's open this new file from 'banner.p' using pickle.


'''
#print("Showing the pickled data: ")
#item_ls = []
for index, item in enumerate(data_):
    print('\n')
    for it in item:
        char, num = it
        for i in range(int(num)):
            print(char, end='')

'''
un = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

#l1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#l2 = [0,1,2,3,4,5,6,7,8,9,]

'''
def decode_(sent):
    for ind, chr_ in enumerate(sent):
        #print(chr_)
        if chr_ == "x":
            print(int('0x' + sent[ind+1] + sent[ind+2]),16)

decode_(un)
decode_(pw)
'''

# I was right in guessing that they needed to be decoded. But, bee --> busy --> busy too --> bz2 was the clue.
import bz2
print(bz2.decompress(un))
print(bz2.decompress(pw))


