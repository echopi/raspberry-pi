
## bittorrent server


### install

```
sudo apt-get update
sudo apt-get upgrade

sudo apt-get install deluged deluge-console deluge-web
```


### start
```
deluged

<!-- 网页操作 -->
deluged-web

deluge-web --fork
deluge-web --ssl


<!-- 控制台查看进度 -->
deluge-console
```


* 默认端口：8112
* 默认密码：deluged
