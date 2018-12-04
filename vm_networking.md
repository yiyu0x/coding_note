virtualbox 拿不到第二張網卡(ifconfig 看不到第二張網卡(bridge))

先用ip a看一下第二張網卡名稱 (我看到的是enp0s8)

然後到`/etc/network/interfaces`裡面新增
```
auto enp0s8
iface enp0s8 inet dhcp
```

並且下載ifupdown

`apt install ifupdown`

接著啟動介面即可

`ifupdown enp0s8`
