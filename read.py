import cv2 as cv

# reading images:
# img = cv.imread('Resources/Photos/cat.jpg')

# cv.imshow("Cat", img)
# cv.waitKey(0)


# reading videos:
# 0 would do webcam, 1 second cam
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
  isTrue, frame = capture.read() # reads video frame by frame and success boolean
  cv.imshow("Video", frame)

  # if letter d is pressed, break out of video
  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()
