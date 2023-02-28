# Ubuntu - Expand Partition on Hyper-V Virtual Machine

## Table of Contents

## Introduction

We need to expand a disk that have become to small on a Hyper-V virtual machine. The disk is a virtual disk that is
attached to the virtual machine. The virtual machine is running Ubuntu LTS. The disk is a VHDX file that is attached to
the virtual machine. The disk is a dynamic disk.

## Preparations

### Hyper-V

1. Open Hyper-V Manager
2. Make sure the virtual machine have no snapshots (otherwise you need to delete them)
3. Shut down the virtual machine if necessary and make sure there are none.

### Ubuntu

```shell
sudo apt update && sudo apt upgrade -y
df -h
sudo pvdisplay
sudo fdisk -l
sudo parted -l
sudo parted /dev/sda
sudo parted /dev/sda print
sudo parted /dev/sda print free
```

## Hyper-V Steps

Now we should be able to expand the disk in Hyper-V while the VM is running.

1. Right click on the virtual machine and select "Settings"
2. Select the "Hard Drive" under "SCSI Controller"
3. Follow the guide to expand the disk
4. Start the virtual machine if off else reboot the virtual machine

## Steps

1. Open a terminal window or SSH to the virtual machine
2. Run the following command to list the disks

    ```bash
    sudo fdisk -l
    ```

   The output should look like this

   ```text
   GPT PMBR size mismatch (<number> != <bigger_number>) will be corrected by w(rite).
   ```

3. Run the following command to fix this error:

    ```bash
    sudo parted -l
    > fix
    ```

4. Verify that the disk is fixed

    ```bash
    sudo fdisk -l
    ```

5. Resize the partition

    ```bash
    sudo parted /dev/sda
    > print
    > resizepart 3 # (or whatever number the partition is)
    > <number> # (the new size, my new size was 68.7GB so I entered 68.5GB = -200MB for safety)
    > print # (to verify the new size)
    > quit
    ```

   You may be warned that the disk is in use, this is generally okay, so enter yes.

6. To discover the filesystem used by each partition on your system, use the following command:

    ```bash
   lsblk -f
   
   # or
   lsblk
    ```

   Output:

   ```text
   NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
   sda                         8:0    0   64G  0 disk
   ├─sda1                      8:1    0  1.1G  0 part /boot/efi
   ├─sda2                      8:2    0  1.5G  0 part /boot
   └─sda3                      8:3    0 61.3G  0 part
     └─ubuntu--vg-ubuntu--lv 253:0    0 14.7G  0 lvm  /
   sr0                        11:0    1 1024M  0 rom
   ```

7. Extend the physical volume:

    ```bash
    sudo pvresize /dev/sda3
    ```

   Output:

    ```text
    Physical volume "/dev/sda3" changed
    1 physical volume(s) resized / 0 physical volume(s) not resized
    ```

8. The result can be checked using pvs:

    ```bash
    sudo pvs
    ```

   Output:

    ```text
    PV         VG        Fmt  Attr PSize  PFree
    /dev/sda3  ubuntu-vg lvm2 a--  61.24g <46.52g
    ```

9. Then resize the logical volume.
   Use -r to automatically resize the contained filesystem.
   After the prefix /dev/mapper/, specify the logical volume name shown by `lsblk` below sda3:

    ```bash
    sudo lvresize -r -l+100%FREE /dev/mapper/ubuntu--vg-ubuntu--lv
    ```

   Output:

    ```text
      Size of logical volume ubuntu-vg/ubuntu-lv changed from 14.72 GiB (3769 extents) to 61.24 GiB (15678 extents).
      Logical volume ubuntu-vg/ubuntu-lv successfully resized.
    ```

10. The result

    ```bash
    lsblk
    ```

    ```text
      NAME                      MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
      sda                         8:0    0   64G  0 disk
      ├─sda1                      8:1    0  1.1G  0 part /boot/efi
      ├─sda2                      8:2    0  1.5G  0 part /boot
      └─sda3                      8:3    0 61.3G  0 part
        └─ubuntu--vg-ubuntu--lv 253:0    0 61.2G  0 lvm  /
      sr0                        11:0    1 1024M  0 rom
    ```
   
    ```bash
    df -h
    ```
   
    ```text
      Filesystem                         Size  Used Avail Use% Mounted on
      udev                               1.9G     0  1.9G   0% /dev
      tmpfs                              395M  556K  394M   1% /run
      /dev/mapper/ubuntu--vg-ubuntu--lv   61G  5.0G   53G   9% /
      tmpfs                              2.0G     0  2.0G   0% /dev/shm
      tmpfs                              5.0M     0  5.0M   0% /run/lock
      tmpfs                              2.0G     0  2.0G   0% /sys/fs/cgroup
      /dev/sda2                          1.5G   79M  1.3G   6% /boot
      /dev/sda1                          1.1G  5.3M  1.1G   1% /boot/efi
      tmpfs                              395M     0  395M   0% /run/user/1000
    ```
   
    ```bash
    sudo pvs
    ```

    ```text
     PV         VG        Fmt  Attr PSize  PFree
     /dev/sda3  ubuntu-vg lvm2 a--  61.24g    0
    ```

## Conclusion

The disk is expanded and the file system is expanded.

## References

* [HOW TO FIX ERROR: GPT PMBR SIZE MISMATCH](https://arstech.net/gpt-pmbr-size-mismatch/)
* [Resizing a Partition + Filesystem on Linux from the CLI](https://www.privex.io/articles/how-to-resize-partition/)
* [How can I add the new space to a volume group after resizing partition?](https://askubuntu.com/questions/1078918/how-can-i-add-the-new-space-to-a-volume-group-after-resizing-partition)
