#! /bin/bash

sudo apt-get update

sudo apt-get install libraspberrypi-bin -y

sudo apt-get install python3 python3-pip -y

pip3 install vcgencmd

git clone https://github.com/We-Fly/Rpi-status.git

sudo cp Rpi-status/rpistatus.py /usr/bin/status

sudo cp rpistatus.py /usr/bin/status

sudo chmod 755 /usr/bin/status

sudo rm -rf Rpi-status

cd .. && sudo rm -rf Rpi-status
