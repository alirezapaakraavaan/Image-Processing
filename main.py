from src.load_image import load_image
from src.denoising import denoising
from src.sharping import sharping
from src.closing import closing

#Loading Image
path = 'src/img/input.png'
image = load_image(path)

#Denoising Image
denoising(image)

#Sharping Image
sharping(image)

closing()