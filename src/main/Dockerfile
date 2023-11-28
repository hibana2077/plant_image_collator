# 使用 Python 3.11 的 Alpine Linux 版本作為基本映像
FROM python:3.11-alpine

# 設置工作目錄
WORKDIR /app

# 安裝 vim 與 bash
RUN apk add --no-cache vim bash

# 複製 requirements.txt 文件到工作目錄
COPY requirements.txt .

# 安裝 Python 依賴
RUN pip install --no-cache-dir -r requirements.txt

# 複製所有其他文件到工作目錄
COPY . .

# 執行應用程式
CMD ["python3", "app.py"]