import cv2
import numpy as np

def sharping(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
    sharpened_image = cv2.filter2D(image, -1, kernel) 
    cv2.imshow('sharped', sharpened_image) 
