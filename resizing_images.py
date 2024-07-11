
import PIL
from PIL import Image

def resize_image(image_path, target_size):
    img = Image.open(image_path)
    img_resized = img.resize(target_size)
    return img_resized

path_img_1 = "demo_images/img_1.png"
img_1_resized = resize_image(path_img_1, (800,600))

img_1_resized.save('img_1_resized.png')

