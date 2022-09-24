转换磁盘格式为 GPT 

> 这步操作会清除所有磁盘
我们在这个错误提示的时候，不要重启电脑，直接在键盘上按下 
<kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> F10 </kbd>&ensp;组合键,这时候就会弹出 CMD 命令提示符

```cmd
diskpart
list disk
select disk 0
clean
convert gpt
```
UEFI 引导对应的是 GPT 分区
Legacy 引导对应的是 MBR 分区


还有可能就是主板 BIOS中，磁盘是 MBR 格式，BOOT启动模式一定要对应修改为 Legecy 模式，
不过在新主板中，选项默认双支持，同时支持 Legecy和UEFI模式，就不用修改了，将U盘启动模式对应就好了。
