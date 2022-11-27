from split_image import split_image
import os


def split(filename, tile_h=6, tile_w=3):
    out = os.path.join('./Blocks/')
    img = os.path.join('./Images/{}').format(filename)
    split_image(img, rows=tile_w, cols=tile_h, should_square=False, should_cleanup=False)


# split('launch.jpeg')
