# -*- coding: utf-8 -*-
import time
import numpy as np
import pandas as pd
'''
时间：2020年04月06日17:09:35
问题：根据arrears表中的合同号筛选出invoice表里的快递号和接受人信息
耗时：It cost 2hour+ to work out

'''

start_time = time.time()

# 读取文件
arrears_file_data = pd.read_excel('arrears.xlsx', 'Table1', index_col=None, na_values=['NA'])
invoice_file_data = pd.read_excel('invoice.xlsx', '发票快递情况', index_col=None, na_values=['NA'])

# 提取数据
express_numbers = []
receivers = []
contract_number = arrears_file_data['Unnamed: 0']
for index, value in contract_number.iteritems():
    if isinstance(value, str) and 'JR' in value:
        need_data = invoice_file_data.loc[invoice_file_data['合同号'] == value]
        if need_data.empty:
            express_numbers.append('NAN')
            receivers.append('NAN')
        else:
            express_number = need_data.iloc[0, 0]
            receiver = need_data.iloc[0, 2]
            express_numbers.append(express_number)
            receivers.append(receiver)
    else:
        express_numbers.append('NAN')
        receivers.append('NAN')

# 生成数据
arrears_file_data.insert(1, 'express_number', express_numbers)
arrears_file_data.insert(1, 'receivers', receivers)

# 导出数据
arrears_file_data.to_excel('arrears_handled.xlsx', sheet_name='Sheet1')

print('complete successfully')
print((time.time() - start_time))
