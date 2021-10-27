if [ $(id -u) -ne 0 ]; then
	echo "This script must be ran as root! / Bu arac root olarak calistirilmalidir!"
	exit 1
fi
apt install python3 -y
pip3 install clint
python3 banner/installation_banner.py
apt-get update
apt install python3 -y
apt install python3-pip -y
apt-get install xterm
pip3 install colored
