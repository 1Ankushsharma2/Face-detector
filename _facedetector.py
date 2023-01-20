import cv2
cap=cv2.VideoCapture(0)
fasecascade=cv2.CascadeClassifier("C:\\Users\\Client\\AppData\\Local\\Programs\\Python\\Python311-32\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

while(True):
    ret, frame=cap.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces=fasecascade.detectMultiScale(

        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),   
     )

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h), (0,255,0), 2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break    
cap.release()
cv2.destroyAllWindows()
