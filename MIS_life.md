紀錄一些管理主機以來學到的事情

## nginx

強大的access log圖像化分析套件，goaccess

> goaccess -f `<access.log>`


## ssh

找出誰在暴力測試ssh登入
> grep sshd.\*Failed /var/log/auth.log | less

找出誰ssh連線失敗(通常是ssh key錯誤)
> grep sshd.*Did /var/log/auth.log | less

## 刪除某個用戶全部process
> killall -u <username>
  
## 刪除某個用戶全部資料
> userdel -r guest
