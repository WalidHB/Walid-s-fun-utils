from PIL import Image


im = Image.open("image.jpg")
color = (0, 0, 0)
i = 0
while color[0] == color[1] and color[1] == color[2]:
    color = sorted(im.getcolors(maxcolors=2073600), key=lambda t: t[0], reverse=True)[i][1]
    i = i + 1
print(color)