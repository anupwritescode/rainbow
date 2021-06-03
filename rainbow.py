from PIL import Image, ImageDraw

w, h = 200, 200
shape = [0, 0, w*2, h*2]
canvas = Image.new('RGB', (w, h))

overlay = ImageDraw.Draw(canvas)

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
width = 5
for color in colors:
    overlay.arc(shape, start = 180, end = 270, fill = color, width = width)
    shape[0] = shape[0] + width
    shape[1] = shape[1] + width

canvas.show()
