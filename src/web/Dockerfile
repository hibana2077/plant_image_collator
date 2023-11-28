# 使用ubuntu 22.04作為基礎映像檔
FROM ubuntu:22.04

# 設定工作目錄
WORKDIR /app

#add python3 and other tools
RUN apt-get update && apt-get install -y python3 python3-pip iputils-ping gcc g++ git

# 更新pip
RUN pip3 install --upgrade pip

# 複製requirements.txt並安裝依賴
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# 複製應用程式碼
COPY ./app.py /app/app.py

# 複製其他檔案
COPY ./pages /app/pages

# Streamlit會使用的端口
EXPOSE 3000

# 啟動Streamlit應用程式
CMD ["streamlit", "run", "app.py", "--server.port", "3000"]