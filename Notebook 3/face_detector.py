# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 08:56:28 2021

@author: ASUS
"""
"""
import cv2

trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('en_crecjhe._istock_5.jpg')


grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)


#(x,y,w,h)=face_coordinates[0]
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Detector',img)
cv2.waitKey()

print("code completed")
"""

import cv2

trained_face_data=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

webcam=cv2.VideoCapture(0)


while True:
    successful_forme_read,forme=webcam.read()
    grayscaled_img=cv2.cvtColor(forme,cv2.COLOR_BGR2GRAY)
    face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)
    for (x,y,w,h) in face_coordinates:
        cv2.rectangle(forme,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow('Detector',forme)
    key=cv2.waitKey(1)
    
    if key==81 or key ==113:
        break

webcam.release()
   

"""

grayscaled_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


face_coordinates=trained_face_data.detectMultiScale(grayscaled_img)

print(face_coordinates)


#(x,y,w,h)=face_coordinates[0]
for (x,y,w,h) in face_coordinates:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Detector',img)
cv2.waitKey()
"""
print("code completed")