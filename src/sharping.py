import cv2
import numpy as np
from src.framework.show_image import show_image

def sharping(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]]) 
    sharpened_image = cv2.filter2D(image, -1, kernel) 
    show_image('Sharped', sharpened_image) 
