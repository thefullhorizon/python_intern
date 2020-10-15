# -*- coding=utf-8 -*-
import numpy as np
from project.job.utils.util_visualize import visualize_two_dimension, get_sign
import os
import requests
import math
import time
import pandas as pd
from tqdm import tqdm
import jieba
from wordcloud import WordCloud
# from selenium import webdriver
# from scipy.misc import imread
# from imageio import imread
# import statsmodels.api as sm
# from pyecharts import Bar
from project.job.utils.util_common import get_current_date
from pylab import mpl
import matplotlib.pyplot as plt

"""

以拉钩为数据来源，对职业进行数据分析

Author       :   Cucumber
Date         :   10/14/20

"""
# 使用matplotlib能够显示中文
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class LaGou:

    def __init__(self, job):
        self.job = job
        self.raw_data_path = self.__get_path()
        pass

    def crawl_data(self):
        """
        爬取数据核心方法
        """
        url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        first_page = self.__get_json(self.job, url, 1)
        total_count = first_page['content']['positionResult']['totalCount']
        num = self.__get_page_num(total_count)
        print("Total job count : {}, total page number:{}".format(total_count, num))
        total_info = []
        time.sleep(2)
        print("")
        for num in tqdm(range(1, num + 1)):
            page_data = self.__get_json(self.job, url, num)
            jobs_list = page_data['content']['positionResult']['result']
            page_info = self.__get_page_info(jobs_list)
            total_info += page_info
            time.sleep(2)
            df = pd.DataFrame(data=total_info,
                              columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域',
                                       '职位名称', '工作经验', '学历要求', '薪资', '职位福利',
                                       '经营范围', '职位类型', '公司福利', '第二职位类型', '城市'])

        df.to_csv(self.raw_data_path, index=False)

    def __get_json(self, job, url, num=1):
        """
        TODO 按照爬取主要城市所有区的形式，绕过30页的限制，爬取更多的数据，力求数据更加全面
        :param url 获取职位的url
        :param num 页数，默认第一页
        :return: 从指定的url中通过requests请求携带请求头和请求体获取网页中的职位的Json信息
        """
        __url = 'https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput='
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': 'https://www.lagou.com/jobs/list_%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90?labelWords=&fromSearch=true&suginput=',
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        }

        data = {
            'first': 'true',
            'pn': num,
            'kd': job}
        # 建立session并拿到cookies
        session = requests.Session()
        session.get(url=__url, headers=headers, timeout=3)
        cookie = session.cookies
        res = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3)
        res.raise_for_status()
        res.encoding = 'utf-8'
        page_data = res.json()
        return page_data

    def __get_page_num(self, total_count):
        """
        :return: 根据职位总数计算总的分页数
        """
        page_num = math.ceil(total_count / 15)
        if page_num > 30:
            return 30
        else:
            return page_num

    def __get_page_info(self, jobs_list):
        """
        TODO 这里可以有两个优化点
            1. 需要的数据封装成对象
            2. json与对象的转换
            3. 需要的字段与其对应的中文描述对应起来
        :param jobs_list:
        :return: 获取职位详细信息
        """
        page_info_list = []
        for i in jobs_list:
            job_info = [i['companyFullName'], i['companyShortName'], i['companySize'], i['financeStage'], i['district'],
                        i['positionName'], i['workYear'], i['education'], i['salary'], i['positionAdvantage'],
                        i['industryField'], i['firstType'], i['companyLabelList'], i['secondType'], i['city']]
            page_info_list.append(job_info)
        return page_info_list

    def __get_path(self):
        """
        :return     :获取保存文件的路径
        """

        return get_current_date() + '_' + self.job + '_raw.csv'

    def __crawl_job_by_city(self, job, city=None):
        """
        :param city :指定城市
        :return     :获取某个职位在某个城市下的职位总数，如果city为空则表示获取全国数据
        """
        url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        if city is not None:
            url += ("&city=" + city)
        first_page = self.__get_json(job, url)
        total_page_count = first_page['content']['positionResult']['totalCount']
        return total_page_count

    def clean_data(self):
        """
        对爬取的原始数据进行简单的数据处理
        """
        df = pd.read_csv(self.raw_data_path, encoding='utf-8')
        # 进行数据清洗，过滤掉实习岗位
        # df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)
        # print(df.describe())
        # 由于csv文件中的字符是字符串形式，先用正则表达式将字符串转化为列表，在取区间的均值
        pattern = '\d+'
        # print(df['工作经验'], '\n\n\n')
        # print(df['工作经验'].str.findall(pattern))
        df['工作年限'] = df['工作经验'].str.findall(pattern)
        avg_work_year = []
        count = 0
        for i in df['工作年限']:
            # 如果工作经验为'不限'或'应届毕业生',那么匹配值为空,工作年限为0
            if len(i) == 0:
                avg_work_year.append(0)
                count += 1
            # 如果匹配值为一个数值,那么返回该数值
            elif len(i) == 1:
                avg_work_year.append(int(''.join(i)))
                count += 1
            # 如果匹配为一个区间则取平均值
            else:
                num_list = [int(j) for j in i]
                avg_year = sum(num_list) / 2
                avg_work_year.append(avg_year)
                count += 1

        df['avg_work_year'] = avg_work_year
        # 将字符串转化为列表,薪资取最低值加上区间值得25%，比较贴近现实
        df['salary'] = df['薪资'].str.findall(pattern)

        avg_salary_list = []
        for k in df['salary']:
            int_list = [int(n) for n in k]
            avg_salary = int_list[0] + (int_list[1] - int_list[0]) / 4
            avg_salary_list.append(avg_salary)
        df['月薪'] = avg_salary_list
        df.to_csv(self.raw_data_path, index=False)

#   ----- 可视化部分 -----
    def __visualize_salary_hist(self, df):
        """
        以直方图的形式查看薪资分布
        """
        # 绘制python薪资的频率直方图并保存
        plt.hist(df['月薪'], bins=8, facecolor='#ff6700', edgecolor='blue')  # bins是默认的条形数目
        plt.title("Post：" + self.job + " \n")
        plt.xlabel('薪资(单位/千元)\n\n' + get_sign("拉勾"))
        plt.ylabel('频数/频率')
        # plt.savefig('python薪资分布.jpg')
        plt.show()

    def __visualize_city_pie(self, df):
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

    def __visualize_city_bar(self, df):
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
        plt.title("Post：" + self.job + " \n")
        plt.xlabel("城市\n\n" + get_sign("拉勾"))
        plt.ylabel("数量")
        plt.bar(keys, values)
        plt.show()

    def __visualize_city_cloud(self, df):
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

    def visualize_data(self):
        df = pd.read_csv(self.raw_data_path, encoding='utf-8')
        # self.__visualize_salary_hist(df)
        # self.__visualize_city_pie(df)
        self.__visualize_city_bar(df)
        # self.__visualize_city_cloud(df)

    """
        因为拉钩每页展示15天，总共可以展示30页，也就是说只能拿去450条数据，无法拿去全部数据
        但可以进行如下的分析：
        * 分析不同职业在全国维度上的数量情况      -> analysis_between_job()
        * 分析同一职业在不同城市维度上的数量情况   -> analysis_job_between_city()
    """
    def analysis_between_job(self, jobs):
        """
        分析不同职业在全国维度上的数量情况
        :param jobs: 职业(数组)
        """
        job_numbers = []
        for job in jobs:
            total_count = self.__crawl_job_by_city(job)
            print(job + " total count\t\t: " + str(total_count))
            job_numbers.append(total_count)
        title = "analysis between job"
        visualize_two_dimension(title, jobs, np.array(job_numbers))

    def analysis_job_between_city(self, jobs, cities):
        """
        分析同一职业在不同城市维度上的数量情况
        :param jobs     : 职业(数组) 有几张图片就会生成几张分析图片
        :param cities   : 城市(数组)
        """
        job_numbers = []
        for job in jobs:
            total_count = self.__crawl_job_by_city(job)
            print(job + " total count\t\t: " + str(total_count))
            job_numbers.clear()
            for city in cities:
                job_number_in_city = self.__crawl_job_by_city(job, city)
                print(city + " \t： " + str(job_number_in_city))
                job_numbers.append(job_number_in_city)
            title = "Post: " + job + " / Total: " + str(total_count)
            visualize_two_dimension(title, cities, np.array(job_numbers))


def analyze_job_base_la_gou(job, jobs, cities):

    # 初始化
    la_gou = LaGou(job)
    # 爬取
    la_gou.crawl_data()
    # 清洗
    la_gou.clean_data()
    # 可视化
    la_gou.visualize_data()
    # 分析 -> 生成自动化报表（TODO 暂定MarkDown格式）

# 以下独立分析
    la_gou.analysis_between_job(jobs)
    la_gou.analysis_job_between_city(jobs, cities)

