# -*- coding=utf-8 -*-
import datetime

import numpy as np

from app.email_util import QQClient
from project.job.utils.util_visualize import visualize_two_dimension, get_sign
import requests
import math
import time
import pandas as pd
from tqdm import tqdm
import jieba
from wordcloud import WordCloud
from project.job.utils.util_common import get_cities
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

    def __init__(self, job, file_name):
        self.job = job
        self.raw_data_path = file_name
        pass

    def crawl_data(self):
        """
        爬取一个职位在全国的数据
        :return:
        """
        total_info = []
        cities_districts = get_cities()
        for city in cities_districts.keys():
            districts = cities_districts[city]
            city_info = []
            print("start crawl " + city + " data")
            # TODO 这里尝试使用多线程方式显示爬虫
            for district in tqdm(districts):
                city_info += self.__crawl_data(city, district)
            total_info += city_info
            print("Job in {} total count is : {} \n".format(city, str(len(city_info))))
        need_columns = ['公司全名', '公司简称', '公司规模', '融资阶段', '区域',
                        '职位名称', '工作经验', '学历要求', '薪资', '职位福利',
                        '经营范围', '职位类型', '公司福利', '第二职位类型', '城市', '区域']
        new_df = pd.DataFrame(data=total_info, columns=need_columns)
        new_df.to_csv(self.raw_data_path, index=False)
        print("It crawl {} count job data".format(str(len(total_info))))

    def __crawl_data(self, city, district=None):
        """
        爬取数据核心方法
        """
        url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        if city is not None:
            url += "&city=" + city
        if district is not None:
            print("\ncrawling " + district)
            url += "&district=" + district
        first_page = LaGouUtil.get_json(self.job, url, 1)
        total_count = first_page['content']['positionResult']['totalCount']
        num = self.__get_page_num(total_count)
        total_info = []
        time.sleep(2)
        for num in range(1, num + 1):
            page_data = LaGouUtil.get_json(self.job, url, num)
            jobs_list = page_data['content']['positionResult']['result']
            page_info = self.__get_page_info(jobs_list)
            total_info += page_info
            time.sleep(3)
        return total_info

    @staticmethod
    def __get_page_num(total_count):
        """
        :return: 根据职位总数计算总的分页数
        """
        page_num = math.ceil(total_count / 15)
        if page_num > 30:
            return 30
        else:
            return page_num

    @staticmethod
    def __get_page_info(jobs_list):
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
                        i['industryField'], i['firstType'], i['companyLabelList'], i['secondType'], i['city'],
                        i['district']]
            page_info_list.append(job_info)
        return page_info_list

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
            if int_list.__len__() == 2:
                avg_salary = int_list[0] + (int_list[1] - int_list[0]) / 4
                avg_salary_list.append(avg_salary)
            else:
                print("---------exception---------")
                avg_salary_list.append(0)
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

    @staticmethod
    def __visualize_city_pie(df):
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

    def __visualize_city_bar(self, df, pic_path):
        """
        以柱状图的形式职位数在城市维度上的分布情况
        :param pic_path 保存的图片绝对地址
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
        plt.title("岗位：{} | 总量：{}".format(self.job, str(df.shape[0])))
        # 如果X轴的坐标 文字的坐标比较长的时候可以考虑这样的旋转
        # plt.xticks(np.arange(len(keys))+1, keys, size='small', rotation=30)
        plt.xlabel("城市\n\n" + get_sign("拉勾"))
        plt.ylabel("数量")
        plt.legend(["x"])
        # plt.grid()
        plt.bar(keys, values)
        for a, b in zip(keys, values):
            plt.text(a, b + 0.05, '%.0f' % b, ha='center', va='bottom', fontsize=12)
        plt.savefig(pic_path)
        plt.show()

    @staticmethod
    def __visualize_city_cloud(df):
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

    def __visualize_city_map(self, df):
        """
        TODO 地图可视化
        :param df:
        :return:
        """
        pass

    def visualize_data(self, pic_name):
        """
        一个职位的全国数据可视化
        """
        df = pd.read_csv(self.raw_data_path, encoding='utf-8')
        # df = pd.read_csv("20201021_raw_财务_la_gou.csv", encoding='utf-8')
        # self.__visualize_salary_hist(df)
        # self.__visualize_city_pie(df)
        self.__visualize_city_bar(df, pic_name)
        # self.__visualize_city_cloud(df)
        return df.shape[0]


class LaGouFast:
    """
        因为拉钩每页展示15天，总共可以展示30页，也就是说只能拿去450条数据，无法拿去全部数据
        但可以进行如下的分析：
        * 分析不同职业在全国维度上的数量情况      -> analysis_between_job()
        * 分析同一职业在不同城市维度上的数量情况   -> analysis_job_between_city()
    """

    @staticmethod
    def fast_analysis_between_job(jobs):
        """
        快速分析不同职业在全国维度上的数量情况
        :param jobs: 职业(数组)
        """
        job_numbers = []
        for job in jobs:
            total_count = LaGouFast.__crawl_job_by_city(job)
            print(job + " total count\t\t: " + str(total_count))
            job_numbers.append(total_count)
        title = "analysis between job"
        visualize_two_dimension(title, jobs, np.array(job_numbers))

    def fast_analysis_job_between_city(self, jobs, cities):
        """
        快速分析同一职业在不同城市维度上的数量情况
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

    @staticmethod
    def __crawl_job_by_city(job, city=None):
        """
        :param city :指定城市
        :return     :获取某个职位在某个城市下的职位总数，如果city为空则表示获取全国数据
        """
        url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        if city is not None:
            url += ("&city=" + city)
        first_page = LaGouUtil.get_json(job, url, 1)
        return first_page['content']['positionResult']['totalCount']


class LaGouUtil:
    @staticmethod
    def get_json(job, url, num):
        """
        :param job: 职位
        :param url 获取职位的url
        :param num 页数，默认第一页
        :return: 从指定的url中通过requests请求携带请求头和请求体获取网页中的职位的Json信息
        """
        __url = 'https://www.lagou.com/jobs/list_'+job
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': ('https://www.lagou.com/jobs/list_'+job+'/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=').encode('utf-8'),
            'X-Anit-Forge-Code': '0',
            'X-Anit-Forge-Token': 'None',
            'X-Requested-With': 'XMLHttpRequest'
        }

        data = {
            'first': 'true',
            'pn': num,
            'kd': job.encode('utf-8')}
        try:
            # 建立session并拿到cookies
            session = requests.Session()
            session.get(url=__url.encode('utf-8'), headers=headers, timeout=3)
            cookie = session.cookies
            res = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3)
            res.raise_for_status()
            res.encoding = 'utf-8'
            return res.json()
        except IOError:
            print("It occurs some exception")


def analyze_job_la_gou(job, file_name, send_who):
    """
    针对一个职位进行分析
    :param send_who:
    :param file_name: 文件的名字
    :param job:
    """
    start_time = datetime.datetime.now()
    # 初始化
    la_gou = LaGou(job, file_name + '.csv')
    # 爬取
    la_gou.crawl_data()
    # 清洗
    la_gou.clean_data()
    # 可视化
    accessory_pic = file_name + ".png"
    data_count = la_gou.visualize_data(accessory_pic)

    # 输出
    # TODO 形式一：自动化报表 形式二：文章  形式三：数据看板

    # 结果通知(仅仅用作任务完后的通知)
    # 方式一：邮件[OK]  方式二：微信 方式三 更新到数据看板
    analyze_cost_time = datetime.datetime.now() - start_time
    notification = "It costs {} and handle {} pieces data".format(analyze_cost_time, str(data_count))
    print(notification)

    title = "{} job analysis result".format(job)
    content = "Successfully! you could have a overall cognition with the visualization picture. <br>{}".format(notification)
    client_qq = QQClient(send_who)
    client_qq.text_with_image(title, content, accessory_pic)


def analyze_job_special(jobs, cities):
    """
    自定义的从整体上分析职位
    :param jobs:
    :param cities:
    """
    start_time = datetime.datetime.now()
    la_gou_fast = LaGouFast()
    la_gou_fast.fast_analysis_between_job(jobs)
    la_gou_fast.fast_analysis_job_between_city(jobs, cities)
    analyze_cost_time = datetime.datetime.now() - start_time
    print("It totally cost " + analyze_cost_time)
