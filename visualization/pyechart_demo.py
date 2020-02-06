# coding=utf-8

from __future__ import unicode_literals
from pyecharts import Bar, Gauge, Geo, Scatter3D, Page

render_address = r"d:\my_chart.html"

# 简单的生成一个bar
# bar = Bar("this is my first chart", "this a subtitle")
# bar.add("cloth", ["A", "B"], [5, 30])
# bar.show_config()
# bar.render(render_address)

# 简单的生成一个仪表盘

# gauge = Gauge("Gauge")
# gauge.add("A", "Complete", 95)
# gauge.show_config()
# gauge.render(render_address)

# 简单的生成一个空气质量图
data = [
    ("海南", 9), ("Shanghai", 12)]
geo = Geo("main cities air quality ", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color = '#404a59')
attr, value = geo.cast(data)
geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
# geo.add_coordinate("海南", 119.3, 26.08)
geo.show_config()
geo.render(render_address)

# scatter3D
# import random
# page = Page()
# data = [[random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)] for _ in range(80)]
# range_color = ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
#                '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
# scatter3D = Scatter3D("3D 散点图示例", width=1200, height=600)
# scatter3D.add("", data, is_visualmap=True, visual_range_color=range_color)
# page.add(scatter3D)
# page.render(render_address)