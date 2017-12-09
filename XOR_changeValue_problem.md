
# Problem

XOR 交換兩個數值時發生異常
+ 預期輸出
-- 2 2
+ 實際輸出
-- 0 0

# Source Code

![code](https://i.imgur.com/91XB42r.png)

# Why

假設 

a  address 0x0001 | value 2

b  address 0x0001 | value 2

> a = a^b

a = 2^2 (so a=0)

- 此刻因為a,b的address都是 0x0001 所以b目前也是0

> b = a^b

b = 0^0 (so b=0)

> a = a^b

a = 0^0 (so a=0)

# Proof

![proofc_code](https://i.imgur.com/COTzU2l.png)
![proof_output](https://i.imgur.com/ic3qk6E.png)

# How to fix?

- 用XOR swap兩數值的時候要先比對兩數字的參考位置 
- 陣列數值用XOR 交換時要先檢查index是否相同 

# Code

```
#include <iostream>
using namespace std;
void t(int &a,int &b){
  a = a^b;
  cout << "line 1 : a="<< a <<" b="<< b <<endl;
  b = a^b;
  cout << "line 2 : a="<< a <<" b="<< b <<endl;
  a = a^b;
  cout << "line 3 : a="<< a <<" b="<< b <<endl;
}
int main(){
  int x[] = {2,2};
  t(x[0],x[0]);
  cout << x[0] << " " << x[0] << endl;
}
```

- reference : https://en.wikipedia.org/wiki/XOR_swap_algorithm
