# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

'''

学习时间：2020-04月
学习地址：https://www.bilibili.com/video/BV1Jx411L7LU?p=11
学习记录：
    2020-04-30 看完P12，做笔记
    2020-04-29 早上学习了半小时，过完了一遍 P12还没看
    2020-04-27 看完P15，注意P12还没没看
学习笔记：
    柱状图：
    Contours等高线图：
    Image图片：举例了一些
    3D图，展示3D的效果，这种方式比较形象的展示数据的结构
    Subplot共有3中方法让，多张子图显示在一张图上
    图中图实现方式
    次坐标轴：比如共享X轴，两边各一个坐标轴，这里有主次之分
    Animation动画：演示了正弦函数的动画演示，有点不太明白


    整体的感觉Matplotlib给人的感觉就是参数很多

'''


def draw_sin():
    fig, axe = plt.subplots()
    x = np.arange(0, 2*np.pi, 0.01)
    line, = axe.plot(x, np.sin(x))

    plt.show()


def draw_line():

    x = np.linspace(-5, 5, 10)

# 设置坐标刻度
    new_ticks = np.linspace(-10, 10, 5)
    plt.xticks(new_ticks)
    plt.yticks([-3, 3], [
        r'$no$', r'$ok\ yeah$'
    ])

# 移动坐标的中心点
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['left'].set_position(('data', 0))

# 初始化两个函数
#   plt.figure(figsize=(6, 7))
    line01, = plt.plot(x, x + 1, color='red', linewidth=2.0, linestyle='--')
    line02, = plt.plot(x, x ** 2, color='blue', linewidth=2.0, linestyle='--')
    plt.xlim((-10, 10))
    plt.ylim((-10, 10))
    plt.xlabel('x label')
    plt.ylabel('y label')

    x0 = 3
    y0 = x0 + 1
    plt.scatter(x0, y0, s=30, color='green')
    plt.plot([x0, x0], [y0, 0], '--', lw=1.5)
    plt.annotate(r'$x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+20, -30), textcoords='offset points',
                 arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=.2'))

    plt.legend(handles=[line01, line02], labels=['horizon', 'cucumber'], loc='lower right')
    plt.show()


def draw_scatter():
    """
    散点图
    """
    np.random.seed(19680801)
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

    plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    plt.show()


def draw_bar():
    """
    柱状图
    """
    N = 12
    x = np.arange(N)
    print(x)
    y = (1 - x/float(N)) * np.random.uniform(0.5, 1.0, N)
    plt.bar(x, y, facecolor='#c3f3c3', edgecolor='white')
    for m, n in zip(x, y):
        plt.text(m, n + 0.02, '%.2f' % n, ha='center', va='bottom')

    plt.xticks(())
    plt.yticks(())

    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.show()


if __name__ == '__main__':
    draw_sin()
    # draw_line()
    # draw_scatter()
    # draw_bar()

