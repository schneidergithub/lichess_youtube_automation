
from PIL import Image, ImageDraw

def generate_thumbnail(frame):
    img = Image.open(frame)
    draw = ImageDraw.Draw(img)

    draw.text((100,100),"CHESS PUZZLE", fill="yellow")

    img.save("thumbnails/thumb.png")
