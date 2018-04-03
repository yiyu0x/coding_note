
# 你所不知道的python(?


## print

print函數後面可以接key，常用的有sep跟end

預設的print函數

> `print('hello',sep=' ',end='\n')`

所以print函數在印出東西時會自動將每一個物件中間空格，並且換行

- - -

還有一個技巧是有時候print的東西很多的時候，coding時可以簡單排版

只要要一行都有用引號即可，印出時會是連續的字串

```python
 print("hello,"
       "python is pretty")
```

out:`hello,python is pretty`

## round

round函數有先天漏洞，四捨五入實際上是取接近偶數的整數

例如:

> round(4.5)

out: 4

> round(3.5)

out: 4

> round(0.5)

out: 0

## pythonic

### 讀取多個使用者輸入值

```python
#input three int , seperate by space
a,b,c = map(int,input().split())

#input three int , seperate by ','
a,b,c = map(int,input().split(','))

#input three string , seperate by space
a,b,c = input().split(',')

#input any number int , seperate by space
data = list(map(int,input().split(',')))
```
### 找出字串中出現最多的字元

```python
text = input()
print(max(string.printable,key=text.count))
```

[rederence python2.7 doc](https://docs.python.org/2/library/string.html)

### find prime number

```python
l = [x for x in range(2,int(input())) if all(x % i for i in range(2,x))]
```
