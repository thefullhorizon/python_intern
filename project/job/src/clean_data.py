# -*- coding=utf-8 -*-
import pandas as pd


def clean_data(job_key, raw_data_path):
    """
    对爬取的原始数据进行简单的数据处理
    :param job_key: 用户搜索关键字
    :param raw_data_path:原始数据存储的CSV
    :return: 处理之后的数据路径
    """

    df = pd.read_csv(raw_data_path, encoding='utf-8')

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
    df.to_csv(raw_data_path, index=False)
