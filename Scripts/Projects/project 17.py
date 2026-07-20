#Gun shot 
import cv2
import imutils

gun_cascade = cv2.CascadeClassifier(r"C:\Users\asus\Downloads\gun_cascad (1).xml")
camera = cv2.VideoCapture(0)

firstFrame = None
gun_exit = None

while True:
    success,frame = camera.read()
    frame = imutils.resize(frame,width=500)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gun = gun_cascade.detectMultiScale(gray,1.3,5,minSize=(100,100))
    
    if len(gun) > 0:
        gun_exist = True
        
    for(x,y,w,h) in gun:
        frame = cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        
    cv2.imshow("Security", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    
if gun_exist:
    print("Gun Detected")
else:
    print("Gun not found")
    
camera.released()
cv2.destroyAllWindows