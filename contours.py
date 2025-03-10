import cv2 as cv
import numpy as np

img = cv.imread("Resources/Photos/cats.jpg")

cv.imshow("cats", img)

# blank slate
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("blank", blank) 

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

# blur file
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# recommend use canny and then find contours from that
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f' found {len(contours)} contours')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow("controus", blank)

cv.waitKey(0)