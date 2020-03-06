# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

'''
主要联系数据分析里面基础的Python库

'''


def test_pandas():
    """
    pandas 数据类型：Series,DataFrame,
    :return:
    """

    array = np.random.randn(3, 3)
    # print(array)
    df_obj = pd.DataFrame(array)
    # print(df_obj)
    print(df_obj.head())
    pass


def test():
    names = ["horizon", "xiyouji"]
    for i, item in enumerate(names):
        print("position %s item %s " % (i, item))


if __name__ == "__main__":
    # test()
    test_pandas()

