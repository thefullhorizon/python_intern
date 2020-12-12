# -*- coding=utf-8 -*-
import datetime

from project.job.src.la_gou import analyze_job_la_gou, analyze_job_special
from project.job.utils.util_common import get_file_name

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

# True表示针对某一职位专项爬虫
# False表示快速爬虫方式
normal_crawl = False

if __name__ == '__main__':

    if normal_crawl:
        start_time = datetime.datetime.now()
        # 爬取某个职位详细的全国数据并分析: 数据分析, android, java
        job = "数据分析"
        # 定义任务完后给到通知对象的一个邮件配图
        file_name = get_file_name(job, "la_gou")
        # 定义任务完成后的通知对象
        send_who = ['1013629814@qq.com']
        # send_who = ['1510691263@qq.com']
        analyze_job_la_gou(job, file_name, send_who)
        cost = datetime.datetime.now() - start_time
        print('It costs {}'.format(cost))
    else:
        # 快速获取某个职位在主要城市上的总数值数据
        start_time = datetime.datetime.now()
        jobs = ['数据分析', '数据科学家', '大数据开发', '数据挖掘', 'Java', 'Android']
        cities = ["北京", "上海", "深圳", "广州", "杭州",
                  "南京", "成都", "重庆", "武汉", "郑州",
                  "西安", "苏州"]
        analyze_job_special(jobs, cities)
        analyze_cost_time = datetime.datetime.now() - start_time
        print('It totally cost{}'.format(analyze_cost_time))
    pass
