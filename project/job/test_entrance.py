# -*- coding=utf-8 -*-
import datetime
import time

from project.job.src.la_gou import analyze_job_base_la_gou
from project.job.src.la_gou import analyze_job_special

"""
>>>该项目主要目的是想完整走一遍数据分析的流程：
    -> 用户输入（小程序, Web, 客户端(Flutter方案)）
        -> 爬取数据 -> 数据清洗 -> 数据建模 -> 数据分析 -> 数据可视化
            -> 数据报告/自动化生成报告（尝试MarkDown文本）
            
>>>依次爬取 拉钩，智联，51Job，Boss, 猎聘网五大招聘网站
    其实最好的招聘应该是平日里的自己通过能力来的积累。

>>>该文件完成了两件事情  
    1.一个职位的详细分析
    2.从全国的维度上看职位的市场行情
    
>>>完后状态跟踪：
    目前初步完成了以拉钩为平台的职位数据分析
   
Initial Date    : 200928
Location city   : Shanghai   
Reference       : https://www.cnblogs.com/sui776265233/p/11146969.html
Author          : Cucumber
Date            : 09/28/20
"""
if __name__ == '__main__':
    job = "android"
    start_time = datetime.datetime.now()
    analyze_job_base_la_gou(job)
    print(datetime.datetime.now()-start_time)

    # jobs = ['财务', '会计', '数据分析', 'java', 'android']
    # cities = ["北京", "上海", "深圳", "广州", "杭州",
    #           "南京", "成都", "重庆", "武汉", "郑州",
    #           "西安", "苏州"]
    # analyze_job_special(jobs, cities)
    pass
