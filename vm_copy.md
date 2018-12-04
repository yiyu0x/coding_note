
複製一份vm在同一台電腦會發現UUID重複

此時需要重置UUID (重置複製出來新的那一份)

`VBoxManage internalcommands sethduuid "/home/user/VirtualBox VMs/drupal/drupal.vhd"`

重置完畢後即可將vm匯入virtualbox
