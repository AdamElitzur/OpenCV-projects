import cv2 as cv

img = cv.imread("Resources/Photos/cat.jpg")
cv.imshow("Cat", img)

def rescaleFrame(frame, scale=0.2):
  # images, videos, live videos
  width = int(frame.shape[1]*scale)
  height = int(frame.shape[0]*scale)
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow("Image", resized_image)

def changeRes(width, height):
  # works for only live video
  capture.set(3,width)
  capture.set(4,height)


# reading videos:
# 0 would do webcam, 1 second cam
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
  isTrue, frame = capture.read() # reads video frame by frame and success boolean
  frame_resized=rescaleFrame(frame)
  cv.imshow("Video", frame)
  cv.imshow("Video Resized", frame_resized)
  # if letter d is pressed, break out of video
  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()