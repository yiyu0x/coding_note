紀錄一些管理主機以來學到的事情

# nginx

強大的access log圖像化分析套件，goaccess

> goaccess -f `<access.log>`


# ssh

找出誰在暴力測試ssh登入
> grep sshd.\*Failed /var/log/auth.log | less

找出誰ssh連線失敗(通常是ssh key錯誤)
> grep sshd.*Did /var/log/auth.log | less

## fail2ban

安裝完之後，先看目前規則是否多出fail2ban
> iptables -L

如果有封鎖來源會多出規則
```
Chain f2b-sshd (1 references)
target     prot opt source               destination
REJECT     all  --  sw67-167-176.adsl.dynamic.seed.net.tw  anywhere             reject-with icmp-port-unreachable
RETURN     all  --  anywhere             anywhere
```

若要將封鎖規則刪除
> sudo iptables -D f2b-sshd 1

# ufw


開啟關閉
> sudo ufw enable
> sudo ufw disable

決定使用白名單或黑名單

全部打開,要設防火牆設關閉的規則
> sudo ufw default allow

全部關閉,要設防火牆設開啟的規則(個人用這個)
> sudo ufw default deny

允許某個服務(相反用 deny)
> sudo ufw allow ssh

ssh對應的port從`/etc/services`這個檔案對應

允許某的port(相反用 deny)
> sudo ufw allow in 22

刪除規則

` sudo ufw delete <number>`

查看規則number
> sudo ufw status numbered

開啟log
> sudo ufw logging on
存在`/var/log/ufw.log`

查看狀態
> sudo ufw status

# mysql/mariadb

## 設定root密碼

> sudo mysql -uroot

`GRANT ALL PRIVILEGES on *.* to 'root'@'localhost' IDENTIFIED BY '<password>'`
  
> FLUSH PRIVILEGES;

## 建立使用者

`CREATE USER 'my_user'@'localhost' IDENTIFIED BY 'my_password';`

[mysql常用手段](https://blog.gtwang.org/linux/mysql-create-database-add-user-table-tutorial/)

## 檢視db中所有user

> select User, Host from mysql.user; 



# 帳戶管理

## 刪除某個用戶全部process
> killall -u <username>
  
## 刪除某個用戶全部資料
> userdel -r guest

