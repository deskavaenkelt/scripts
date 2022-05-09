# Fresh Install

## Table of Contents

- [Updates](#updates)

## Updates

Edit files

```shell
nano /etc/apt/sources.list
```

```shell
deb http://ftp.se.debian.org/debian bullseye main contrib

deb http://ftp.se.debian.org/debian bullseye-updates main contrib

# security updates
deb http://security.debian.org bullseye-security main contrib

# PVE pve-no-subscription repository provided by proxmox.com,
# NOT recommended for production use
deb http://download.proxmox.com/debian/pve bullseye pve-no-subscription
```

```shell
nano /etc/apt/sources.list.d/pve-enterprise.list
```

```shell
#deb https://enterprise.proxmox.com/debian/pve bullseye pve-enterprise
```

Run

```shell
apt-get update && apt dist-upgrade -y && reboot
```


