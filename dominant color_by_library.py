from colorthief import ColorThief
from colormap import rgb2hex

color_thief = ColorThief('image.jpg')
print(type(color_thief))
dominant_color_rgb = color_thief.get_color(quality=1)

print (dominant_color_rgb) #this gives the RGB

red_value = dominant_color_rgb[0]
green_value = dominant_color_rgb[1]
blue_value = dominant_color_rgb[2]

print(rgb2hex(dominant_color_rgb[0], dominant_color_rgb[1], dominant_color_rgb[2])) #this gives the HEX


