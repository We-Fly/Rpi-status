#! /bin/bash

sudo apt-get install python3 python3-pip -y
pip3 install vcgencmd

git clone https://github.com/We-Fly/Rpi-status.git

sudo cp Rpi-status/rpistatus.py /usr/bin/status

sudo chmod 755 /usr/bin/status

rm -rf Rpi-status
