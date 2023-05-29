# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 11:58:11 2021

@author: ASUS
"""
"""
import cv2

trained_face_data=cv2.CascadeClassifier('cars.xml')

webcam=cv2.VideoCapture('v1.mp4')


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
import cv2

trained_face_data=cv2.CascadeClassifier('haarcascade_fullbody.xml')

webcam=cv2.VideoCapture('tokyou.mp4')


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