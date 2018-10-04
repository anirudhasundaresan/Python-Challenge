# K -> M ; O -> Q and E -> G

# Create a dictionary where each letter points to what it represents and output the string. There must be a simple way to get the alphabet list.
# There is a 1 letter gap between the letters. And all are lower case letters.

# Full stops should match to the same. And so must brackets, I guess.

# 'ord' and 'chr' commands will come in handy here.

l1 = ['y', 'z', ' ', "'", '(', ')', '.', '/', ':']
l2 = ['a', 'b', ' ', "'", '(', ')', '.', '/', ':']
dic = dict(zip(l1, l2))

for i in range(97, 121):
    #l1.append(chr(i))
    #l2.append(chr(i+2))
    dic[chr(i)] = chr(i+2) # all keys appear only once, hence no specific conditions required.
#l1_ = ''.join(l1)
#l2_ = ''.join(l2)

decoded_str = ''
coded_str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

# decoded_str = coded_str.maketrans(l1_, l2_)

for char in coded_str:
    decoded_str += dic[char]

print(decoded_str)

'''
Output:
i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.
https://docs.python.org/2/library/string.html
'''

# need to apply this on the URL now:
url = 'http://www.pythonchallenge.com/pc/def/map.html'
url_encoded = ''

for char in url:
    url_encoded += dic[char]

print(url_encoded)
# only change the 'map' to 'ocr' to get challenge no: 2
