#Real time Face Detection using your webcam as a primary camera

import cv2
a = cv2.CascadeClassifier(cv2.data.haarcascades + r"C:\Users\asus\Downloads\haarcascade_frontalface_default (1) (1).xml")
cam = cv2.VideoCapture(0)

while True:
    ret,cam_img = cam.read()
    gray = cv2.cvtColor(cam_img, cv2.COLOR_BGR2GRAY)
    face = a.detectMultiScale(gray,1.3,6)
    for (x1,y1,w1,h1) in face:
        cv2.rectangle(cam_img,(x1,y1),(x1+w1,y1+h1),(255,0,0),3)
    cv2.imshow("Face",cam_img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
       break
   
cam.release()  
cv2.destroyAllWindows()
 