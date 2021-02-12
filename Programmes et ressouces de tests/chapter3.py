import  cv2 as ocv
import numpy as np

image = ocv.imread("Ressources/Fermion.jpg")

print("Fermion : ", image.shape) #Taille (largeur, hauteur, format (3 = RGB))

imageResize = ocv.resize(image, (300, 300)) #Redimmensionner une image (image, (largeur, hauteur))

print("Fermion resized : ", imageResize.shape)

imageCropped = image[300:600, 300:600] #Rognage (Hauteur, Largeur)

ocv.imshow("Image", image)

ocv.imshow("Image Resize", imageResize)

ocv.imwrite("Ressources/fermion_resized.png", imageResize);

ocv.imshow("Image Cropped", imageCropped)

ocv.waitKey(0)