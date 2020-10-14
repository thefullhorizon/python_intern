# -*- coding=utf-8 -*-
from project.job.src.clean_data import clean_data
from project.job.src.crawl_data import crawl_data
from project.job.src.job_overall_analysis import analysis_between_job
from project.job.src.job_overall_analysis import analysis_job_between_city
from project.job.src.visualize_data import visualize_data

"""
该项目主要目的是想完整走一遍数据分析的流程：
    数据获取，数据清洗，数据建模，数据分析，数据可视化，数据报告。
    
该文件完成了两件事情  
    1.一个职位的详细分析
    2.从全国的维度上看职位的市场行情
初始日期：200928
城市坐标：上海   
参考地址：https://www.cnblogs.com/sui776265233/p/11146969.html

依次爬取 拉钩，智联，51Job，Boss, 猎聘网五大招聘网站，最好的招聘应该是平日里的自己通过能力来的积累。

"""

job_key = "财务"


def analysis_job_in_overall():
    """
    具体说明参见：job_overall_analysis文件
    :return:
    """
    analysis_between_job()
    analysis_job_between_city()


def detail_analysis_job_in_cities():
    """
    一个岗位在城市的维度上的深入洞察
    :return:
    """
    print("》》》 crawl data ")
    raw_data_path = crawl_data(job_key)
    print("》》》 clean data ")
    clean_data(job_key, raw_data_path)
    print("》》》 visualize data ")
    visualize_data(job_key, raw_data_path)
    # visualize_data(job_key, "20201011_android_raw.csv")


if __name__ == '__main__':
    """
    完整的数据分析步骤：
    爬取数据 -> 数据清洗 -> 数据建模 -> 数据分析 -> 数据可视化 -> 数据报告 
    """
    # detail_analysis_job_in_cities()
    analysis_job_in_overall()
    pass
