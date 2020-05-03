# -*- coding: utf-8 -*-
"""
Created on Fri May  1 17:22:11 2020

@author: Muhammad Junaid Iqbal
"""

import cv2
import numpy as np

def main():
    w = 800
    h = 600
    cap = cv2.VideoCapture(0)
    
    cap.set(4, w)
    cap.set(5, h)
    
#    print(cap.get(3))
#    print(cap.get(4))
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    ret, frame1 = cap.read()
    ret, frame2 = cap.read()


    while ret:
        
        d = cv2.absdiff(frame1, frame2)
        print (d)
        
        grey = cv2.cvtColor(d, cv2.COLOR_BGR2GRAY)
        
        blur = cv2.GaussianBlur(grey, (5, 5), 0)
        
        ret, th = cv2.threshold( blur, 20, 255, cv2.THRESH_BINARY)
    
        dilated = cv2.dilate(th, np.ones((3, 3), np.uint8), iterations=1 )
        
        eroded = cv2.erode(dilated, np.ones((3, 3), np.uint8), iterations=1 )
        
        c, h = cv2.findContours(eroded, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        cv2.drawContours(frame1, c, -1, (0, 0, 255), 2)
        
        #cv2.imshow("Output", frame1)
        #cv2.imshow("Original", cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB))
        #cv2.imshow("Output", frame1)
        #cv2.imshow("Output1", cv2.Canny(frame1, 100, 150, L2gradient=True))
        #cv2.Canny(img, 100, 150, L2gradient=True)
        
        if cv2.waitKey(1) == 27: # exit on ESC
            break
        
        frame1 = frame2
        ret, frame2 = cap.read()

    cv2.destroyAllWindows()
    cap.release()

main()