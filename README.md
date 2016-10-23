## Notes of Raspberry Pi

### 系统启动盘

系统下载： 这里选择 RASPBIAN JESSIE

https://www.raspberrypi.org/downloads/raspbian/

Noobs：系统安装助手

https://www.raspberrypi.org/downloads/noobs/

### sources.list
/etc/apt/sources.list

### ssh
默认用户名：pi
原始密码：raspberry


### install something useful
* git: sudo apt-get install git-ycore
* vim: sudo apt-get install vim
* pip: sudo apt-get install python-pip


### mount

1. 插上自动识别挂载在某一目录下，拔下自动umount

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

3. 查看挂载信息
```
sudo mount -l
sudo df -h
```

### samba

[samba](https://help.ubuntu.com/community/How%20to%20Create%20a%20Network%20Share%20Via%20Samba%20Via%20CLI%20(Command-line%20interface/Linux%20Terminal)%20-%20Uncomplicated,%20Simple%20and%20Brief%20Way!)
sudo apt-get update
sudo apt-get install samba
sudo smbpasswd -a <user_name>: e.g. pi
mkdir /home/pi/xunlei
sudo cp /etc/samba/smb.conf ~
sudo vim /etc/samba/smb.conf
sudo /etc/init.d/samba restart

```
#append to smb.conf
[media]
path=/media
validusers=pi
browseable=yes
public=yes
writable=yes
```

Remember that your user must have permission to write and edit the folder you want to share.
```
sudo chown <user_name> /var/opt/blah/blahblah
sudo chown :<user_name> /var/opt/blah/blahblah
```




### 1. aria2
* 目录：/etc/aria2
* 配置：/etc/aria2/aria2.conf
* 服务：/etc/init.d/aria2c


### 2. xunlei
利用树莓派搭建迅雷远程下载服务器
http://www.jianshu.com/p/17cee17159f4

vim ~/xunlei/etc/thunder_mounts.cfg
```
valiable_mount_path_pattern
{
/media/pi/HD/TDDOWNLOAD
}
```
http://192.168.0.106:9001:9001/getusedpartitioninfo
http://192.168.0.106:9001/getsysinfo

THE ACTIVE CODE IS: ffvksv
go to http://yuancheng.xunlei.com, bind your device with the active code.
finished.


### 3. transmission


### 保护硬盘
由于树莓派 24 小时不断电，大部分时间硬盘是空闲的，为了省电，同时保护硬盘，可以设置空闲的时候自动停转（spin down），进入 standby 状态。编辑 hdparm 的配置文件/etc/hdparm.conf：

```
quiet 
apm = 127
spindown_time = 60

```

apm 设置高级电源管理功能，越小表示越激进，0-127 允许 spin down。spindown_time 设置停转的超时时间，1-240 的单位是 5s，因此设为 60 表示 5 分钟没有读写硬盘将停转。
这里顺便说一下，西数硬盘声名狼藉的 C1 问题（LCC 增长很快）就跟高级电源管理特性有关，解决办法一般是用 wdidle3 将固件里的超时时间改大。



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

### vnc
1. install: sudo apt-get update && sudo apt-get install tightvncserver
2. set password: vncpasswd (hello1234)
3. new a vnc desktop: tightvncserver
4. stop a desktop: vncserver -kill:1
5. Mac vnc viewer: [realvnc](https://www.realvnc.com/download/viewer/) for Mac
6. connect ip:num

开机自启：
* sudo vi /etc/init.d/tightvncserver
* sudo chmod 755 /etc/init.d/tightvncserver
* sudo update-rc.d tightvncserver defaults

```
#!/bin/sh
### BEGIN INIT INFO
# Provides:          tightvncserver
# Required-Start:    $local_fs
# Required-Stop:     $local_fs
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stop tightvncserver
### END INIT INFO
 
# More details see:
# http://www.penguintutor.com/linux/tightvnc
 
### Customize this entry
# Set the USER variable to the name of the user to start tightvncserver under
export USER='pi'
### End customization required
 
eval cd ~$USER
 
case "$1" in
  start)
    # 启动命令行。此处自定义分辨率、控制台号码或其它参数。
    su $USER -c '/usr/bin/tightvncserver -depth 16 -geometry 800x600 :1'
    echo "Starting TightVNC server for $USER "
    ;;
  stop)
    # 终止命令行。此处控制台号码与启动一致。
    su $USER -c '/usr/bin/tightvncserver -kill :1'
    echo "Tightvncserver stopped"
    ;;
  *)
    echo "Usage: /etc/init.d/tightvncserver {start|stop}"
    exit 1
    ;;
esac
exit 0
```

ls Xvnc
* ps ax | grep Xtightvnc | grep -v grep


### 一些常用目录
* /etc/init.d
* 密码管理：/etc/passwd


### 开机自启
sudo update-rc.d xunlei defaults
sudo update-rc.d aria2 defaults

or edit: /etc/rc.local
nohup sudo -u pi /home/pi/xunlei/portal >/dev/null 2>&1 &




### 常用命令
* sudo fdisk -l
* sudo blkid: 成功识别到硬盘后，可以查询文件系统类型、LABEL、UUID等信息
* sudo reboot
* sudo raspi-config
* uname -a: 系统内核信息查询
* sudo crontab -l
* ls -lR /dev/disk



### 文件管理——百度网盘直链系统V2.0
http://bdbea3.duapp.com/baidu_pcs/file_manage.php


### 树莓派设置支持中文
http://www.jianshu.com/p/00fc5725d3fc
