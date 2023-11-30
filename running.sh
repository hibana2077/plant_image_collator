sudo docker-compose -f docker-compose.yml up -d --build

# run python in background
# ./main/app.py
python3 main/app.py > main.log &