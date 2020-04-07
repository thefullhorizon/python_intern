# -*- coding: utf-8 -*-
import numpy as np


def handle_numpy():
    a = np.arange(32).reshape(8, 4)
    print(a)
    print(a[[4, 2, 1, 7]])
    # print(a.shape)
    # print(a.ndim)
    # print(a.dtype)
    # a1 = np.arange(10)
    # s = slice(2, 8, 2)
    # print(a1[s])
    # x = np.array([[1, 2], [3, 4], [5, 6]])
    # print(x)
    # y = x[[0, 1, 2], [0, 1, 1]]
    # print(y)


if __name__ == "__main__":
    handle_numpy()

