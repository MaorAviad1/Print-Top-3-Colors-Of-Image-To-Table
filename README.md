# Dominant Colors Analyzer

This script analyzes and extracts the top 3 dominant colors from a collection of JPEG images in the current working directory. The output is presented in a table format, with the closest CSS3 color names.

## Requirements

- Python 3.6 or higher
- PIL (Pillow)
- webcolors
- tabulate

## Installation

To install the required libraries, run:

```bash
pip install Pillow webcolors tabulate


## Usage

1.  Save the script as `dominant_colors_analyzer.py`.
2.  Place the `.jpg` image files in the same directory as the script.
3.  Run the script:

The output will be a table displaying the file name and the top 3 dominant colors for each image.


# Example Output

File Name      Color 1    Color 2    Color 3
------------  ---------  ---------  ---------
example1.jpg  lavender   azure      mistyrose
example2.jpg  coral      steelblue  gainsboro
example3.jpg  skyblue    aliceblue  lightgray
