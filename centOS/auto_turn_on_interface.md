將網卡設定為每次開機都自動開啟

`sudo vi /etc/sysconfig/network-scripts/ifcfg-enp0s3`

將 ONBOOT 設為 yes
```
ONBOOT=yes
```