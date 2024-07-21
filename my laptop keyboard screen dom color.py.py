from openrgb import OpenRGBClient
from openrgb.utils import RGBColor
import pyautogui
import time
import numpy as np
from colors import *



def closest_node(node, nodes):
    nodes = np.asarray(nodes)
    deltas = nodes - node
    dist_2 = np.einsum('ij,ij->i', deltas, deltas)
    return tuple(nodes[np.argmin(dist_2)])


def closest(color, colors):
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    smallest_distance = colors[index_of_smallest]
    return smallest_distance 


client = OpenRGBClient()
k = client.get_devices_by_name('ASUS TUF Keyboard')[0]
k.set_mode("direct")
n = 0
m = 0
o = 0

try:
   while True:
        im = pyautogui.screenshot()
        color = sorted(im.getcolors(maxcolors=2073600), key=lambda t: t[0], reverse=True)[0][1]
        if color == (255, 255, 255) or color == (30, 30, 30):
            color = sorted(im.getcolors(maxcolors=2073600), key=lambda t: t[0], reverse=True)[1][1]

        color = closest(color, newcolordb)
        print(color)
        
        # r, g, b =h2r(r2h(color))
        r, g, b = color
        k.set_color(RGBColor(r, g, b))
        if (r, g, b) == (n, m, o):
            continue
        else:
            k.set_color(RGBColor(r, g, b))
            n, m, o = r, g, b
            
        print(r, g, b)
        time.sleep(0.1)
except KeyboardInterrupt:
    print('\ndone')


