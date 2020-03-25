# -*-coding:utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import cv2
import sys, os
import numpy as np

print(cv2.__version__)

os.makedirs("Output", exist_ok=True)
# img = cv2.imread("data/src/Lena.jpg")
# # print(img.shape)
# print "Hello World"
# # print(img)

print("Choice Video Capturing")
print("Video = 0 ")
print("Live Stream = 1 ")

choice = int(input())

if choice == 0:
    cap = cv2.VideoCapture("data/movie/People.mp4")
elif choice == 1:
    cap = cv2.VideoCapture(0)
else:
    sys.exit()

if not cap.isOpened():
    print("Stream Error")
    sys.exit()

chk_read, frame = cap.read()
Img_Height, Img_Width = frame.shape[:2]
# frame.shape = (height,width)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
OutPut_Image = cv2.VideoWriter("./Output/test.avi", fourcc, 30.0, (Img_Height, Img_Width))

while cap.isOpened():
    chk_read, frame = cap.read()
    if not chk_read:
        break
    print('Width = ', cap.get(3), ' Height = ', cap.get(4), ' fps = ', cap.get(5))
    cv2.imshow("video", frame)
    OutPut_Image.write(frame)
    if cv2.waitKey(30) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
