import cv2 as cv
import os
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Mindy Kaling', 'Madonna']
DIR = '/Users/adamelitzur/Documents/Code/OpenCV-projects/Resources/Faces/train'

haar_cascade = cv.CascadeClassifier('haar_face.xml')


features = []
labels = []

def create_train():
  for person in people:
    # getting path to person folder
    path = os.path.join(DIR, person)
    label = people.index(person)

    for img in os.listdir(path):
      # getting path to image in person folder
      img_path = os.path.join(path, img)

      img_array = cv.imread(img_path)

      gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

      faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

      for (x,y,w,h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]
        features.append(faces_roi)
        labels.append(label)

create_train()
print("training done ________________")
features = np.array(features, dtype="object")
labels = np.array(labels)
# instantiates face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()

# train the recognizer on features list and labels list

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)