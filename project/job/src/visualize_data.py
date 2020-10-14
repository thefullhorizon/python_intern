# -*- coding=utf-8 -*-
import time

import matplotlib.pyplot as plt
import pandas as pd
from pylab import mpl
import jieba
from wordcloud import WordCloud
# from selenium import webdriver
# from scipy.misc import imread
# from imageio import imread
# import statsmodels.api as sm
# from pyecharts import Bar

# 使用matplotlib能够显示中文
from project.job.src.common_util import open_url

mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


def visualize_salary(job_key, df):
    """
    以直方图的形式查看薪资分布
    """
    # 绘制python薪资的频率直方图并保存
    plt.hist(df['月薪'], bins=8, facecolor='#ff6700', edgecolor='blue')  # bins是默认的条形数目
    plt.title(job_key + ' 职位\n')
    plt.xlabel('薪资(单位/千元) \n\n' + get_sign())
    plt.ylabel('频数/频率')
    # plt.savefig('python薪资分布.jpg')
    plt.show()


def visualize_city_pie(df):
    """
    以饼图的形式职位数在城市维度上的分布情况
    """
    # 绘制饼状图并保存
    city = df['城市'].value_counts()
    label = city.keys()
    city_list = []
    count = 0
    n = 1
    distance = []
    for i in city:
        print(i)
        city_list.append(i)
        count += 1
        if count > 5:
            n += 0.1
            distance.append(n)
        else:
            distance.append(0)
    plt.pie(city_list, labels=label, labeldistance=1.2, autopct='%2.1f%%', pctdistance=0.6, shadow=True,
            explode=distance)
    plt.axis('equal')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.1, 1))
    # plt.savefig('python地理位置分布图.jpg')
    plt.show()


def visualize_city_bar(job_key, df):
    """
    以柱状图的形式职位数在城市维度上的分布情况
    """
    city = df['城市'].value_counts()
    keys = city.index
    values = city.values

    # 使用epychart
    # bar = Bar("python职位的城市分布图")
    # bar.add("城市", keys, values)
    # bar.print_echarts_options()  # 该行只为了打印配置项，方便调试时使用
    # result_url = "/Users/nashan/Documents/WS/pycharm/python_learning/project/job/a.html"
    # bar.render(path=result_url)
    # open_url(result_url)

    # 使用matplotlib进行展示
    plt.figure(figsize=(10, 6))
    plt.title(job_key + " 职位数量在不同城市中的对比\n")
    plt.xlabel("城市\n\n" + get_sign())
    plt.ylabel("数量")
    plt.bar(keys, values)
    plt.show()


def visualize_two_dimension(title, keys, values):
    # plt.figure(figsize=(10, 6))
    plt.title(title)
    plt.bar(keys, values)
    plt.show()


def visualize_city_cloud(df):
    """
    绘制福利待遇的词云
    """
    text = ''
    for line in df['公司福利']:
        if len(eval(line)) == 0:
            continue
        else:
            for word in eval(line):
                # print(word)
                text += word

    cut_word = ','.join(jieba.cut(text))
    # word_background = imread('公主.jpg')
    cloud = WordCloud(
        font_path=r'/Users/nashan/Documents/WS/pycharm/python_learning/project/job/song.ttf',
        background_color='white',
        # mask=word_background,
        max_words=500,
        max_font_size=100,
        width=1024,
        height=500

    )
    word_cloud = cloud.generate(cut_word)
    # word_cloud.to_file('福利待遇词云.png')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


def get_sign():
    current_date = time.strftime("%Y-%m-%d", time.localtime())
    return current_date + " / " + "拉勾" + " / " + "环岛"


def visualize_data(job_key, clean_data):

    df = pd.read_csv(clean_data, encoding='utf-8')
    visualize_salary(job_key, df)
    # visualize_city_pie(df)
    visualize_city_bar(job_key, df)
    # visualize_city_cloud(df)
