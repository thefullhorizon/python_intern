# coding=utf-8

from __future__ import unicode_literals
from pyecharts import WordCloud
from pyecharts import Bar, Gauge, Geo, Scatter3D, Page

render_address = r"my_chart.html"

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
# data = [
#     ("cn", 9), ("Shanghai", 12)]
# geo = Geo("main cities air quality ", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
# attr, value = geo.cast(data)
# geo.add("", attr, value, visual_range=[0, 200], visual_text_color="#fff", symbol_size=15, is_visualmap=True)
# geo.add_coordinate("cn", 119.3, 26.08)
# geo.show_config()
# geo.render(render_address)

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


name = ['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
value = [7000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
word_cloud = WordCloud(width=1300, height=620)
word_cloud.add("", name, value, word_size_range=[20, 100])
word_cloud.show_config()
word_cloud.render(render_address)
