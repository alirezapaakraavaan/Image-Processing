from src.framework.load_image import load_image
from src.denoising import denoising
from src.sharping import sharping
from src.framework.closing import closing
from src.remove_bachground import remove_background

#Loading Image
path = 'src/img/input.png'
image = load_image(path)

#Denoising Image
denoising(image)

#Sharping Image
sharping(image)

#Remove Background
remove_background(path)

closing()
