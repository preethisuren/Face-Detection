import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Video
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    #convert image to grey scale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.1, 4)

    #draw rectangle around the face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 3, color='black')


    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
cap.release()