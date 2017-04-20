## [n2n](http://www.ntop.org/n2n/)

![n2n](http://uploads.shuyz.com/2014/08/3448697635.png)

### install n2n

debian

```
-- n2n v1
sudo apt-get install n2n
sudo apt-get remove n2n

-- n2n v2
sudo apt-get install subversion build-essential libssl-dev
svn co https://svn.ntop.org/svn/ntop/trunk/n2n
cd n2n/n2n_v2
make
sudo make install 
```


macOS
* intall [tuntap](http://tuntaposx.sourceforge.net/download.xhtml)
* install n2n

```
git clone https://github.com/meyerd/n2n.git
cd n2n/n2n_v1
make
sudo make install
```

问题：
* tuntap 在 macOS Sierra 还有一些问题
* [编译问题](https://gist.github.com/tevino/9798566)
* n2n 的另一个分支：https://github.com/certik/n2n.git

tuntap_osx.c这个文件：
* 注释掉void tun_close(tuntap_dev *device);这行代码
* 将tun_close(device);这段代码更换为tuntap_close(device);


### default config
* /etc/default/n2n(by apt-get)

### supernode

```
supernode -h
supernode -l <listening port> [-v] [-h]

For n2n_v1 supernode: 
88.86.108.50:82
remoteqth.com:82

n2n_v2 supernode: 
88.86.108.50:86

```


### edge
```
edge -h

"-a <IP地址>" 选项（静态地）指定了分配给 TAP 接口的 VPN 的 IP 地址。如果你想要使用 DHCP，你需要在其中一台边缘节点上配置一台 DHCP 服务器，然后使用“-a dhcp:0.0.0.0”选项来代替


n2n v1
-- raspberry pi
sudo edge -d edge0 -a 10.0.0.10 -c n2n_v1_ljw -k hello -l 88.86.108.50:82
sudo edge -d edge0 -a 10.0.0.10 -c n2n_v1_ljw -k hello -l remoteqth.com:82



sudo edge -d edge0 -a 10.0.0.11 -c n2n_v1_ljw -k hello -l remoteqth.com:82



-- macOS
./edge -a 10.0.0.11 -c n2n_v1_ljw -k hello -l 88.86.108.50:82



n2n v2
sudo edge -d edge0 -a 10.0.0.10 -c n2n_v2_ljw -k hello -l 88.86.108.50:86

```

<!-- sudo ip route add 192.168.1.0/24 via 10.1.2.1 -->
<!-- sudo /etc/init.d/n2n start -->


### n2n_Gui
1. [Windows](https://sourceforge.net/projects/n2nedgegui/)
2. [Android](https://play.google.com/store/apps/details?id=org.zhoubug.n2n_gui)

一些问题
* Android 机器需要 root
* Windows 客户端乱码

<!-- ip rule list -->
<!-- ip route list table local -->
<!-- ip addr show -->
<!-- ip route show -->
<!-- sudo ip route flush dev eth0 -->

