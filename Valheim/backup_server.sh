#!/bin/bash

#sudo apt update && sudo apt upgrade -y

# Install the CIFS Utils pkg
#apt-get install cifs-utils

# Create a mount point
#sudo mkdir /mnt/backups

# Mount the volume
#sudo mount -t cifs -o user=lars//192.168.1.9/Backups/Valheim/devops1 /mnt/backups


ssh steam@192.168.2.20

scp steam@192.168.2.20:"/home/steam/.config/unity3d/IronGate/Valheim/worlds/devops.db.old" /backups/
scp steam@192.168.2.20:"/home/steam/.config/unity3d/IronGate/Valheim/worlds/devops.fwl.old" /backups/



