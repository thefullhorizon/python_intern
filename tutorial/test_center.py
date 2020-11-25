# -*- coding=utf-8 -*-
"""

这里用户快速的验证某些操作

Author       :   Cucumber
Date         :   10/23/20

"""
import pandas as pd


if __name__ == '__main__':
    df = pd.DataFrame({"name": ["horizon", "cucumber", "", "horizon,k"],
                       "age": [20, 22, 16, 25]})
    print(df)

