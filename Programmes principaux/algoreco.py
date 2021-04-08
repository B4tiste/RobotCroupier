import cv2
import numpy 
import os

path = '/home/pi/Desktop/base3'
#chemin de la base de données

orb = cv2.ORB_create(nfeatures=1000)

#### Import Images
images = []
classNames = []
myList = os.listdir(path)

#affiche le nombre d'images dans la base de données
print('Total Classes Detected', len(myList))

#enleve le .png dans le nom des images
for num in myList:
    imgCur = cv2.imread(f'{path}/{num}', 0)
    images.append(imgCur)
    classNames.append(os.path.splitext(num)[0])
print(classNames)

#Trouve les descriptors/keypoints des images et les ajoute a desList
#un descriptor ou keypoints est un element permettant de caractériser une image
def findDescriptor(images):
    desList = []
    for i in images:
        kp, des = orb.detectAndCompute(i, None)
        desList.append(des)
    return desList

#compare les keypoints et retourne l'indice de desList correspondant à l'image qui
#matche le mieux
def findID(img, desList, thres = 3):
    kp2, des2 = orb.detectAndCompute(img, None)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING)
    #brute force matcher ==> compare les images en fonctions de leur descriptor
    matchList = []
    finalVal = -1
    try:
        #compare le descriptor d'une image avec la liste de descriptors de la bdd
        for des in desList:
            matches = bf.knnMatch(des, des2, k=2)
            good = []
            for m, n in matches:
                if m.distance < 0.69 * n.distance:
                    good.append([m])
            matchList.append(len(good))
    except:
        pass
    # print(matchList)
    if len(matchList) != 0:
        if max(matchList) > thres:
            #retourne l'image avec le plus de similitudes 
            finalVal = matchList.index(max(matchList))
    return finalVal


def chiffrefinal(List):
    count = 0
    num = List[0]
    for i in List :
        nbchiffre = List.count(i)
        if (nbchiffre > count):
            count = nbchiffre
            num = i
    return num


desList = findDes(images)
print(len(desList))

cap = cv2.VideoCapture(0)
sucessimg = []


def reco():
    
    success, img2 = cap.read()
    imgOriginal = img2.copy()
    #copie l'image de la caméra
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    #la transforme en nuances de gris
    img2 = cv2.GaussianBlur(img2, (7,7), 0)
    #la floute

    id = findID(img2, desList)
    if id != -1:
        #si la fonction findID retourne un resultat coherent, l'affiche sur le flux camera
        cv2.putText(imgOriginal, classNames[id], (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 2)
        sucessimg.append(classNames[id])
    
    cv2.imshow('img2', imgOriginal)
    
    
while True:
    reco()
    cv2.waitKey(100)
