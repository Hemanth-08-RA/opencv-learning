# Car Detection
import cv2

cascade = r"C:\Users\asus\Downloads\cars (1).xml"
Video = r"C:\Users\asus\Downloads\WhatsApp Video 2026-07-20 at 10.58.27 PM.mp4"

cap = cv2.VideoCapture(Video)
car_cascade = cv2.CascadeClassifier(cascade)

while True:
    Success,image = cap.read()
    
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray,1.1,1)
    
    for (x,y,w,h) in cars:
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),1)
        
    cv2.imshow("car detector",image)
    
    if cv2.waitKey(33) == 27:
        break
    
cv2.destroyAllWindows()