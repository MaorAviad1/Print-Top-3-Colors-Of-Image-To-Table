import os
from collections import Counter
from PIL import Image
import webcolors
from tabulate import tabulate

def closest_color(rgb):
    differences = {}
    for color_hex, color_name in webcolors.CSS3_HEX_TO_NAMES.items():
        r, g, b = webcolors.hex_to_rgb(color_hex)
        differences[sum([(r - rgb[0]) ** 2,
                         (g - rgb[1]) ** 2,
                         (b - rgb[2]) ** 2, ])] = color_name
    return differences[min(differences.keys())]

image_files = [f for f in os.listdir(".") if f.endswith(".jpg")]

table_data = []

for filename in image_files:
    img = Image.open(filename)

    colors = img.getcolors()

    if not colors:
        colors = img.getdata()

    counter = Counter(colors)
    most_common_colors = counter.most_common(3)

    color_names = []
    for color, count in most_common_colors:
        r, g, b = color
        color_name = closest_color((r, g, b))
        color_names.append(color_name)

    table_data.append([filename, *color_names])

# Define table headers
headers = ["File Name", "Color 1", "Color 2", "Color 3"]

# Print the table
print(tabulate(table_data, headers=headers))
