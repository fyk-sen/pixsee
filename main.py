# imports
import numpy as np
from PIL import Image
from urllib.request import urlopen
import matplotlib.pyplot as plt

# script
url = input('Enter image URL:')
img = Image.open(urlopen(url))

colors = Image.Image.getpalette(img)
sort = [colors[x:x+3] for x in range(0,len(colors),3)]

palette = np.array(sort)[np.newaxis, :]

plt.subplot(2,1,1)
plt.imshow(palette)

nimg = np.array(img)
nimg = Image.fromarray(nimg, mode = 'P')
nimg.putpalette(colors)

plt.subplot(2,1,2)
plt.imshow(nimg)
plt.show()
