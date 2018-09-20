# ubuntu-tips

## install new version nodejs on ubuntu

```
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -
sudo apt-get install -y nodejs
```

## position of the windows buttons

### introduction

In ubuntu 18.04 LTS the position of buttins are on right , but I was used to those buttom on left side(my other OS is macOS) .

so , if you want to change it to left or right , you can use the command

change to the left:

`gsettings set org.gnome.desktop.wm.preferences button-layout close,minimize,maximize:`

change to the right:

`gsettings set org.gnome.desktop.wm.preferences button-layout :minimize,maximize,close`

### view

![](https://i.imgur.com/GQuf8DJ.gif)

## install sublime_text_3 with terminal

### add sb3 to repository

`wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -`

`sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"`

### install

`sudo apt install sublime-text`

### using

`subl`

### view

![subl_view](https://i.imgur.com/cyxRXjK.gif)

### set default editor as sublime_text_3

running on 13.04+, update the file: /etc/gnome/defaults.list.

`sudo sed -i 's/gedit.desktop/sublime_text.desktop/g' /etc/gnome/defaults.list`

## rename the dicectory in Home to English

### method 1 (recommend)

check $LANG now :

`echo $LANG`

change to English :

`export LANG=en_US`

update :

`xdg-user-dirs-gtk-update`

**you need to reboot or restart X-windows**

#### view

![view_LANG](https://i.imgur.com/mcOIcn6.gif)

when you reboot the system , you will see:

![reboot_LANG](https://i.imgur.com/XxEq0GL.png)

it's mean succuessed

### method 2

or you can set the configuration file `~/.config/user-dirs.dirs`

**you need to reboot or restart X-windows**


