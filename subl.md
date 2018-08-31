在mac上安裝sublime text3之後，但是要在terminal打開卻很麻煩，不像vscode可以直接用`code`指令來開啟app。

以下配置，讓sublime text3也能像vscode一樣在terminal中使用自如。

1. 確定sublime text3是否安裝完畢

> file /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/sublime
output : /Applications/Sublime Text.app/Contents/SharedSupport/bin/subl: Mach-O 64-bit executable x86_64
如果這一步找不到就代表安裝沒有完成，請不要往下做

2. 製作link
> ln -s /Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl /usr/local/bin/subl

完成。

以後就可以直接在project裡面用`subl .`來將專案用sublime text3開啟

如果不喜歡subl這個名字，可以在步驟2自己設定link的名稱
