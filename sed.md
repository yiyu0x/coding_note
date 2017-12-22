# sed雷 💣

sed 內容如果是變數 

> sed -e 's/${var}/${var2}'

要改為

> sed -e "s/${var}/${var2}"
