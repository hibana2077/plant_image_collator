# 使用
FROM python:3.11-bullseye

# 設定工作目錄
WORKDIR /app

#add python3 and other tools
RUN apt-get update && apt-get install -y iputils-ping

# 複製requirements.txt並安裝依賴
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

# 複製應用程式碼
COPY ./app.py /app/app.py

# Streamlit會使用的端口
EXPOSE 8501

# 設定環境變數
ENV USER=streamlit
ENV PWD=streamlit

# 啟動Streamlit應用程式
CMD ["streamlit", "run", "app.py"]