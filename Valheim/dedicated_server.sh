#!/bin/bash

# Update Ubuntu
apt update && sudo apt upgrade -y

# add multiverse repository
apt install software-properties-common -y
add-apt-repository multiverse

# Add 32-bit architecture for running Steam Command Application
dpkg --add-architecture i386

# Update again
apt update

# Install Steam Command
apt install steamcmd -y

# create a steam user
# Let user input a password
echo
echo '#################'
echo '# User settings #'
echo '#################'
echo
echo "Set password for steam user"
invalid_input=true
while [ $invalid_input ];
do
  read -sp 'Password: ' passvar1
  echo
  read -sp 'Retype Password: ' passvar2
  echo

  if [[ $passvar1 == $passvar2  ]]
  then
    invalid_input=$false
  else
    echo 'Passwords dont match, retype passwords!'
    echo
  fi

done

useradd --create-home --shell /bin/bash --password $passvar1 steam

# Create a symbolic link to Steam Command
cd /home/steam
ln -s /usr/games/steamcmd steamcmd

# Install Valheim Server (steam id: 896660) using Steam Command
steamcmd +login anonymous +force_install_dir /home/steam/valheimserver +app_update 896660 validate +exit

# Go into Valheim server folder
cd valheimserver

# Create start_server file with config
# Set server name

echo
echo '###################'
echo '# Server settings #'
echo '###################'
echo

read -p 'Server name: ' server_name
echo
read -p 'Server World: ' server_world

# Set a Server Password
invalid_input=true
while [ $invalid_input ];
do
  read -sp 'Server Password: ' server_passvar1
  echo
  read -sp 'Retype Password: ' server_passvar2
  echo

  if [[ $erver_passvar1 == $erver_passvar2  ]]
  then
    invalid_input=$false
  else
    echo 'Passwords dont match, retype passwords!'
    echo
  fi

done

echo "
#!/bin/bash
export templdpath=\$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=./linux64:\$LD_LIBRARY_PATH
export SteamAppId=892970

# Tip: Make a local copy of this script to avoid it being overwritten by steam.
# NOTE: Minimum password length is 5 characters & Password cant be in the server name.
# NOTE: You need to make sure the ports 2456-2458 is being forwarded to your server through your local router & firewall.
./valheim_server.x86_64 -name '$server_name' -port 2456 -nographics -batchmode -world '$server_world' -password '$server_passvar1'
-public 1

export LD_LIBRARY_PATH=\$templdpath
" >> start_valheim.sh

#!/bin/bash
export templdpath=$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=./linux64:$LD_LIBRARY_PATH
export SteamAppId=892970

# Tip: Make a local copy of this script to avoid it being overwritten by steam.
# NOTE: Minimum password length is 5 characters & Password cant be in the server name.
# NOTE: You need to make sure the ports 2456-2458 is being forwarded to your server through your local router & firewall.
./valheim_server.x86_64 -name "Geekhead" -port 2456 -nographics -batchmode -world "Geakheadv1" -password "sism1234" -public 1

export LD_LIBRARY_PATH=$templdpath

echo

chmod +x start_valheim.sh

# exit Valheim folder
cd ..

# Add a log file
echo 'journalctl --unit=valheimserver --reverse' >> check_log.sh
chmod +x check_log.sh

#Add as Service
echo "
#!/bin/bash
[Unit]
Description=Valheim Server
Wants=network-online.target
After=syslog.target network.target nss-lookup.target network-online.target

[Service]
Type=simple
Restart=on-failure
RestartSec=5
StartLimitInterval=60s
StartLimitBurst=3
User=steam
Group=steam
ExecStartPre=/home/steam/steamcmd +login anonymous +force_install_dir /home/steam/valheimserver +app_update 896660 validate +exit
ExecStart=/home/steam/valheimserver/start_valheim.sh
ExecReload=/bin/kill -s HUP \$MAINPID
ExecStop=/bin/kill -s INT \$MAINPID
WorkingDirectory=/home/steam/valheimserver
LimitNOFILE=100000

[Install]
WantedBy=multi-user.target
" >> /etc/systemd/system/valheimserver.service

sleep 1
systemctl daemon-reload
sleep 5
systemctl start valheimserver
sleep 15
systemctl enable valheimserver

ip a
systemctl status valheimserver
