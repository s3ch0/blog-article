

# 如何高效使用 Vim?

## 学习 Vim 的资料
[why use vim](http://www.viemu.com/a-why-vi-vim.html)  : 为什么使用 vim (这篇文章解释得较为全面)

[vim-galore](https://github.com/mhinz/vim-galore): 学习vim 的一个较好的资料

[vim-reference](https://learnbyexample.gitbooks.io/vim-reference/content/Introduction.html) : vim说明书

[vim实用技巧](https://library-cdq.oss-cn-beijing.aliyuncs.com/technology/Vim%E5%AE%9E%E7%94%A8%E6%8A%80%E5%B7%A7.pdf) : 一本关于如何高效使用 vim 的书

[vim-golf](http://www.vimgolf.com/)

如果你要低头看着键盘打字，那学习 Vim 的好处并不会立竿见影地显现出来。如果要高效地使用 Vim，并完全脱离鼠标必须学会盲打!!!
以达到在 Vim 中所有的操作都通过键盘完成.

> 这边介绍几个能帮助你熟悉 vim 移动键位的几个网站

[TypingClub](https://www.typingclub.com/): 一个非常棒练习盲打的网站
> <font color=red>下面这些网站都是关于 vim 的一些小游戏</font>

[Pacvim](https://github.com/jmoon018/PacVim) : 这是一个用C++ 编写的开源项目
[vim-snake](https://vimsnake.com/): 贪吃蛇 vim 版

[Vim-Genius](http://www.vimgenius.com/) | [Open Vim Tutorials](https://www.openvim.com/tutorial.html) | [Vim-Adventures](https://vim-adventures.com)

<font color="red" face=Monaco size=3> 我们知道 <kbd class="keybord"> CapsLock </kbd>&ensp;这个键位不是特别经常使用的一个键位，但它又离我们的主键位非常近，并且还比较大所以我们有必要将这个键替换掉 </font>

这时候我们就可以更快地使用 快捷键了
<kbd class="keybord"> Ctrl  </kbd> + <kbd class="keybord"> i </kbd>&ensp;提示
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> e </kbd>&ensp;补全
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> j </kbd>&ensp; 回车
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> u </kbd>&ensp;  删除一整行
<++> TODO

安装 `xcape` 工具
```bash
# ubuntu
sudo apt-get install xcape
# Arch Linux
sudo pacman -S xcape
```
运行命令
```bash
# make CapsLock behave like Ctrl
setxkbmap -option ctrl:nocaps

# make short-pressed Ctrl behave like Escape:
xcape -e 'Control_L=Escape'
```

设置开机自动启动
将上面那两条命令添加到 `~/.xprofile` 文件里
从而让每次 启动 X 服务都运行上面那些命令





## Vim 的基本操作
![wAUpUM.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6fb0ca512816ffb3f079dd474ce42374.png)
vim 与别的编辑器最大的不同,<font color=red>就在于它有多种模式</font>,而在不同的模式下分别负责不同的功能模块.
我们需要进入到相应的模式来快速完成我们的操作。如我们可以进入插模式下来进行字符的输入,在可视模式下完成字符的选取等等....

下面就先来介绍,进入 vim 里默认的模式 `普通模式`
### 普通模式 ( `normal mode` )
在 [vim 实用技巧](https://library-cdq.oss-cn-beijing.aliyuncs.com/technology/Vim%E5%AE%9E%E7%94%A8%E6%8A%80%E5%B7%A7.pdf) 中是这样描述 vim 的普通模式的：
>就像画家只花一小部分时间涂色一样，程序员也只花一小部分时间编写代码。绝大多数时间用来思考、阅读，以及在代码中穿梭浏览。而且，当确实需要做修改时，谁说一定要切换到插入模式才行？我们可以重新调整已有代码的格式，复制它们，移动其位置，或是删除它们。在普通模式中，我们有众多的工具可以利用。

所以当你需要停顿思考要书写什么内容,或者要移动光标时,请退回到普通模式.

#### 移动光标
在 vim 中我们可以使用 <kbd>h</kbd> <kbd>j</kbd> <kbd>k</kbd> <kbd>l</kbd> 来左下上右地移动光标.

<font color=tomato>我们应该尽量少用上下左右方向键，因为上下左右键离我们的主键位太远了，而我们又要经常使用移动光标这个操作，所以如果想熟练使用 vim 的话一定要学会使用 hjkl 来控制光标! ( 或者使用自己的键位 )</font>


> 而这个过程其实并不会很漫长，只需要适应一段时间，你就会喜欢这个设定！当然你也可以玩上面提到的各种 vim 小游戏来快速适应这些操作。

一种简单的记忆方式是左右两边的 <kbd>h</kbd> 和 <kbd>l</kbd> 分别对应左右移动，而食指在键盘的默认位置 <kbd>j</kbd> 则为向下( 向下这个操作相对来说被使用的概率较大 ),反之 <kbd>k</kbd> 为向上。

如果一行非常长的话，你可能会问，如果在行首要将光标移动到行尾的话，难道要有多少个字母就要按多少下 <kbd class="keybord"> l </kbd>&ensp;吗？

<font color="red" face=Monaco size=3> 其实在 vim 里我们可以使用 <kbd> $  ^ </kbd> 分别跳转到行尾和行首</font>

如果你熟悉正则表达式的话可以发现其实 <kbd class="keybord"> ^ </kbd>&ensp;就是表示行首的意思，而 <kbd class="keybord"> $ </kbd>&ensp;就是代表行尾的意思。

我们可以使用 <kbd class="keybord"> w b e </kbd>&ensp; 来实现以单词为单位的跳转。

+ <kbd class="keybord"> w </kbd>&ensp;跳转到当前光标的下一个单词的首字母
+ <kbd class="keybord"> e </kbd>&ensp;跳转到当前光标所在单词的尾字母
+ <kbd class="keybord"> b </kbd>&ensp;跳转到当前光标所在单词的前一个单词(左边)




![gyKgUn.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/60887ebc1d0a5486ee9dea16b41108fe.png)

我们可以通过
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> u </kbd>&ensp; 向上翻页
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> d </kbd>&ensp; 向下翻页
<kbd class="keybord"> H </kbd>&ensp;移动到页面最上方
<kbd class="keybord"> L </kbd>&ensp;移动到页面最下方
<kbd class="keybord"> M </kbd>&ensp;移动到页面中间位置







我们还可以通过使用 <kbd class="keybord"> f{char} / F{char} </kbd>&ensp; 来向左/向右查找对应的字符 **( 字符所处位置 )**

<kbd class="keybord"> t{char} </kbd> / <kbd class="keybord"> T{char} </kbd>&ensp; 效果和 `f(find)`命令一样 唯一不同的是 `t/T` 命令是跳转到要查找单词的前一个字符


<kbd class="keybord"> % </kbd>&ensp; 跳转到成对出现的字符上如现在光标在左括号上`(` 现在我们想跳转到右括号上 `%` 我们只需要在普通模式下按 `%` 号即可


![Pddwc3.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5a69b8f53716db1c9623b3f0273b99d2.png)




### 插入模式 ( `insert mode` )

![diLxcP.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dd6aa7868fd94f9d0439cc366c5c5785.png) 
#### 复合命令
减少无关的移动 a 命令在当前光标之后添加内容，而 `A` 命令则在当前行的结尾添加内容。不管光 标当前处于什么位置，输入 `A` 都会进入插入模式，并把光标移到行尾。
换句话说，它把 `$a` 封装成了一个按键操作。



我们可以这样说，`A` 命令把两个动作 `($a)` 合并成了一次按键。不过它不是唯一一个这样的 命令，很多 Vim 的单键命令都可以被看成两个或多个其他命令的组合。下表列出了类似的一些例子



| 复合命令     | 等效的长命令     |
| ------------ | ---------------- |
| <kbd>C</kbd> | <kbd>c$</kbd>    |
| <kbd>s</kbd> | <kbd>cl</kbd>    |
| <kbd>S</kbd> | <kbd>^c</kbd>    |
| <kbd>I</kbd> | <kbd>^i</kbd>    |
| <kbd>A</kbd> | <kbd>$a</kbd>    |
| <kbd>o</kbd> | <kbd>A<CR></kbd> |
| <kbd>O</kbd> | <kbd>ko</kbd>    |




| 按键操作                       | 用途                          |
| ------------------------------ | ----------------------------- |
| <kbd>Ctrl</kbd> + <kbd>h</kbd> | 删除前一个字符                |
| <kbd>Ctrl</kbd> + <kbd>u</kbd> | 删除至行首                    |
| <kbd>Ctrl</kbd> + <kbd>w</kbd> | 删除前一个单词 (与退格符一样) |

>  这些命令不是插入模式所独有的，甚至也不是 Vim 所独有的，在 Vim 的命令行模 式中，以及在 bash shell 中，也可以使用它们。








![lNuHSh.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e0c04140ce5113bbc61c7c4dc046902b.png)

![TmK9Ua.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e1963c71852d63dc0b9269ec922f252a.png)

### 可视模式 ( `Visual mode` )
在普通模式下我们只需要按 <kbd class="keybord"> v </kbd>&ensp; 即可进入可视模式
还有两种特殊一点的可视模式 (也非常重要)

+ <kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> v </kbd>&ensp; 进入行可视模式 ( `Line Visual Mode` )
+ <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> v </kbd>&ensp; 进入块可视模式 ( `Block Visual Mode` )

#### 行可视模式
行可视模式一般用在复制某些内容然后进行粘贴比较方便

#### 块可视模式

<kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> I </kbd>&ensp; 插入

<kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> A </kbd>&ensp; 插入


### 替换模式 ( `Replace mode` )

我们只需要在普通模式下按 <kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> r </kbd>&ensp; 就能进入替换模式了



## Vim 的实用技巧
我们可以使用一些小的正则表达式来达到很多惊艳的效果

如我们可以使用以下命令
```vim
:%s/^\n$//g
```
来删除文本内所有重复的换行 (回车)



## Vim 的快捷键

## Vim 的窗口
### 窗口管理的默认快捷键

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> w </kbd>&ensp; 

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> w </kbd> + <kbd class="keybord"> s </kbd>&ensp; 上下分屏

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> w </kbd> + <kbd class="keybord"> v </kbd>&ensp; 左右分屏

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> w </kbd> + <kbd class="keybord"> q </kbd>&ensp; 退出光标所在的分屏

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> w </kbd> + <kbd class="keybord"> h j k l </kbd>&ensp; 对应光标 左 上 下 右 的移动 ( 窗口间移动 )


## Vim 里的折叠 ( Folding )
**在vim里关于折叠的操作命令是 `z` **
设置根据语法来进行自动折叠 在大项目里面可能会有一会的延迟

```vim
set foldmethd=syntax
```

+ <kbd class="keybord"> zf </kbd>&ensp;创建折行 
+ <kbd class="keybord"> zo </kbd>&ensp;打开折行
+ <kbd class="keybord"> zc </kbd>&ensp;关闭折行
+ <kbd class="keybord"> zd </kbd>&ensp;删除折行

```vim
zfa{
```
<++>

## Vim 的Buffer

## Vim 的Tags

## Vim 的Tab

## Vim 的寄存器

## Vim 的宏操作

## Vim 的配置

## 其它Vim小技巧
+ [x] 如果你在vim里想查看一下当前文件的路径，那么你可以使用一下方法。
	+ <kbd class="keybord"> {count} </kbd>&ensp;+ <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> G </kbd>&ensp; 我们可以使用:  <kbd class="keybord"> 1 </kbd> + <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> G </kbd>&ensp; 来获得当前文件所处路径
	+ 




<font size=3 color=green>参考</font>
+ [vim-awesome](https://vimawesome.com/)

