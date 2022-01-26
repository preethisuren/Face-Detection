import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Image
imS = cv2.imread('harry.jpg')
img = cv2.resize(imS, (300, 300))
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(grey, 1.1, 4)
color = (0, 0, 0)
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3,)


    cv2.imshow('img',img)
    cv2.waitKey()