import streamlit as st
import pandas as pd
from io import BytesIO
from datetime import datetime
from os import getenv
from requests import get
from base64 import b64decode
from plotly import express as px

def init():
    st.session_state["login"] = True
    st.session_state["api_url"] = "http://api:5000/"

def login():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == getenv("USERNAME") and password == getenv("PASSWORD"):
            st.session_state["login"] = True
            st.success("Login success")
            st.rerun()
        else:
            st.error("Login fail")

def caculate_metrics():
    status = get(st.session_state["api_url"]+"status")
    if status.status_code != 200:
        st.error("Get status fail")
        return None,None,None,None,None,None
    status = status.json()
    if len(status) == 0:
        st.warning("No status")
        return None,None,None,None,None,None
    df_status = pd.DataFrame(status)
    df_status = df_status.set_index("time")
    df_status = df_status.sort_index()
    df_node_mean = df_status.groupby("node_name").mean(numeric_only=True)
    df_node = df_status.groupby("node_name")
    df_time_mean = df_status.groupby("time").mean(numeric_only=True)
    last_cpu_time_mean = df_time_mean.iloc[-1]["cpu"]
    last_memory_time_mean = df_time_mean.iloc[-1]["memory"]
    diff_cpu_time_mean = df_time_mean.diff().iloc[-1]["cpu"]
    diff_memory_time_mean = df_time_mean.diff().iloc[-1]["memory"]
    return last_cpu_time_mean,last_memory_time_mean,diff_cpu_time_mean,diff_memory_time_mean,df_node_mean,df_node

def photo():
    #get photo
    response = get(st.session_state["api_url"]+"photo")
    if response.status_code != 200:
        st.error("Get photo fail")
        return None
    response = response.json()
    # return's photo is in base64 format
    # decode it
    image_data = {}
    for i in response:
        if i["node_name"] not in image_data:
            image_data[i["node_name"]] = []
    for i in response:
        image_data[i["node_name"]].append({
            "image": BytesIO(b64decode(i["image"])),
            "time": datetime.strptime(i["time"], "%Y-%m-%d %H:%M:%S"),
            "plant_name": i["plant_name"],
            "node_name": i["node_name"]
        })
    return image_data

def dowload_all_photo():
    #get photo
    response = get(st.session_state["api_url"]+"photo")
    if response.status_code != 200:
        st.error("Get photo fail")
        return None
    response = response.json()
    # change to dataframe
    df = pd.DataFrame(response)
    # return dataframe in csv format
    return df

def caculate_diff(in_value:int | float | None):
    if in_value is None:return 0
    return in_value

def main():
    if st.session_state["login"]:
        
        st.title("Plant Image Collator Dashboard")
        # Mertics logic
        col1,col2,col3 = st.columns(3)
        cpu,memory,diff_cpu,diff_memory,df_node_mean,df_node = caculate_metrics()
        col1.metric("CPU", f"{cpu} %", f"{caculate_diff(diff_cpu)} %")
        col2.metric("Memory", f"{memory} %", f"{caculate_diff(diff_memory)} %")
        col3.metric("Status", "OK")# need to add error status logic
        
        # Status logic
        st.header("Status")
        st.subheader("CPU")
        if cpu not in [None,0]:
            df_node_mean = df_node_mean.reset_index()
            st.dataframe(df_node_mean)
            fig_cpu = px.bar(df_node_mean, x=df_node_mean.index, y="cpu", color="node_name", barmode="group")
            st.plotly_chart(fig_cpu, use_container_width=True)
        else:
            st.warning("No CPU data")
        st.subheader("Memory")
        if memory not in [None,0]:
            fig_mem = px.bar(df_node_mean, x=df_node_mean.index, y="memory", color="node_name", barmode="group")
            st.plotly_chart(fig_mem, use_container_width=True)
        else:
            st.warning("No Memory data")
        if df_node_mean is not None:
            st.subheader("Node")
            selected_node = st.selectbox("Select node", df_node.groups.keys(), index=None)
            if selected_node is not None:
                fig_node_history_cpu = px.line(df_node.get_group(selected_node), x=df_node.get_group(selected_node).index, y="cpu", title=f"{selected_node} CPU usage history")
                st.plotly_chart(fig_node_history_cpu, use_container_width=True)
                fig_node_history_memory = px.line(df_node.get_group(selected_node), x=df_node.get_group(selected_node).index, y="memory", title=f"{selected_node} Memory usage history")
                st.plotly_chart(fig_node_history_memory, use_container_width=True)
            else:
                st.warning("No node selected")
        else:
            st.warning("No node data")
        
        # Photo logic
        st.header("Photos")
        image_data = photo()
        if image_data is None:st.error("Get photo fail")
        selected_node = st.selectbox("Select node", list(image_data.keys()), index=None, key="Photo-select-node")
        if selected_node is not None:
            image_data[selected_node].sort(key=lambda x:x["time"])
            earliest_time = datetime.date(image_data[selected_node][0]["time"])
            latest_time = datetime.date(image_data[selected_node][-1]["time"])
            recommended_date_end = datetime.date(earliest_time.year, earliest_time.month, earliest_time.day+1)
            selected_date_range = st.date_input("Select date range",(earliest_time, recommended_date_end), earliest_time, latest_time)
            filtered_image_data = []
            for i in image_data[selected_node]:
                if selected_date_range[0] <= datetime.date(i["time"]) <= selected_date_range[1]:
                    filtered_image_data.append(i)
            if len(filtered_image_data) == 0:st.warning("No photo")
            else:
                st.subheader("Select photo")
                st.info("Click the download button to download the photo")
                st.download_button(label="Download", data=pd.DataFrame(filtered_image_data).to_csv(index=False), file_name="photo.csv", mime="text/csv")
                st.download_button(label="Download all", data=dowload_all_photo(), file_name="all_photo.csv", mime="text/csv")
                image_list = [i["image"] for i in filtered_image_data]
                caption_list = [f"{i['plant_name']} {i['time']}" for i in filtered_image_data]
                if len(image_list) > 20:
                    st.warning("Too many photos, only show 20, please download them")
                    image_list = image_list[:20]
                    caption_list = caption_list[:20]
                st.image(image_list, caption=caption_list, width=200)
    else:
        login()

if "login" not in st.session_state:init()
st.set_page_config(layout="wide")
main()