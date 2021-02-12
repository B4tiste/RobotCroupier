import cv2

print("Package imported")

#Image

image = cv2.imread("Ressources/black.jpg")  #Permet de charger une image

cv2.imshow("Fermion", image) #Permet d'afficher l'image dans une nouvelle fenetre
cv2.waitKey(1) #Permet de créer un délais afin de visualiser l'image

#Video

video = cv2.VideoCapture("Ressources/test_video.3gp") #Permet de charger une video

#Video = Somme d'image : boucle while pour parcourir toutes les frames de la video

while True:
    success, frame = video.read() #Permet de donner une réponse booléenne sur la lecture chaque frame de la video

    cv2.imshow("Clip",frame) #Affichage d'une frame à chaque cycle de la boucle while

    if cv2.waitKey(40) & 0xFF ==ord('q'): #Boucle de fermeture de la vidéo lors de l'appuie sur la touche "q"
        break

#Camera

camera = cv2.VideoCapture(0)
camera.set(3, 640) #Largeur
camera.set(4, 480) #Hauteur
camera.set(10, 50) #Luminosité

while True:
    success, img = camera.read()
    cv2.imshow("Webcam", img)
    if cv2.waitKey(1) & 0xFF ==ord('c'):
        break