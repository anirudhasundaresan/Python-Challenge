import requests
import pprint
import pdb

''' (Nothing much; title = 'smarty')
url1 = "http://www.pythonchallenge.com/pc/def/oxygen.html"

r = requests.get(url1)
x = r.content.decode('UTF-8')
print(x)

'''
import numpy as np
from PIL import Image
img = Image.open('code_7.png')
im_arr = np.asarray(img)
#print(list(img.getdata()))

# this one was good, and I had to think a lot for this.
import npumpy as np
# I kinda got the idea that some message was hidden in the shaded gray areas of the pic.
x = im_arr[42:52] # somewhere around the centre.
img.mode() # gives RGBA
# All the A values for every pixel is 255. On decoding x[:][:][2] gives us a set of characters.
ls = []
for i in range(10):
    for j in range(629):
        ls.append(x[i][j][2])
print(''.join(ls))

# Decode the output ascii to alphabet: use chr()
# Next level: 'Integrity'
