# -*- coding=utf-8 -*-
import os

import requests
import math
import time
import pandas as pd
from tqdm import tqdm


def get_json(job_key, url, num):
    """
    从指定的url中通过requests请求携带请求头和请求体获取网页中的信息,
    :return:
    """
    url1 = 'https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput='
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
        'kd': job_key}
    session = requests.Session()
    session.get(url=url1, headers=headers, timeout=3)
    cookie = session.cookies
    res = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3)
    res.raise_for_status()
    res.encoding = 'utf-8'
    page_data = res.json()
    return page_data


def get_page_num(count):
    """
    计算要抓取的页数，通过在拉勾网输入关键字信息，可以发现最多显示30页信息,每页最多显示15个职位信息
    :return:
    """
    page_num = math.ceil(count / 15)
    if page_num > 30:
        return 30
    else:
        return page_num


def get_page_info(jobs_list):
    """
    获取职位信息
    :param jobs_list:
    :return:
    """
    page_info_list = []
    for i in jobs_list:  # 循环每一页所有职位信息
        job_info = [i['companyFullName'], i['companyShortName'], i['companySize'], i['financeStage'], i['district'],
                    i['positionName'], i['workYear'], i['education'], i['salary'], i['positionAdvantage'],
                    i['industryField'], i['firstType'], i['companyLabelList'], i['secondType'], i['city']]
        page_info_list.append(job_info)
    return page_info_list


def crawl_data(job_key):
    """
    爬取数据核心方法
    :param job_key:
    :return:
    """
    url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    first_page = get_json(job_key, url, 1)
    total_page_count = first_page['content']['positionResult']['totalCount']
    num = get_page_num(total_page_count)
    total_info = []
    time.sleep(10)
    print("Total job count : {}, total page number:{}".format(total_page_count, num))
    for num in tqdm(range(1, num + 1)):
        # 获取响应json
        page_data = get_json(job_key, url, num)
        jobs_list = page_data['content']['positionResult']['result']  # 获取每页的所有python相关的职位信息
        page_info = get_page_info(jobs_list)
        total_info += page_info
        time.sleep(20)
        df = pd.DataFrame(data=total_info,
                          columns=['公司全名', '公司简称', '公司规模', '融资阶段', '区域',
                                   '职位名称', '工作经验', '学历要求', '薪资', '职位福利',
                                   '经营范围', '职位类型', '公司福利', '第二职位类型', '城市'])
    raw_csv_path = get_path(job_key)
    df.to_csv(raw_csv_path, index=False)
    return raw_csv_path


def get_path(job_key):
    """
    获取保存文件的路径
    :param job_key:
    :return:
    """
    save_dir = os.path.abspath(os.path.dirname(os.getcwd()))
    current_date = time.strftime("%Y%m%d", time.localtime())
    return save_dir + "/" + current_date + '_' + job_key + '_raw.csv'


def crawl_data_by_city(job_key, city):
    url = ' https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    if len(city) > 0:
        url += ("&city=" + city)
    first_page = get_json(job_key, url, 1)
    total_page_count = first_page['content']['positionResult']['totalCount']
    return total_page_count
