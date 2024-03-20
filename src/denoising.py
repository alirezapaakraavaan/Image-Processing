import cv2

def denoising(image):
    dst = cv2.fastNlMeansDenoisingColored(image, None,10,10,10,10)
    cv2.imshow('denoised', dst)
