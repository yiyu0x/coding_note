> $ pip -h

```
Traceback (most recent call last):
  File "/usr/bin/pip", line 9, in <module>
    from pip import main
ImportError: cannot import name main
```

把 `/usr/bin/pip`的 (如果python3就改 `/usr/bin/pip3`)

```
from pip import main
if __name__ == '__main__':
    sys.exit(main())
```

改成

```
from pip import __main__
if __name__ == '__main__':
    sys.exit(__main__._main())
```

即可
