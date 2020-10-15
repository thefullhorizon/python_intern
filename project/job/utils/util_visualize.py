# -*- coding=utf-8 -*-
import matplotlib.pyplot as plt
from pylab import mpl
from project.job.utils.util_common import get_current_date

# 使用matplotlib能够显示中文
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def visualize_two_dimension(title, keys, values):
    """
    可视化一个二维的关系，比如城市（横坐标）在数量（纵坐标）上的关系
    :param title:
    :param keys:
    :param values:
    """
    plt.title(title+"\n")
    plt.xlabel("\n" + get_sign("拉勾"))
    plt.bar(keys, values)
    plt.show()


def get_sign(platform):
    """
    :param platform: 平台如拉勾
    :return: 获取可视化图底部的签名信息
    """
    return get_current_date() + " / " + platform + " / " + "环岛"

