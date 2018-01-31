
### 避免此用法 有round-off error問題 (可能造成無窮迴圈)

```c
for (double x=0; x!=10; x+=0.1){
    ..........
}
```
