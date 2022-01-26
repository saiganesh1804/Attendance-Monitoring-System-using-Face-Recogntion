import cv2
import numpy as np
import face_recognition

imgelon = face_recognition.load_image_file('ImagesBasic/ElonMusk.jpg')
imgelon2 = face_recognition.load_image_file('ImagesBasic/ElonMusk.jpg')
imgelon = cv2.cvtColor(imgelon,cv2.COLOR_BGR2RGB)
imgtest = face_recognition.load_image_file('ImagesBasic/ElonMuskTest.jpg')
# imgtest = cv2.cvtColor(imgtest,cv2.COLOR_BGR2RGB)

# faceLoc = face_recognition.face_locations(imgelon)[0]
# encodeElon = face_recognition.face_encodings(imgelon)[0]
# cv2.rectangle(imgelon,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),((255,255,0)),2)
# # print(faceLoc)
# faceLoctest = face_recognition.face_locations(imgtest)[0]
# encodeElontest = face_recognition.face_encodings(imgtest)[0]
# cv2.rectangle(imgtest,(faceLoctest[3],faceLoctest[0]),(faceLoctest[1],faceLoctest[2]),((255,255,0)),2)
#
# results = face_recognition.compare_faces([encodeElon],encodeElontest)
# faceDis = face_recognition.face_distance([encodeElon],encodeElontest)
# print(results,faceDis)
# cv2.putText(imgtest,f'{results}{round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow('Elon Musk',imgelon)
# cv2.imshow('Elon Test',imgtest)
cv2.imshow('Elon Musk(BGR)',imgelon2)
cv2.waitKey(0)