紀錄一些管理主機以來學到的事情

## nginx

強大的access log圖像化分析套件，goaccess

> goaccess -f `<access.log>`


## ssh

找出誰在暴力測試ssh登入
> grep sshd.\*Failed /var/log/auth.log | less

找出誰ssh連線失敗(通常是ssh key錯誤)
> grep sshd.*Did /var/log/auth.log | less

### fail2ban

安裝完之後，先看目前規則是否多出fail2ban
> iptables --list

如果有封鎖來源會多出規則
```
Chain f2b-sshd (1 references)
target     prot opt source               destination
REJECT     all  --  sw67-167-176.adsl.dynamic.seed.net.tw  anywhere             reject-with icmp-port-unreachable
RETURN     all  --  anywhere             anywhere
```

若要將封鎖規則刪除
> sudo iptables -D f2b-sshd 1

## mysql/mariadb

設定root密碼

> sudo mysql -uroot

> GRANT ALL PRIVILEGES on *.* to 'root'@'localhost' IDENTIFIED BY '<password>';
  
> FLUSH PRIVILEGES;



## 帳戶管理

### 刪除某個用戶全部process
> killall -u <username>
  
### 刪除某個用戶全部資料
> userdel -r guest

