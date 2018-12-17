ubuntu server更改hostname

把 `/etc/hostname` 跟 `/etc/hosts` 改為新的主機名稱

接著

`sudo hostnamectl set-hostname <new-name>`

接著重開機 

如果還是無效

(server版要加上這行)
將 `/etc/cloud/cloud.cfg` 的 `preserve_hostname` 設定 改為 `true`

再重開機

[參考](https://ubuntuforums.org/showthread.php?t=2389098&page=2)
