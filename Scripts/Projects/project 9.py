import cv2
img = cv2.imread(r"C:\Users\asus\OneDrive\Desktop\Learn_CV\images\Ironman.jpg")

color = cv2.bilateralFilter(img,d=9,sigmaColor=75,sigmaSpace=75)
gray = cv2.cvtColor(color,cv2.COLOR_BGR2GRAY)
gray_blur = cv2.medianBlur(gray,7)

edges = cv2.adaptiveThreshold(gray_blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,10)

cartoon = cv2.bitwise_and(color,color,mask=edges)

cv2.imshow("Cartoon",cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
