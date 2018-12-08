`sudo vim /etc/systemd/system/network-online.target.wants/networking.service`

TimeoutStartSec=5min  

改成

TimeoutStartSec=10sec

然後reboot即可
