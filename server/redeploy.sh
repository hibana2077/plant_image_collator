
docker stop $(sudo docker ps -a -q)
docker rm $(sudo docker ps -a -q)
docker-compose up -d --build