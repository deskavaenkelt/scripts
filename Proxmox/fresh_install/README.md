# Fresh Install

## Table of Contents

- [Updates](#updates)
- [IOMMU (PCI Passthrough)](#iommu-pci-passthrough)
- [Add shares](#add-shares)
- [Add backups](#add-backups)


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

## IOMMU (PCI Passthrough)

[Proxmox PCI Passthrough](https://pve.proxmox.com/wiki/Pci_passthrough)

### For GRUB:

Edit:

```shell
nano /etc/default/grub
```

```shell
# comment out the line containing 'GRUB_CMDLINE_LINUX_DEFAULT="quiet"'
GRUB_CMDLINE_LINUX_DEFAULT="quiet"

# Add the following line to the file for INTEL:
GRUB_CMDLINE_LINUX_DEFAULT="quiet intel_iommu=on"
# or for AMD:
GRUB_CMDLINE_LINUX_DEFAULT="quiet amd_iommu=on"
```

Then save the changes and update grub:

```shell
update-grub
proxmox-boot-tool refresh
```

Edit: 

```shell
nano /etc/modules
```

```shell
update-initramfs -u -k all
reboot
```

## Add shares

Add SMB/CIFS shares:

ID: Share name
Server name: IP address for NAS
Username: For NAS user
Password: For NAS user
Share: ISO's directory

## Add backups

Datacenter backup: 

- Add
- Node
- Storage
- Schedule
- Selection mode
