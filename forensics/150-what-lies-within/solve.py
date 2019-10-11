#!/usr/bin/env python
import numpy as np
from PIL import Image


def solve(fn='buildings.png'):
    with Image.open(fn) as im:
        pixels = np.array(im)

    xs = np.packbits((pixels[:,:,:3] % 2).ravel()[:224])
    return bytes(xs).strip(b'\0').decode('ascii')


if __name__ == '__main__':
    print(solve())
