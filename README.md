## Handbook of Raspberry Pi

### 系统启动盘

系统下载： 这里选择 RASPBIAN JESSIE

https://www.raspberrypi.org/downloads/raspbian/

Noobs：系统安装助手

https://www.raspberrypi.org/downloads/noobs/

### sources.list
/etc/apt/sources.list

### ssh
* 默认用户名：pi
* 原始密码：raspberry

### install
* git: sudo apt-get install git-ycore
* vim: sudo apt-get install vim
* pip: sudo apt-get install python-pip

### 时区

1. sudo apt-get install ntpdate 
2. tzselect: Asia China Beijing
3. sudo ntpdate cn.pool.ntp.org
4. date

> cn.pool.ntp.org 是国内的ntp服务器

### mount

exFAT & ntfs

```
sudo apt-get update
sudo apt-get install ntfs-3g
sudo apt-get install exfat-fuse exfat-utils
```



1.0 插上自动识别挂载在某一目录下，拔下自动umount

```
sudo vim /etc/udev/rules.d/10-usbstorage.rules
sudo /etc/init.d/udev restart
udevadm control --reload-rules
```

2.1 默认挂载NTFS格式的硬盘只有只读权限，需要借助其它工具实现

```
#安装所需软件包
sudo apt-get install fuse-utils ntfs-3g
#加载内核模块
modprobe fuse
#编辑fstab让移动硬盘开机自动挂载
sudo vim /etc/fstab
#在最后一行添加如下内容
/dev/sda1 /media/usb ntfs-3g defaults,noexec,umask=0000,utf8=1 0 0
#保存重启，即可生效
```

2.2 挂载FAT32格式的硬盘（U盘通常是这种格式）

```
#创建挂载点
sudo mkdir /mnt/myusbdrive
#编辑fstab让移动硬盘开机自动挂载
sudo vim /etc/fstab
#在最后一行添加如下内容
/dev/sda1 /mnt/myusbdrive auto defaults,noexec,umask=0000 0 0
#保存重启，即可生效
```

3.0 查看挂载信息
```
sudo mount -l
sudo df -h
```

### [samba](https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!)

* sudo apt-get update
* sudo apt-get install samba
* sudo smbpasswd -a <user_name>: e.g. pi
* mkdir /home/pi/xunlei
* sudo cp /etc/samba/smb.conf ~
* sudo vim /etc/samba/smb.conf
* sudo /etc/init.d/samba restart

Remember that your user must have permission to write and edit the folder you want to share.

```
sudo chown <user_name> /var/opt/blah/blahblah
sudo chown :<user_name> /var/opt/blah/blahblah
```


```
# add to smb.conf
[media]
path=/media
validusers=pi
browseable=yes
public=yes
writable=yes
```




### aria2
* 目录：/etc/aria2
* 配置：/etc/aria2/aria2.conf
* 服务：/etc/init.d/aria2c


### xunlei

[利用树莓派搭建迅雷远程下载服务器](http://www.jianshu.com/p/17cee17159f4)

vim ~/xunlei/etc/thunder_mounts.cfg

```
valiable_mount_path_pattern
{
/media/pi/HD/TDDOWNLOAD
}
```

link
* http://192.168.0.108:9001/getusedpartitioninfo
* http://192.168.0.108:9001/getsysinfo
* http://yuancheng.xunlei.com


> 通过 192.168.0.108:9001/getsysinfo 获取激活码，是一个数字串

### transmission


### 保护硬盘
由于树莓派 24 小时不断电，大部分时间硬盘是空闲的，为了省电，同时保护硬盘，可以设置空闲的时候自动停转（spin down），进入 standby 状态。

sudo vim /etc/hdparm.conf

```
quiet 
apm = 127
spindown_time = 60
```

apm 设置高级电源管理功能，越小表示越激进，0-127 允许 spin down。spindown_time 设置停转的超时时间，1-240 的单位是 5s，因此设为 60 表示 5 分钟没有读写硬盘将停转。



### sslocal

最简单的方法是安装python版本的：

1. install pip: apt-get install python-gevent python-m2crypto
2. install shadowsocks: pip install shadowsocks
3. 配置文件：e.g. ~/shadowsocks.json | /etc/shadowsocks.json
4. start & stop

```
python sslocal -c ~/shadowsocks.json
or
sslocal -c ~/shadowsocks.json -d start
sslocal -c ~/shadowsocks.json -d stop
```


### 一些常用目录

* /etc/init.d
* 密码管理：/etc/passwd


### 开机自启

```
sudo update-rc.d xunlei defaults
sudo update-rc.d aria2 defaults

or edit: /etc/rc.local
nohup sudo -u pi /home/pi/xunlei/portal >/dev/null 2>&1 &
```

### 常用命令

* sudo fdisk -l
* sudo blkid: 成功识别到硬盘后，可以查询文件系统类型、LABEL、UUID等信息
* sudo reboot
* sudo raspi-config
* uname -a: 系统内核信息查询
* sudo crontab -l
* ls -lR /dev/disk


### 文件管理——百度网盘直链系统V2.0
* [deprecated] http://bdbea3.duapp.com/baidu_pcs/file_manage.php
* http://pan.plyz.net/Man.aspx

### 树莓派设置支持中文
http://www.jianshu.com/p/00fc5725d3fc
