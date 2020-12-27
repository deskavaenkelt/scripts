#!/bin/bash

echo Lars Ubuntu update script

# Update all
sudo apt-get update && sudo apt-get upgrade -y
sudo apt autoremove -y
sudo apt-get autoclean -y
