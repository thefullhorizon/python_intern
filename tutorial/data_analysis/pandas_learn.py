# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

"""
学习总结：
Pandas是基于Numpy的一种数据结构扩展，主要包含了Series, DataFrame两种数据结构

>>>DataFrame

学习从以下维度进行：数据结构构造，基本方法，数据分析相关（统计分析，相关分析，分组，清洗，数据转换）

"""
print('-----Series--------')
# s = pd.Series([1, 2, 'horizon'])
# print(s, type(s))

# ts = pd.Series(np.random.randn(100), index=pd.date_range('1/1/2000', periods=100))
# ts = ts.cumsum()
# ts.plot()

print('-----DataFrame base--------')
# dates = pd.date_range('2020-04-02', periods=3)
# 用于每次产生预期的随机数
# np.random.seed(2)
# frame = pd.DataFrame(np.random.randint(2, 5, size=(3, 4)), index=dates, columns=list('HKMN'))
# print(frame)
# frame.at[dates[1], 'H'] = 9
# frame.iat[1, 1] = 3
# frame.loc[:, 'M'] = np.array([5] * len(frame))
# # 0表示按行（index），1表示按列(columns)
# print(frame.sort_index(axis=1, ascending=True))

# frame_new = frame.reindex(index=dates[0:3], columns=list(frame.columns) + ['T'])
# frame_new.loc[dates[0]:dates[1], 'T'] = 6
# print(frame)
# print(frame_new)
# dropna必须用可以对象接受，否则不生效，查看源码发现dropna是带return, 是不是python里面带返回值时必须要用对象接收？
# frame_new = frame_new.dropna(how='any')
# frame_new = frame_new.fillna(value=9)
# mean 默认按列进行，加参数1时按行统计
# print(frame_new.mean(1))
# print(frame_new.apply(lambda x: x.max() - x.min(), axis=1))

print('-----DataFrame advanced--------')

l_df = pd.DataFrame({'key': ['foo', 'bar'], 'value': ['l_value_0', 'l_value_1']})
r_df = pd.DataFrame({'key': ['foo', 'bar'], 'value': ['r_value_0', 'r_value_1']})
print('---')
print(l_df)
print('---')
print(r_df)
print('---')
print(pd.merge(l_df, r_df, on='key'))


