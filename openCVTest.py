import cv2
import pytesseract
#why did i install old tesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe"
img = cv2.imread("newspaper.jpeg")      
# cv2.namedWindow("output", cv2.WINDOW_NORMAL)                   
# imgS = cv2.resize(img, (960, 540))                    
# cv2.imshow("output", imgS)  
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# print(pytesseract.image_to_string(img))
hImg,wImg,_ = img.shape
boxes = pytesseract.image_to_boxes(img)
#characters
# for b in boxes.splitlines():
#     b = b.split(' ')
#     x,y,w,h = int(b[1]),int(b[2]),int(b[3]),int(b[4])
#     cv2.rectangle(img,(x,hImg-y),(w,hImg-h),(0,0,255),2)
#     cv2.putText(img,b[0],(x,hImg-y),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
# cv2.imshow("good",img)
# cv2.waitKey(0)
wordBox = pytesseract.image_to_data(img)
for x,b in enumerate(wordBox.splitlines()):
    if x!=0:
        print(b)
print(wordBox)