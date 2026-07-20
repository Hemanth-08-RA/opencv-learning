import cv2
import numpy as np

background = cv2.imread(r"C:\Users\asus\Downloads\green\bg.jpeg")
background = cv2.resize(background,(640,480))

lower_green = np.array([35,100,100])
upper_green = np.array([85,255,255])

cap = cv2.VideoCapture(r"C:\Users\asus\Downloads\green\green.mp4")

if not cap.isOpened():
    print("Video is not Found")
    exit()
    
while True:
    ret,frame = cap.read()
    
    frame = cv2.resize(frame,(640,480))
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv,lower_green,upper_green)
    mask_inv = cv2.bitwise_not(mask)
    
    person = cv2.bitwise_and(frame,frame,mask=mask_inv)
    background_part = cv2.bitwise_and(background,background,mask=mask)
    
    result = cv2.add(person,background_part)
    
    cv2.imshow("demo",hsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    