import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
# simple thresholding
# grayscale image, threshold value, max value, type
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('threshold', thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('threshold inverse simple', thresh_inv)

# adaptive thresholding:
# takes grayscale image, max value, method, type, block size (neighborhood size), c value (fine tuning threshold), but no threshold value bc it's adaptive
adaptive_thresh = cv.adaptiveThreshold(gray,  
255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow("adaptive thresholding", adaptive_thresh)

cv.waitKey(0)