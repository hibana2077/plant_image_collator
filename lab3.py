'''
Author: hibana2077 hibana2077@gmail.com
Date: 2023-11-30 13:52:11
LastEditors: hibana2077 hibana2077@gmail.com
LastEditTime: 2023-11-30 15:47:55
FilePath: \plant_image_collator\lab3.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import pandas as pd
from plotly import express as px
from plotly import graph_objects as go

data = {
    "time": ['1','1','2','2','3','3','4','4','5','5'],
    "cpu": [11,12,13,12,11,12,13,12,11,12],
    "memory": [21,22,23,22,21,22,23,22,21,22],
    "node_name": ['node1','node2','node1','node2','node1','node2','node1','node2','node1','node2']
}

df = pd.DataFrame(data)
df = df.set_index("time")
df = df.sort_index()

df_node_mean = df.groupby("node_name").mean(numeric_only=True)
print(df_node_mean)

df_temp = df.groupby("node_name")
print(df_temp.get_group("node1"))
fig = go.Figure()
fig.add_trace(go.Line(x=df_temp.get_group("node2").index, y=df_temp.get_group("node2")["cpu"], name="node2"))
fig.add_trace(go.Line(x=df_temp.get_group("node2").index, y=df_temp.get_group("node2")["memory"], name="node2"))
fig.show()
print(df_temp.groups.keys())

df_time_mean = df.groupby("time").mean(numeric_only=True)
print(df_time_mean.iloc[-1])