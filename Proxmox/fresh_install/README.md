# Fresh Install

## Table of Contents

- [Updates](#updates)
- [IOMMU (PCI Passthrough)](#iommu-pci-passthrough)
- [Shares](#shares)
- [Backups](#backups)
- [Upload ISOs](#upload-isos)
- [Create templates](#create-templates)
- [Cluster](#cluster)

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

## Shares

Add SMB/CIFS shares:

ID: Share name
Server name: IP address for NAS
Username: For NAS user
Password: For NAS user
Share: ISO's directory

## Backups

Datacenter backup:

- Add
- Node
- Storage
- Schedule
- Selection mode

## Upload ISOs

- [Windows VirtIO Drivers](https://pve.proxmox.com/wiki/Windows_VirtIO_Drivers)

## Create templates

- Shut down machine
- Convert to template
- Right click on template and select "Clone"
- Mode
    - Linked Clone (builds a new VM from on top of template / really fast)
    - Full Clone (builds a whole new VM from template / slower but standalone)
- Reset machine (Linux)
    - Change hostname: `sudo nano /etc/hostname` find your hostname and change it to the name you want
    - change hosts file: `sudo nano /etc/hosts` find your hostname and change it to the name you want
    - Reset machine id: `rm -f /etc/machine-id /var/lib/dbus/machine-id && dbus-uuidgen --ensure=/etc/machine-id &&
      dbus-uuidgen --ensure`
    - Regenerate ssh keys: `regen ssh keys && sudo rm /etc/ssh/ssh_host_* && sudo dpkg-reconfigure openssh-server`
    - Reboot machine
- Reset machine (Windows)
  -
  Sysprep [Windows](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation?view=windows-11)
    - Run: `Sysprep /generalize /shutdown` in command prompt
    - Reboot machine

## Cluster

Make sure to have:

- 2 NICs (1 for management and 1 for public)
- No VMs (all VMs should be deleted if any exist)

Click on Datacenter -> Clusters -> Create Cluster

- Name of cluster
- Chose the correct interface for the cluster
- Create

Click on Join Cluster and select the join information for the cluster you created.

On the Proxmox machine you want to add to cluster chose:

Click on Datacenter -> Clusters -> Join Cluster

- Paste join information from the cluster you created
- Join
