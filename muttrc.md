postfix 把 mailbox 設定為 maildir 後

```mailbox
home_mailbox = Mailbox
```

```maildir
home_mailbox = Maildir/
```

還要把 MTA (這篇用的是 mutt) 設定為用 maildir 格式閱讀信件

因為 postfix 預設 maildir 目錄是在 `~/Maildir` 

所以我們就把 mutt 設定為從這邊讀取信件即可

~/.muttrc
```
set mbox_type=Maildir
set spoolfile="~/Maildir/"
set folder="~/Maildir/"
```

缺少 `set spoolfile="~/Maildir/"` 的話 mutt 依然會從 /var/mail/<user> (mailbox)去讀取信件，不知道原因＠＠
