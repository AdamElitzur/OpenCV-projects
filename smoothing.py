import cv2 as cv

img = cv.imread("Resources/Photos/cats.jpg")
cv.imshow('img', img)

# averaging:
average = cv.blur(img, (3,3))
cv.imshow('average blur', average)

# gaussian blur
gaussian = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('gaussian blur', gaussian)

# Median blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral blurring
# bilateral and median blurring start to look smudged at higher values
# img, diameter of pixel neighborhood, sigma color, sigma space (how far pixels will influences)
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)