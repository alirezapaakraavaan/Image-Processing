from rembg import remove
from PIL import Image
import cv2
from src.framework.load_image import load_image
from src.framework.show_image import show_image

def remove_background(path):
    input = Image.open(path)
    output = remove(input)
    out_path = "src/img/result.png"
    output.save(out_path)
    result = load_image(out_path)
    show_image('No Background', result)
