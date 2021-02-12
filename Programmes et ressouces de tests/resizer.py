import PIL
import  cv2
import os
import glob
from PIL import Image
f = 'Cartes'
for file in os.listdir(f):
    f_img = f+"/"+file
    img = Image.open(f_img)
    img = img.resize((320,426))
    img.save(f_img)
cv2.waitKey(30)






"""""
import numpy as np
#### Import Images
path = 'Cartes'
folderlen = len(path)
os.mkdir('Resized Cards')
i = 1

for img in glob.glob(path + "/*.png"):
    image = Image.open(img)
    imgResized = cv2.resize(image, (240, 426))
    cv2.imwrite("image" + img[folderlen], imgResized)
    i+= 1
    cv2.imshow('gngng', imgResized)
    cv2.waitKey(30)
    cv2.destroyAllWindows()

images = []
classNames = []
myList = os.listdir(path)
print('Total Classes Detected', len(myList))
for cl in myList:
    imgCur = cv2.imread(f'{path}/{cl}', 0)
    imageResize = cv2.resize(imgCur,(240, 426))  # Redimmensionner une image (image, (largeur, hauteur))
    images.append(imgCur)
    classNames.append(os.path.splitext(cl)[0])
cv2.imwrite(""+classNames, imageResize);

cv2.waitKey(0)
"""