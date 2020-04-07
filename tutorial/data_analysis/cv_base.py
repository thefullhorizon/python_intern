# -*- coding: utf-8 -*-
import skimage as si
from skimage import data
from skimage import io
import numpy as np
from matplotlib import pyplot as plt

# random_image = np.random.random([500, 500])
# plt.imshow(random_image)
# plt.colorbar()
# plt.show()


def show(it):

    plt.imshow(it, cmap='gray')
    plt.colorbar()
    plt.show()


if __name__ == "__main__":

    cat = data.camera()
    print(type(cat), cat.dtype, cat.shape)
    # cat[90:140, 140:200, :] = [0, 220, 0]
    # show(cat)

    imread = io.imread('./ecnu.png')
    show(imread)
