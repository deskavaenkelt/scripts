#!/bin/bash

curl https://raw.githubusercontent.com/deskavaenkelt/scripts/main/ubuntu_server_post_install.sh | bash

sudo apt install git -y
sudo apt install python -y
sudo apt install nginx -y