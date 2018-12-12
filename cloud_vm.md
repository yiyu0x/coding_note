### on vm
1. add user

`adduser yiyu`

if you want to remove

`userdel -r yiyu`

2. give sudo identity

`usermod -aG sudo yiyu`

3. give login shell

`chsh -s /bin/bash yiyu`

4. color shell

~/.bashrc:
```
PS1='\[\033[1;36m\]\u\[\033[1;31m\]@\[\033[1;32m\]\h:\[\033[1;35m\]\w\[\033[1;31m\]\$\[\033[0m\] '
```



### on host
generate ssh public key

`ssh-keygen -f ~/.ssh/y-gcp -C "yiyu"`
