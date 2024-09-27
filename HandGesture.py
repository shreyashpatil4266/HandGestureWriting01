import os

import cv2

#camera setup
width, height = 1280, 720

folderpath = "Presentation"

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(3,height)

#Get the list of presentation images
pathimages = sorted(os.listdir(folderpath), key=len)

#variables
imgNo = 0
hs, ws = int(120*1), int(213*1)

while True:
    #import images
    success, img = cap.read()
    pathFullimage = os.path.join(folderpath, pathimages[imgNo])
    imgcurrent = cv2.imread(pathFullimage)


    #Adding webcam image on slide
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgcurrent.shape
    imgcurrent[0:hs, w-ws:w] = imgSmall


    cv2.imshow("image", img)
    cv2.imshow("Slides", imgcurrent)


    key = cv2.waitKey(1)
    if key == ord('q'):
        break




