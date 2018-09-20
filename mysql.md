```
（讀取資料庫 ... 目前共安裝了 190366 個檔案和目錄。）
準備解開 .../mysql-server-5.7_5.7.23-0ubuntu0.18.04.1_amd64.deb ...
Failed to stop mysql.service: Unit mysql.service not loaded.
invoke-rc.d: initscript mysql, action "stop" failed.
invoke-rc.d returned 5
There is a MySQL server running, but we failed in our attempts to stop it.
Stop it yourself and try again!
dpkg: error processing archive /var/cache/apt/archives/mysql-server-5.7_5.7.23-0ubuntu0.18.04.1_amd64.deb (--unpack):
 new mysql-server-5.7 package pre-installation script subprocess returned error exit status 1
選取了原先未選的套件 mysql-server。
準備解開 .../mysql-server_5.7.23-0ubuntu0.18.04.1_all.deb ...
解開 mysql-server (5.7.23-0ubuntu0.18.04.1) 中...
處理時發生錯誤：
 /var/cache/apt/archives/mysql-server-5.7_5.7.23-0ubuntu0.18.04.1_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

mysql相依性問題，造成apt無法繼續使用

解決：

先乾淨移除mysql
> sudo apt-get remove --purge mysql-server mysql-client mysql-common

> sudo apt-get autoremove

> sudo apt-get autoclean

> sudo rm -rf /var/lib/mysql

> sudo rm -rf /etc/mysql

在重新安裝即可
> sudo apt-get install mysql-server  

[ref](http://glj8989332.blogspot.com/2015/10/mysql-ubuntumysql.html)

查看相關套件
> dpkg -l | grep mysql
