# title says odd-even: I think it is a blend of 2 images, odd pixels and even pixels probably make separate pictures?

from matplotlib.image import imread

img = imread('cave.jpg')
print(img.shape)

import matplotlib.pyplot as plt
plt.imshow(img[::2, ::2, :])

# shows 'evil' -- that's the code
