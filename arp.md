nmap掃出windows host(預設參數掃不出 有防火牆)
> nmap -sW 192.168.0.0/24

arp spoofing 
> sudo apt install dsniff

安裝完之後
> arpspoof -i eth0 192.168.0.1 192.168.0.5

(arpspoof -i <網卡> <router-ip> <target-ip>)
