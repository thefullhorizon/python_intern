# -*- coding=utf-8 -*-
import datetime
from collections import Iterable

import numpy as np
from app.email_util import QQClient
from project.job.utils.util_visualize import visualize_two_dimension, get_sign
import requests
import math
import time
import pandas as pd
from tqdm import tqdm
from project.job.utils.util_common import get_cities
from pylab import mpl
import matplotlib.pyplot as plt


"""

以拉钩为数据来源，进行数据爬虫，分析部分统一在Notebook上进行

Author       :   Cucumber
Date         :   10/14/20

"""
# 使用matplotlib能够显示中文
mpl.rcParams['font.sans-serif'] = ['Arial Unicode MS']
mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题


class LaGou:

    def __init__(self, job, file_path):
        self.job = job
        self.raw_data_path = file_path
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
                        '经营范围', '职位类型', '公司福利', '第二职位类型', '城市']
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
            if not isinstance(page_data, dict):
                continue
            try:
                jobs_list = page_data['content']['positionResult']['result']
                page_info = self.__get_page_info(jobs_list)
                if page_info is None:
                    continue
                total_info += page_info
                time.sleep(3)
            except TypeError:
                print("TypeError: 'NoneType' object is not subscriptable")
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
        if not isinstance(jobs_list, Iterable):
            return
        page_info_list = []
        for i in jobs_list:
            job_info = [i['companyFullName'], i['companyShortName'], i['companySize'], i['financeStage'], i['district'],
                        i['positionName'], i['workYear'], i['education'], i['salary'], i['positionAdvantage'],
                        i['industryField'], i['firstType'], i['companyLabelList'], i['secondType'], i['city']]
            page_info_list.append(job_info)
        return page_info_list

    @staticmethod
    def __clean_operation(content):
        print(content)
        if isinstance(content, str) and "移动互联网," in content:
            return content.replace("移动互联网,", "")
        else:
            return content

    def clean_data(self):
        """
        对爬取的原始数据进行简单的数据处理
        """
        df = pd.read_csv(self.raw_data_path, encoding='utf-8')
        # 过滤掉实习岗位
        df.drop(df[df['职位名称'].str.contains('实习')].index, inplace=True)
        # 如果经营范围已经有具体的分类时,就去掉经营范围值中的"移动互联网,"
        df['经营范围'] = df['经营范围'].apply(lambda x: self.__clean_operation(x))

        # 由于csv文件中的字符是字符串形式，先用正则表达式将字符串转化为列表，在取区间的均值
        pattern = r'\d+'
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

    def __visualize_city_bar_for_email(self, df, pic_path):
        """
        以柱状图的形式职位数在城市维度上的分布情况
        :param pic_path 保存的图片绝对地址
        """
        city = df['城市'].value_counts()
        keys = city.index
        values = city.values

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
        __url = 'https://www.lagou.com/jobs/list_' + job
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'Host': 'www.lagou.com',
            'Referer': (
                        'https://www.lagou.com/jobs/list_' + job + '/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput=').encode(
                'utf-8'),
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
    file_path = file_name + '.csv'
    la_gou = LaGou(job, file_path)
    # 爬取
    la_gou.crawl_data()
    # 清洗
    la_gou.clean_data()

    # 注：在Jupyter Notebook上进行可视化

    # 结果通知(仅仅用作任务完后的通知)
    # 方式一：邮件[OK]  方式二：微信 方式三 更新到数据看板
    pic_path = file_name + '.png'
    generate_pic(file_path, pic_path)
    analyze_cost_time = datetime.datetime.now() - start_time
    title = "{} job analysis result".format(job)
    content = "Successfully! you could have a overall cognition with the visualization picture. <br>It costs {}".format(analyze_cost_time)
    client_qq = QQClient(send_who)
    client_qq.text_with_image(title, content, pic_path)


def generate_pic(file_path, pic_path):
    """
    生成发送邮件需要中携带的概要图
    :param file_path:
    :param pic_path:
    :return:
    """
    data = pd.read_csv(file_path)
    need_data = data.groupby('城市').size().sort_values(ascending=True)
    plt.barh(need_data.index, need_data.values)
    plt.savefig(pic_path)
    plt.title("样本数：{}".format(data.shape[0]))
    plt.xlabel("\n" + get_sign("拉勾"))
    plt.show()


def analyze_job_special(jobs, cities):
    """
    自定义的从整体上分析职位
    :param jobs:
    :param cities:
    """
    la_gou_fast = LaGouFast()
    la_gou_fast.fast_analysis_between_job(jobs)
    la_gou_fast.fast_analysis_job_between_city(jobs, cities)

