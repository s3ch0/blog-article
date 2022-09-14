

## ZIP 伪加密
压缩源文件数据区：50 4B 03 04：这是头文件标记
 
压缩源文件目录区：
50 4B 01 02：目录中文件文件头标记
3F 00：压缩使用的 pkware 版本 
14 00：解压文件所需 pkware 版本 
00 00：全局方式位标记（有无加密，这个更改这里进行伪加密，改为09 00打开就会提示有密码了）
压缩源文件目录结束标志 ：50 4B 05 06：目录结束标记 
 
我们用winhex打开压缩包，搜索504B，点击第二个504B（压缩源文件目录区）
软件：winhex
我们看到上图，红色框住的50 4B 是压缩源文件数据区的头文件标记，它对应的红色框柱的 09 00 并不影响加密属性。
绿色框住的50 4B 是压缩源文件目录区 ，它对应的绿色框柱的 09 00 影响加密属性，当数字为奇数是为加密，为偶数时不加密。
 
因此我们更改标志位保存即可。




zbarimg
xxd
pngcheck
zsteg

```bash
zip -FF full.zip  --out ff_full.zip
```

brainfuck 

[brainfuck decode](https://www.dcode.fr/brainfuck-language)

vmdk文件可以用7z解压

```bash
7z x flag.vmdk -o./
```
[](https://www.splitbrain.org/services/ook)

F5隐写
我能在 `java-11` 的环境下成功运行
在 `java-17` 的环境下会报错。

```bash
git clone https://github.com/matthewgao/F5-steganography
```
在目录内运行 

```bash
java Extract Misc.jpg
```
默认会保存在当前目录内的 `output.txt` 文件里。

[serpent encode](http://serpent.online-domain-tools.com/)


```bash
sudo pacman -S graphicsmagick
```
```bash
gm convert MY-GIF.gif -coalesce +adjoin GIF_Frame%3d.png
```
