import cv2
from src.framework.show_image import show_image

def denoising(image):
    denoised = cv2.fastNlMeansDenoisingColored(image, None,10,10,10,10)
    show_image('Denoised', denoised)
