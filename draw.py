import cv2 as cv
import numpy as np

blank = np.zeros((500,500, 3), dtype="uint8")
# img = cv.imread("Resources/Photos/cat.jpg")
# cv.imshow("Cat", img)


# #1 paint the image a color:
# blank[200:300, 300:400] = 0,255,0
# cv.imshow("Green", blank)

# # 2. draw a rectangle
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=-1)
# cv.imshow("rectangle", blank)

# # 3. draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
# cv.imshow("Circle", blank)

# #4. draw a line:
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), 3)
# cv.imshow("Line", blank)

# 5. write text:
cv.putText(blank, "Hello my name is Adam", (0,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)