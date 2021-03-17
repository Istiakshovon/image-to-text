import pytesseract
import cv2

img = cv2.imread('img1.png')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Gray image', img_gray)

result = pytesseract.image_to_string(img_gray)
cv2.waitKey()

print(result)