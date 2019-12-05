limm = 28

from scipy.stats import truncnorm
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as patches

genlb = -128
genub = 128
numcolors = 16

x = range(genlb, genub + 1)
l = np.array_split(np.array(x), numcolors)
print(len(l))


def get_random_color(lb, ub):
    my_mean = (lb + ub) / 2
    my_std = abs((lb - ub)) / 3
    a, b = (lb - my_mean) / my_std, (ub - my_mean) / my_std
    return truncnorm.rvs(a, b, size=2, loc=my_mean, scale=my_std)[0]


from colormath.color_objects import LabColor, sRGBColor, AdobeRGBColor
from colormath.color_conversions import convert_color

from colour import Color


def convClamp(m):
    c = convert_color(m, sRGBColor)
    return sRGBColor(c.clamped_rgb_r, c.clamped_rgb_g, c.clamped_rgb_b).get_rgb_hex()


# print(list(convStart.range_to(convEnd, 5)))

def hex_to_RGB(hex):
    ''' "#FFFFFF" -> [255,255,255] '''
    # Pass 16 to the integer function for change of base
    return [int(hex[i:i + 2], 16) for i in range(1, 6, 2)]


def RGB_to_hex(RGB):
    ''' [255,255,255] -> "#FFFFFF" '''
    # Components need to be integers for hex to make sense
    RGB = [int(x) for x in RGB]
    return "#" + "".join(["0{0:x}".format(v) if v < 16 else
                          "{0:x}".format(v) for v in RGB])


def color_dict(gradient):
    ''' Takes in a list of RGB sub-lists and returns dictionary of
      colors in RGB and hex form for use in a graphing function
      defined later on '''
    return {"hex": [RGB_to_hex(RGB) for RGB in gradient],
            "r": [RGB[0] for RGB in gradient],
            "g": [RGB[1] for RGB in gradient],
            "b": [RGB[2] for RGB in gradient]}


def linear_gradient(start_hex, finish_hex="#FFFFFF", n=10):
    ''' returns a gradient list of (n) colors between
      two hex colors. start_hex and finish_hex
      should be the full six-digit color string,
      inlcuding the number sign ("#FFFFFF") '''
    # Starting and ending colors in RGB form
    s = hex_to_RGB(start_hex)
    f = hex_to_RGB(finish_hex)
    # Initilize a list of the output colors with the starting color
    RGB_list = [s]
    # Calcuate a color at each evenly spaced value of t from 1 to n
    for t in range(1, n):
        # Interpolate RGB vector for color at the current value of t
        curr_vector = [
            int(s[j] + (float(t) / (n - 1)) * (f[j] - s[j]))
            for j in range(3)
        ]
        # Add it to our list of output colors
        RGB_list.append(curr_vector)

    return color_dict(RGB_list)



startLabC = LabColor(50, -limm, -limm)
endLabC = LabColor(50, limm, limm)
convStart = convClamp(startLabC)
convEnd = convClamp(endLabC)

print(convStart, convEnd)
lg = linear_gradient(convStart, convEnd)['hex']

print(list(np.linspace(-limm, limm, num=numcolors)))
from itertools import product

lset = list(np.linspace(40, 60, num=numcolors))
xset = list(np.linspace(-limm, limm, num=numcolors))

colors = random.sample((list(product(lset,xset, xset))), k=10)
print('LEN COL',len(colors))

def convcolor(c):
    print(c)
    l = LabColor(*c)
    return convClamp(l)


ready_colors = list(map(convcolor, colors))

fig, ax = plt.subplots(1)
axes = plt.gca()
axes.set_xlim([0, 100])
axes.set_ylim([0, 100])
for i, j in enumerate(ready_colors):
    print(j)
    rect = patches.Rectangle((0, i * 10), 30, 30, linewidth=0, edgecolor='r',
                             facecolor=j)
    ax.add_patch(rect)
plt.show()

# for i in l:
#     a = get_random_color(min(i), max(i))
#     b=0
#     m = LabColor(64, a, b)
#     c=convert_color(m, sRGBColor)
#     clamped_c=sRGBColor(c.clamped_rgb_r,c.clamped_rgb_g,c.clamped_rgb_b)
#     print('AAA', clamped_c.get_upscaled_value_tuple(), m.get_value_tuple(),clamped_c.get_rgb_hex())
#     rect = patches.Rectangle((0, 0), 40, 30, linewidth=1, edgecolor='r',
#                              facecolor=clamped_c.get_value_tuple())
#     fig, ax = plt.subplots(1)
#     ax.add_patch(rect)
#     plt.show()
