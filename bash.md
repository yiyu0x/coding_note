# bash雷 💣


## sed

sed 內容如果是變數 

> sed -e 's/${var}/${var2}'

要改為

> sed -e "s/${var}/${var2}"

## bash字串比對

如果字串內容有空白 比對時外面要加雙引號
```bash

$var = 'test test'
$var2 = 'ha ha'

if [ "$var" != "$var2" ];then
  echo "great"
fi
```
