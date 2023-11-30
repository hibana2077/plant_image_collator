sudo apt-get update && sudo apt-get upgrade -y
sudo apt-get install -y python3-pip wget curl
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo pip3 install -r ./main/requirements.txt