import cv2

def load_image(path):
    image = cv2.imread(path)

    return image