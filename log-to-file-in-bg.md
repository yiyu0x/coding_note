讓django或是其他程式

能把log寫入檔案，並且不要導到stdout

舉例：導入到當前目錄下`nohup.log`
> nohup python manage.py runserver &

or
> nohup /path/my_program &> my_log.txt &

[參考](https://blog.gtwang.org/linux/linux-nohup-command-tutorial/)
