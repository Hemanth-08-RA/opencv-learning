import cv2

def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
       print(x, ' ', y)
       font = cv2.FONT_HERSHEY_SIMPLEX
       cv2.putText(img, str(x)+','+str(y), (x,y), font, 1, (255,0,0), 2)
       cv2.imshow("Ironman", img)
       
    if event == cv2.EVENT_RBUTTONDOWN:
       print(x, ' ', y)
       font = cv2.FONT_HERSHEY_SIMPLEX
       cv2.putText(img, str(x)+','+str(y), (x,y), font, 1, (0,255,0), 2)  
       cv2.imshow("Ironman", img)
       
if __name__ == "__main__":
    
   img = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Ironman.jpg")
   cv2.imshow("Ironman", img)
   cv2.setMouseCallback("Ironman", click_event)
   cv2.waitKey(0)
   cv2.destroyAllWindows()
   