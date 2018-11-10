修改設定檔
> vim /etc/postfix/main.cf

在最下方加入
```
virtual_alias_domains = <server-domain name)>
virtual_alias_maps = hash:/etc/postfix/virtual
```

> vim /etc/postfix/virtual

加入
```
yiyu@server.name yiyu@server.name.want.to.forward
```
> postmap /etc/postfix/virtual
> service postfix reload

[ref](https://www.cyberciti.biz/faq/linux-unix-bsd-postfix-forward-email-to-another-account/)
