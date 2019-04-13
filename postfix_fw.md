###### tags: `private` 
# Postfix fw設定

一般 user 信件 fw 至 `/etc/postfix/main.cf` 

註解打開
```
virtual_alias_domains = yiyu0x.tk localhost
virtual_alias_maps = hash:/etc/postfix/virtual
```

然後到 `/etc/postfix/virtual` 設定:
```
yiyu@localhost yiyu@localhost yiyu0x@icloud.com
```
(欄位1為來源 後面欄位都是要FW的目標 給自己也fw是為了copy)

要確認 `/etc/postfix/virtual.db` 是否存在

如此一來給 yiyu 的信都會跑到 `yiyu0x@icloud.com`

---
## root mail forward

修改 `/etc/aliases`

```
# See man 5 aliases for format
postmaster:    root
root: yiyu0x@icloud.com, \root
```

最後面的 \root 為自己保留一份

記得執行 `sudo newaliases`

才會產生新的 `aliases.db`
