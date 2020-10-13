# -*- coding=utf-8 -*-

"""
因为拉钩每页展示15天，总共可以展示30页，也就是说只能拿去450条数据，无法拿去全部数据
但可以进行如下的分析：
* 分析不同职业在全国维度上的数量情况      -> analysis_between_job()
* 分析同一职业在不同城市维度上的数量情况   -> analysis_job_between_city()
"""
import numpy as np
from project.crawler_job.src.crawl_data import crawl_data_by_city
from project.crawler_job.src.visualize_data import visualize_two_dimension


def analysis_between_job():
    jobs = ['财务', '会计', '数据分析', 'java', 'android']
    job_numbers = []
    for job in jobs:
        total_number = crawl_data_by_city(job, '')
        print("全国" + job + "总数: " + str(total_number))
        job_numbers.append(total_number)
    title = "analysis between job"
    visualize_two_dimension(title, jobs, np.array(job_numbers))


def analysis_job_between_city():
    jobs = ['财务', '会计']
    # jobs = ['数据分析', 'java', 'android']
    cities = ["北京", "上海", "深圳", "广州", "杭州",
              "南京", "成都", "重庆", "武汉", "郑州",
              "西安", "苏州"]
    job_numbers = []
    for job in jobs:
        total_number = crawl_data_by_city(job, '')
        print("全国" + job + "总数: " + str(total_number))
        job_numbers.clear()
        for city in cities:
            job_number_in_city = crawl_data_by_city(job, city)
            print(city + " ： " + str(job_number_in_city))
            job_numbers.append(job_number_in_city)
        title = job + " / " + str(total_number)
        visualize_two_dimension(title, cities, np.array(job_numbers))
