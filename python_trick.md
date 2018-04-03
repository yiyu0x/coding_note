
# 你所不知道的python(?

## round

round函數有先天漏洞，四捨五入實際上是取接近偶數的整數

例如:

> round(4.5)

結果是 4

> round(3.5)

結果是 4

> round(0.5)

結果是0

## pythonic

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
