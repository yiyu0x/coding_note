stdout無法輸出中文字(utf-8),預設是ascii 噴出以下錯誤

```
UnicodeEncodeError: 'ascii' codec can't encode characters in position 500-520: ordinal not in range()
```

解決方法:
```python
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
```
