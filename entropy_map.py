from skimage import data
from skimage.util import img_as_ubyte
from skimage.filters.rank import entropy
from skimage.morphology import disk
import cv2
import numpy as np
img_name = 'INSERT_IMAGE_NAME_HERE'
def on_change(val):
    img = cv2.imread(img_name,0)
    entr_img = entropy(img, disk(val))
    print(np.mean(entr_img))
    cv2.imshow('image',entr_img.astype(np.uint8)*20)
 
windowName = 'image'
 
cv2.imshow(windowName, cv2.imread(img_name,0))
cv2.createTrackbar('slider', windowName, 0, 100, on_change)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
