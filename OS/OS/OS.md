
# 操作系统学习

![operatingsystemsiconslinuxwindowsandroidmaciosiconsvector.jpg](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/56354a5b6630b31c15d5e9a0133ad33d.jpg)
+ [视频链接](https://space.bilibili.com/202224425/video)
+ [课件链接](http://jyywiki.cn/OS/2022/)
+ [Lab链接](https://nju-projectn.github.io/ics-pa-gitbook/ics2021/PA0.html)
+ [阅读材料链接](http://jyywiki.cn/OS/OS_References)

## 操作系统概述
> 阅读材料链接
+ [JYY's read link](http://jyywiki.cn/OS/2022/notes/1)

- [X] 为什么要学操作系统呢？
+ 为什么要学微积分/离散数学/XXXX/……？
+ 长辈/学长：~~擦干泪不要问为什么~~


微积分 “被混起来” 的几件事

+ Newton 时代的微积分 (启蒙与应用)
	+ 现代方法：Mathematica, sympy, sage
		+ 这也是为什么我主张第一门语言学 Python
+ Cauchy 时代的微积分 (严格化与公理化)
	+ 以及之后各种卡出的 bug (Weierstrass 函数、Peano 曲线……)
+ 微积分的现代应用
优化、有限元、PID……

```python
from sympy import *
x = var('x')
atan(x)
init_printing()
integrate(atan(x))
diff(atan(x))
integrate( 1 / (x**3 + x**2 + x))

```
![](./OS.assets/2022-07-26_15-05.png)
<font color="red" face=Monaco size=3> 你体内的 “编程力量” 尚未完全觉醒 </font> 

+ 每天都在用的东西，你还没搞明白
	+ 窗口是怎么创建的？[为什么 Ctrl-C 有时不能退出程序？](https://stackoverflow.blog/2017/05/23/stack-overflow-helping-one-million-developers-exit-vim/)
+ 组里的服务器有 128 个处理器，但你的程序却只能用一个 😂
+ 你每天都在用的东西，你却实现不出来
	+ 浏览器、编译器、IDE、游戏/外挂、任务管理器、杀毒软件、病毒……

<font color="red" face=Monaco size=3> 《操作系统》给你有关 “编程” 的全部 </font>

+ 悟性好：学完课程就在系统方向 “毕业”
	+ 具有编写一切 “能写出来” 程序的能力 (具备阅读论文的能力)
+ 悟性差：内力大增
	+ 可能工作中的某一天想起上课提及的内容

<div style="border-radius:15px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px;">
充满热情而且相当聪明的学生...早就听说过物理学如何有趣...相对论、量子力学……<br>但是，当他们学完两年以前那种课程后，许多人就泄气了……学的还是斜面、静电这样的内容<br>
<div style="text-align:right;padding:0 15px;">
——《The Feynman Lectures on Physics, 1963》
</div>
</div>




我学《操作系统》的时候 (2009)，大家都说操作系统很难教
- 使用豆瓣评分高达 5.7/10 的 “全国优秀教材
	+ 没有正经的实验 (写一些 16-bit code)
	+ 完全错误的 toolchain，调试全靠蛮力和猜
	+ 为了一点微不足道的分数内卷、沾沾自喜、失去 integrity

+ 这么玩，脖子都要被美国人掐断了
	+ 这门课的另一个意义：告诉你可以去变得更强、真正的强

什么是操作系统?
	
<details>
  <summary style="color:darkcyan">
   What is Operating System ?
  </summary>
  <p>
  Operating System: A body of software, in fact, that is responsible for making it easy to run programs (even allowing you to seemingly run many at the same time), allowing programs to share memory, enabling programs to interact with devices, and other fun stuff like that. (OSTEP)
  </p>
</details>
很多疑点：

+ “programs” 就完了？那么多复杂的程序呢！
+ “shared memory, interact with devices, ...”？


**“管理软/硬件资源、为程序提供服务” 的程序？**
![](./OS.assets/os-classify.jpg)

“精准” 的定义毫无意义
问出正确的问题：操作系统如何从一开始变成现在这样的？
+ 三个重要的线索
	+ 计算机 (硬件)
	+ 程序 (软件)
	+ 操作系统 (管理软件的软件)


> 本课程讨论狭义的操作系统
- 对单一计算机硬件系统作出抽象、支撑程序执行的软件系统
- 学术界谈论 “操作系统” 是更广义的 “System” (例子：OSDI/SOSP)

跨时代、非凡的天才设计，但很简单 (还不如我们数电实验课做的 CPU 复杂呢)：

计算机系统 = 状态机 (ICS 课程的 takeaway message)
标准的 Mealy 型数字电路
ENIAC (1946.2.14；请在这个特殊的节日多陪陪你的电脑)

<div align="center">
<img src="./OS.assets/eniacrun.jpg" width="60%" styles="text-align:center;">
</div>

---
**电子计算机实现**
- 逻辑门：真空电子管
- 存储器：延迟线 (delay lines)
- 输入/输出：打孔纸带/指示灯
<table>
<tr>
	<td><img src="./OS.assets/vaccum-tube.gif" width="250px"></td>
	<td><img src="./OS.assets/throw-ball.gif" width="300px"></td>
	<td><img src="./OS.assets/delay-memory-fig2-s.gif" width="400px"></td>
</tr>
<tr>
	<td>逻辑门：真空电子管</td>
	<td>存储器：延迟线 (delay lines)</td>
	<td>输入/输出：打孔纸带/指示灯</td>
</tr>

</table>

ENIAC 程序是用物理线路 “hard-wire” 的

+ 重编程需要重新接线
	+ [ENIAC Simulator](https://www.cs.drexel.edu/~bls96/eniac/); [sieve.e](./OS.Demo/sieve.e)

最早成功运行的一系列程序：打印平方数、素数表、计算弹道……
- 大家还在和真正的 “bugs” 战斗


### 1940s 的操作系统
<div align="center">
<div style="border-radius:10px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px;width:550px;">
没有操作系统！
</div>

</div>

能把程序放上去就很了不起了!
+ 程序直接用指令操作硬件
+ 不需要画蛇添足的程序来管理它
---
### 1950s 的计算机
更快更小的逻辑门 (晶体管)、更大的内存 (磁芯)、丰富的 I/O 设备
+ I/<br>O 设备的速度已经严重低于处理器的速度，中断机制出现 (1953)
<div align='center'>
  <img src='./OS.assets/2022-07-29_18-26.png' width='70%' styles='text-align:center;'>
</div>

#### 1950s 的程序
可以执行更复杂的任务，包括通用的计算任务


希望使用计算机的人越来越多；希望调用 API 而不是直接访问设备
Fortran 诞生 (1957)

```fortran
C---- THIS PROGRAM READS INPUT FROM THE CARD READER,
C---- 3 INTEGERS IN EACH CARD, CALCULATE AND OUTPUT
C---- THE SUM OF THEM.
  100 READ(5,10) I1, I2, I3
   10 FORMAT(3I5)
      IF (I1.EQ.0 .AND. I2.EQ.0 .AND. I3.EQ.0) GOTO 200
      ISUM = I1 + I2 + I3
      WRITE(6,20) I1, I2, I3, ISUM
   20 FORMAT(7HSUM OF , I5, 2H, , I5, 5H AND , I5,
     *   4H IS , I6)
      GOTO 100
  200 STOP
      END
---
```

#### 1950s 的程序 (cont'd)
一行代码，一张卡片

看到上面 1, 2, ... 80 的标号了吧！
7-72 列才是真正的语句 (这就是为什么谭浩强要教你要画流程图)

<div align="center">
<img src="./OS.assets/fortran-card.jpg" width="60%" styles="text-align:center;">
</div>

#### 1950s 的操作系统


<div align="center">
<div style="border-radius:10px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px;width:550px;">
管理多个程序依次排队运行的库函数和调度器。
</div>

</div>

写程序、跑程序都是非常费事的 (比如你写了个死循环……)
+ 计算机非常贵 ($50,000-$1,000,000)，一个学校只有一台
+ 产生了集中管理计算机的需求： <font color="red" face=Monaco size=3>  多用户排队共享计算机 </font> 

**操作系统的概念开始形成**
+ 操作 (operate) 任务 (jobs) 的系统 (system)
	+ “批处理系统” = 程序的自动切换 (换卡) + 库函数 API
	+ Disk Operating Systems (DOS)
		+ 操作系统中开始出现 “设备”、“文件”、“任务” 等对象和 API

### 1960s 的计算机

<font color="red" face=Monaco size=3> 集成电路、总线出现 </font>
+ 更快的处理器
+ 更快、更大的内存；虚拟存储出现
	+ 可以同时载入多个程序而不用 “换卡” 了
+ 更丰富的 I/O 设备；完善的中断/异常机制
<div align="center">
<img src="./OS.assets/sketchpad.jpg" width="400px" height="210px" styles="text-align:center;">
</div>

#### 1960s 的程序
> 更多的高级语言和编译器出现

+ COBOL (1960), APL (1962), BASIC (1965)
	+ Bill Gates 和 Paul Allen 在 1975 年实现了 Altair 8800 上的 BASIC 解释器
+ 计算机科学家们已经在今天难以想象的计算力下开发惊奇的程序

<div align="center">
<img src="./OS.assets/spacewar.jpg" width="60%" styles="text-align:center;">
</div>

#### 1960s 的操作系统

<div align="center">
<div style="border-radius:10px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:10px;padding:15px;width:600px;">
能载入多个程序到内存且灵活调度它们的管理程序，包括程序可以调用的 API。
</div>

</div>


<font color="red" face=Monaco size=3> 同时将多个程序载入内存 </font>是一项巨大的能力

+ 有了进程 (process) 的概念
+ 进程在执行 I/O 时，可以将 CPU 让给另一个进程
	+ 在多个地址空间隔离的程序之间切换
	+ 虚拟存储使一个程序出 bug 不会 crash 整个系统

> **操作系统中自然地增加进程管理 API**

#### 1960s 的操作系统 (cont'd)
<font color="red" face=Monaco size=4> 既然操作系统已经可以在程序之间切换，为什么不让它们定时切换呢？ </font>

**基于中断 (例如时钟) 机制**
+ 时钟中断：使程序在执行时，异步地插入函数调用
+ 由操作系统 (调度策略) 决定是否要切换到另一个程序执行
+ Multics (MIT, 1965)
	+ 现代操作系统诞生


### 1970s+ 的计算机
**集成电路空前发展，个人电脑兴起，“计算机” 已与今日无大异**
+ CISC 指令集；中断、I/O、异常、MMU、网络
+ 个人计算机 (PC 机)、超级计算机……
<div align="center">
<img src="./OS.assets/35247-93685-000-lead-Apple-II-xl.jpg" width="420px" height="220px" styles="text-align:center;">
</div>

#### 1970s+ 的程序
PASCAL (1970), C (1972), …
+ 今天能办到的，那个时代已经都能办到了——上天入地、图像声音视频、人工智能……
+ 个人开发者 (Geek Network) 走上舞台
<div align="center">
<table>


<tr>
	<td><img src="./OS.assets/wordstarvig.jpg" width="450px"></td>
</tr>

<tr>
	<td>Wordstar (1979)</td>
</tr>

</table>
</div>

#### 1970s+ 的操作系统
<div align="center">
<div style="border-radius:10px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:10px;padding:15px;width:600px;">
分时系统走向成熟，UNIX 诞生并走向完善，奠定了现代操作系统的形态。
</div>

</div>


+ 1973: 信号 API、管道 (对象)、grep (应用程序)
+ 1983: BSD socket (对象)
+ 1984: procfs (对象)……
+ UNIX 衍生出的大家族
	+ `1BSD (1977), GNU (1983), MacOS (1984), AIX (1986), Minix (1987), Windows (1985), Linux 0.01 (1991), Windows NT (1993), Debian (1996), Windows XP (2002), Ubuntu (2004), iOS (2007), Android (2008), Windows 10 (2015), ……`

### 今天的操作系统
<div align="center">
<div style="border-radius:10px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:15px;width:600px;">
通过 “虚拟化” 硬件资源为程序运行提供服务的软件。
</div>
</div>


**空前复杂的系统之一**
+ 更复杂的处理器和内存
	+ 非对称多处理器 (ARM big.LITTLE; Intel P/E-cores)
	+ Non-uniform Memory Access (NUMA)
	+ 更多的硬件机制 Intel-VT/AMD-V, TrustZone/SGX, TSX, ...
+ 更多的设备和资源
	+ 网卡、SSD、GPU、FPGA...
+ 复杂的应用需求和应用环境
	+ 服务器、个人电脑、智能手机、手表、手环、IoT/微控制器……

**理解操作系统：三个根本问题**

> 操作系统服务谁？

+ <font color="red" face=Monaco size=3> 程序 = 状态机 </font>
+ 课程涉及：多线程 Linux 应用程序
	
> (设计/应用视角) 操作系统为程序提供什么服务？

+ <font color="red" face=Monaco size=3> 操作系统 = 对象 + API </font>
+ 课程涉及：POSIX + 部分 Linux 特性

> j(实现/硬件视角) 如何实现操作系统提供的服务？
+ <font color="red" face=Monaco size=3> 操作系统 = C 程序 </font>
	+ 完成初始化后就成为 interrupt/trap/fault handler
+ 课程涉及：xv6, 自制迷你操作系统

<font color="red" face=Monaco size=3> 计算机专业学生必须具备的核心素质。 </font>

1. 是一个合格的操作系统用户
	+ 会 STFW/RTFM 自己动手解决问题
	+ 不怕使用任何命令行工具
	+ `vim`, `tmux`, `grep`, `gcc`, `binutils`, `...`
2. 不惧怕写代码
	+ 能管理一定规模 (数千行) 的代码
	+ 能在出 bug 时默念 “机器永远是对的、我肯定能调出来的”
		+ 然后开始用正确的工具/方法调试
> 给 “学渣” 们的贴心提示：补基础、补基础、补基础


### 如何学好操作系统

## 操作系统上的程序
复习：操作系统
+ 应用视角 (设计): 一组对象 (进程/文件/...) + API
+ 硬件视角 (实现): 一个 C 程序
本次课回答的问题
---

+ [x] : 到底什么是 “程序”？
	+ 程序的状态机模型 (和编译器)
	+ 操作系统上的 {最小/一般/图形} 程序

### 数字电路与状态机

**数字逻辑电路**

+ 状态 = 寄存器保存的值 (flip-flop)
+ 初始状态 = RESET (implementation dependent)
+ 迁移 = 组合逻辑电路计算寄存器下一周期的值

例子：

1. $X^{\prime} = \neg X \wedge Y$ 
2. $Y^{\prime} = \neg X \wedge  \neg Y$ 


```c
#define REGS_FOREACH(_)  _(X) _(Y)
#define RUN_LOGIC        X1 = !X && Y; \
                         Y1 = !X && !Y;
#define DEFINE(X)        static int X, X##1;
#define UPDATE(X)        X = X##1;
#define PRINT(X)         printf(#X " = %d; ", X);

int main() {
  REGS_FOREACH(DEFINE);
  while (1) { // clock
    RUN_LOGIC;
    REGS_FOREACH(PRINT);
    REGS_FOREACH(UPDATE);
    putchar('\n'); sleep(1);
  }
}
```
> 更完整的实现：数码管显示

输出数码管的配置信号
+ [logisim.c](./OS.Demo/logisim.c)
+ 会编程，你就拥有全世界！
	+ [seven-seg.py](./OS.Demo/seven-seg.py)
	+ 同样的方式可以模拟任何数字系统
		+ 当然，也包括计算机系统
你还体验了 UNIX 哲学

<div style='border-radius:15px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px; font-family:"Source Code Pro";font-size:16px'>
 Make each program do one thing well<br>
Expect the output of every program to become the input to another
Hmm....
 
  <div style='text-align:right;padding:0 15px;'>
  -- Unix philosophy
	
  </div>
</div>

### 什么是程序?(源代码)

你可能需要<font color='red' face=Monaco size=3>《程序设计语言的形式语义》</font> 


程序就是状态机 (你在 gdb 里看到的)
+ 试试程序吧 [hanoi-r.c](./OS.Demo/hanoi-r.c)

```c
#include <stdio.h>
#include "hanoi-r.c"

int main(){
	hanoi(3,'A','B','C');
}
```

`gcc -g main.c`
`gdb a.out`
`layout src`
`start`
`step`
`info frame`

#### C 程序的状态机模型 (语义，semantics)
+ 状态 = 堆 + 栈
+ 初始状态 = main 的第一条语句
+ 迁移 = 执行一条简单语句
	+ 任何 C 程序都可以改写成 “非复合语句” 的 C 代码
	+ [真的有这种工具](https://cil-project.github.io/cil/) (C Intermediate Language) 和[解释器](https://gitlab.com/zsaleeba/picoc)

(这还只是 “粗浅” 的理解)<br>
`Talk is cheap. Show me the code. (Linus Torvalds):`
 任何真正的理解都应该落到可以执行的代码

#### C 程序的语义
C 程序的状态机模型 (语义，semantics)
+ 状态 = stack frame 的列表 (每个 frame 有 PC) + 全局变量
+ 初始状态 = main(argc, argv), 全局变量初始化
+ 迁移 = 执行 top stack frame PC 的语句; PC++
	+ 函数调用 = push frame (frame.PC = 入口)
	+ 函数返回 = pop frame
> 应用：将任何递归程序就地转为非递归

汉诺塔难不倒你 [hanoi-nr.c](./OS.Demo/hanoi-nr.c)

`A → B, B → A `的也难不倒你

+ 还是一样的 call()，但放入不同的 Frame


### 什么是程序？(二进制)
还是状态机

+ 状态 = 内存  + 寄存器 
+ 初始状态 = (稍后回答)
+ 迁移 = 执行一条指令
	+ 我们花了一整个《计算机系统基础》解释这件事
	+ gdb 同样可以观察状态和执行

操作系统上的程序
+ 所有的指令都只能计算
	+ deterministic: mov, add, sub, call, ...
	+ non-deterministic: rdrand, ...
	+ 但这些指令甚至都无法使程序停下来 (NEMU: 加条 trap 指令)

我们的程序有一个初始状态,我们假设程序没有输入，那么程序永远都是从内存取指令执行 `M[R[PC]]` `(M : Memory , R : register)` 那么我们的程序执行过程就是一条直线。

其实并不是这样的，我们有很多指令并不是确定的.
如生成随机数

```C
#inlcude <stdio.h>
#inlucde <unistd.h>
int main(){
	while(1){
		asm volatile("rdrand %rax");
	}
}
```
我们可以调试这个程序 下 `watchpoint` `watch $rax`

当指令为不确定指令时这时候我们的状态机就产生了分叉，然后一直执行并始终有可能回到过去的状态,这时候我们的状态机就进入	了死循环。我们发现这个状态机停都停不下来，会一直执行下去.


<font color='red' face=Monaco size=3>一条特殊的指令 </font> 

>  调用操作系统 syscall

+ 把 $(M,R)$ 完全交给操作系统，任其修改
	+ 一个有趣的问题：如果程序不打算完全信任操作系统？
+ 实现与操作系统中的其他对象交互
	+ 读写文件/操作系统状态 (例如把文件内容写入$M$)
	+ 改变进程 (运行中状态机) 的状态，例如创建进程/销毁自己

程序 = 计算 + syscall
+ [X] 问题：怎么构造一个最小的 Hello, World？

**构造最小的 Hello, World**

```c
int main() {
  printf("Hello, World\n");
}
```
gcc 编译出来的文件不满足 “最小”
+ `--verbose` 可以查看所有编译选项 (真不少)
	+ `printf` 变成了 `puts@plt`
+ `-static` 会复制 `libc` 

<font color='red' face=Monaco size=3>直接硬来？</font><br> 
当我们只对该文件进行编译时，发现这个文件确实挺小
![](./OS.assets/2022-07-30_17-27.png)

这时候我们能不能直接进行链接呢?<br>
首先ld 给了我们一个警告 说找不到 `_start` 函数，这个我们可以把main函数的名称改成 `_start` 来绕过这个报错,即使是这样还是链接失败，提示找不到 `puts`

![alt](./OS.assets/2022-07-30_17-34.png)

这时候我们把 `printf` 给注释掉的话，发现能成功编译并链接，但当我们运行这个编译链接后的程序之后，我们获得了 `Segmentation Fault`
![alt](./OS.assets/2022-07-30_17-40.png)

当我们在函数体里加一条 `while(1);` 语句再编译链接，发现程序能正常运行！
![alt](./OS.assets/2022-07-30_17-54.png)
那为什么当 `_start` 函数体为空时会出现错误?

我们可以使用 `gdb` 来观察这个程序究竟做了什么

---
**强行编译 + 链接：gcc -c + ld**
+ 直接用 ld 链接失败
	ld 不知道怎么链接库函数……
+ 空的 main 函数倒是可以
	+ 链接时得到奇怪的警告 (可以定义成 _start 避免警告)
	+ 但 Segmentation Fault 了……
+ [x] 问题：为什么会 Segmentation Fault？

+ <font color='red' face=Monaco size=3>当然是观察程序 (状态机) 的执行了</font> 
	+ 初学者必须克服的恐惧：<font color='red' face=Monaco size=3> STFW/RTFM</font> ([Menu 非常有用](https://sourceware.org/gdb/documentation/))
	+ starti 可以帮助我们从第一条指令开始执行程序
		+ gdb 可以在两种状态机视角之间切换 (layout)


**解决异常退出**

有办法让状态机 “停下来” 吗？

+ 纯 “计算” 的状态机：不行
+ 要么死循环，要么 undefined behavior

> 解决办法：syscall
```c
#include <sys/syscall.h>

int main() {
  syscall(SYS_exit, 42);
}
```
调试代码：syscall 的实现在哪里？
+ 坏消息：在 libc 里，不方便直接链接
+ 好消息：代码很短，而且似乎看懂了

Hello, World 的汇编实现

[minimal.S](./OS.Demo/minimal.S)

```armasm
movq $SYS_exit,  %rax   # exit(
movq $1,         %rdi   #   status=1
syscall                 # );
```
Note: gcc 支持对汇编代码的预编译 (还会定义 __ASSEMBLER__ 宏)

~~我是从哪里获得这些黑科技代码的？？？~~

+ syscall (2), syscalls (2)
	+ The Friendly Manual 才是最靠谱的信息来源

回顾：状态机视角的程序
+ 程序 = 计算 → syscall → 计算 → ...


**彩蛋：ANSI Escape Code**
为什么 Hello World 有颜色？？

特殊编码的字符实现终端控制

+ [vi.c](https://git.busybox.net/busybox/tree/editors/vi.c) from busybox
+ telnet towel.blinkenlights.nl (电影；Ctrl-] and q 退出)
+ dialog --msgbox 'Hello, OS World!' 8 32
+ ssh sshtron.zachlatta.com (网络游戏)
	+ 所以编程可以从一开始就不那么枯燥
	+ 看似复杂，实际简单明了
### 如何在程序的两个视角之间切换

如何在程序的两个视角之间切换？
“状态机” 顺便解决了一个非常重要的基本问题：


什么是编译器？？？

编译器：源代码  (状态机) → 二进制代码  (状态机)

$$
\color{darkcyan}
C = compile(S)
$$

编译 (优化) 的正确性 (Soundness):

+ <font color='red' face=Monaco size=3>S 与 C 的可观测行为严格一致</font> 
	+ system calls; volatile variable loads/stores; termination
+ Trivially 正确 (但低效) 的实现
	+ 解释执行/直接翻译 $S$ 的语义


现代 (与未来的) 编译优化
在保证观测一致性 (sound) 的前提下改写代码 (rewriting)

+ Inline assembly 也可以参与优化
	+ 其他优化可能会跨过不带 barrier 的 asm volatile
+ Eventual memory consistency
+ Call to external CU = write back visible memory
	+ talk is cheap, show me the code!

这给了我们很多想象的空间
+ Semantic-based compilation (synthesis)
+ AI-based rewriting
+ Fine-grained semantics & system call fusion


<font color='red' face=Monaco size=3>进入 PL 的领域</font> 


> PL 领域 (的很多人) 有一种倾向：用数学化的语言定义和理解一切 (all about semantics)

~~所以你看一眼 paper 就觉得自己瞎了~~
+ 但背后的直觉依然是 system/software 的
	+ (我们是人，不是无情的数学机器 😂)
	+ 溜了溜了，回到 system 的世界

**Further readings**
+ [An executable formal semantics of C with applications](https://dl.acm.org/doi/10.1145/2103621.2103719) (POPL'12) 
  + [Download Paper PDF](./OS.assets/compcert-backend.pdf)
+ [CompCert C verified compiler](https://compcert.org/motivations.html) and a [paper](https://xavierleroy.org/publi/compcert-backend.pdf)(POPL'06, Most Influential Paper Award 🏅)
+ [Copy-and-patch compilation](https://dl.acm.org/doi/10.1145/3485513) (OOPSLA'21, Distinguished Paper 🏅)
  + [Download Paper PDF](./OS.assets/3485513.pdf)

**操作系统中的一般程序**
<div style='border-radius:15px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px;'>
 和 minimal.S 没有本质区别：程序 = 计算 → syscall → ... 
</div>


操作系统收编了所有的硬件/软件资源
+ 只能用操作系统允许的方式访问操作系统中的对象
	+ 从而实现操作系统的 “霸主” 地位
	+ 例子：[tryopen.c](./OS.Demo/tryopen.c)
+ 这是为 “管理多个状态机” 所必须的
	+ 不能打架，谁有权限就给他

**(二进制) 程序也是操作系统中的对象**<br>
可执行文件
+ <font color='red' face=Monaco size=3>与大家日常使用的文件 (a.c, README.txt) 没有本质区别</font> 
+ 操作系统提供 API 打开、读取、改写 (都需要相应的权限)
 
查看可执行文件
+ vim, cat, xxd 都可以直接查看可执行文件
	+ vim 中二进制的部分无法 “阅读”，但可以看到字符串常量
	+ 使用 xxd 可以看到文件以 "\x7f" "ELF" 开头
	+ vscode 有 Hex editor 插件

**系统中常见的应用程序**

1. Core Utilities (coreutils)
+ standard programs for text and file manipulation
+ 系统中安装的是 [GNU Coreutils](https://www.gnu.org/software/coreutils/)
	+ 有较小的替代品 [busybox](https://www.busybox.net/)

2. 系统/工具程序
+ bash, [binutils](https://www.gnu.org/software/binutils/), apt, ip, ssh, vim, tmux, jdk, python, ...
	+ 这些工具的原理都不复杂 (例如 apt 其实只是 dpkg 的壳)
	+ [Ubuntu Packages](https://packages.ubuntu.com/) (和 apt-file 工具) 支持文件名检索
		+ 例子：找不到 SDL2/SDL.h 时...

3. 其他各种应用程序
+ 浏览器、音乐播放器……

操作系统中的程序：Dark Side<br>
> 杀人的面试题 (1)：一个普通的、人畜无害的 Hello World C 程序执行的第一条指令在哪里？

等价问法

+ “二进制程序状态机的初始状态是什么？”
	+ main 的第一条指令 ❌
	+ libc 的 _start ❌

<font color='red' face=Monaco size=3>问 gdb 吧</font> 
  + `info proc {mappings,...}` - 打印进程内存


main() 之前发生了什么？
`ld-linux-x86-64.so` 加载了 `libc`

+ 之后 libc 完成了自己的初始化
	+ RTFM: [libc startup on Hurd](https://www.gnu.org/software/hurd/glibc/startup.html)
	+ main() 的开始/结束并不是整个程序的开始/结束
	+ 例子：[hello-goodbye.c](./OS.Demo/hello-goodbye.c)

谁规定是 ld-linux-x86-64.so，而不是 rtfm.so？
+ readelf 告诉你答案
+ (计算机系统不存在玄学；一切都建立在确定的机制上)
	回顾 gcc --verbose

我们其实完全可以修改 `ld-linux-x86-64.so`
我们先使用vim的替换模式将 `ld-linux-x86-64.so` 替换成我们想替换的路径. 然后在 vim 里 `:%!xxd` 将刚刚多余的替换成 0
替换完之后 `:%!xxd -r` 还原文件.

<table>
  <tr>
	<td>替换目标</td>
	<td>将多余部分填充0</td>
	<td>还原成二进制格式</td>
  </tr>
  <tr>
	<td><img src='./OS.assets/2022-07-31_00-52.png' width='400px'></td>
	<td><img src='./OS.assets/2022-07-31_00-54.png' width='400px'></td>
	<td><img src='./OS.assets/2022-07-31_00-57.png' width='400px'></td>
  </tr>
</table>

操作系统中的程序：Dark Side<br>
> 杀人的面试题 (2)：main 执行之前、执行中、执行后，发生了哪些操作系统 API 调用？

+ (计算机系统不存在玄学；一切都建立在确定的机制上)
+ 所以你应该有一个强烈的信念：这个问题是可以回答的


<span style='color:blue'>
</span>
<details>
  <summary style='color:darkcyan'>
  What is Trace ?
  </summary>
  <p style="color:darkcyan">
  In general, trace refers to the process of following anything from the beginning to the end. For example, the traceroute command follows each of the network hops as your computer connects to another computer.
  </p>
</details>

**打开程序的执行：Trace (踪迹)**

> 这门课中很重要的工具：strace

+ system call trace
+ 理解程序运行时使用的系统调用
	+ demo: strace ./hello-goodbye
	+ **`strace -f gcc ./logisim.c |& vim -`**
	+ 在这门课中，你能理解 strace 的输出并在你自己的操作系统里实现相当一部分系统调用 (mmap, execve, ...)


<font color='red' face=Monaco size=4>本质上，所有的程序和 Hello World 类似</font> 

程序 = 状态机 = 计算 → syscall → 计算 →

+ 被操作系统加载
	+ 通过另一个进程执行 execve 设置为初始状态
+ 状态机执行
	 进程管理：fork, execve, exit, ...
	+ 文件/设备管理：open, close, read, write, ...
	+ 存储管理：mmap, brk, ...
+ 直到 _exit (exit_group) 退出

(初学者对这一点会感到有一点惊讶)
+ 说好的浏览器、游戏、杀毒软件、病毒呢？都是这些 API 吗？

Yes! - 这些 API 就是操作系统的全部
编译器 (gcc)，代表其他工具程序

+ 主要的系统调用：execve, read, write
+ strace -f gcc a.c (gcc 会启动其他进程)
	+ 可以管道给编辑器 vim -
	+ 编辑器里还可以 %!grep (细节/技巧)

图形界面程序 (xedit)，代表其他图形界面程序 (例如 vscode)

+ 主要的系统调用：poll, recvmsg, writev
+ strace xedit
	+ 图形界面程序和 X-Window 服务器按照 X11 协议通信
	+ 虚拟机中的 xedit 将 X11 命令通过 ssh (X11 forwarding) 转发到 Host

**各式各样的应用程序**<br>
都在 <font color='red' face=Monaco size=3>操作系统 API (syscall)</font>  和 <font color='red' face=Monaco size=3>操作系统中的对象</font> 上构建

**1. 窗口管理器**
+ 管理设备和屏幕 (read/write/mmap)
+ 进程间通信 (send, recv)

**2. 任务管理器**
+ 访问操作系统提供的进程对象 (readdir/read)
+ 参考 gdb 里的 info proc *

**3. 杀毒软件**
+ 文件静态扫描 (read)
+ 主动防御 (ptrace)
+ 其他更复杂的安全机制……

## 多处理器编程


## 理解并发程序执行




## 并发控制

### 互斥

### 同步

> 如何在多处理器上协同多个线程完成任务？

+ 典型的同步问题：生产者-消费者；哲学家吃饭
+ 同步的实现方法：信号量、条件变量

**概念: 同步(Synchronization)**

<font color=green>两个或两个以上随时间变化的量在变化过程中保持一定的相对关系</font>

+ iPhone/iCloud 同步 (手机 vs 电脑 vs 云端)
+ 变速箱同步器 (合并快慢速齿轮)
+ 同步电机 (转子与磁场速度一致)
+ 同步电路 (所有触发器在边沿同时触发)

<font color="green" face=Consolas> 异步 (Asynchronous) = 不同步 </font>

上述很多例子都有异步版本 (异步电机、异步电路、异步线程)

并发程序中的同步

并发程序的步调很难保持 “完全一致”

线程同步: <font color="red" face=Monaco size=3> 在某个时间点共同达到互相已知的状态 </font> 




## 真实世界的并发编程



## 并发 BUG 与应对



## 操作系统的状态机模型

+ 软件和硬件的桥梁
+ 操作系统的加载和初始化
+ AbstractMachine 代码导读

> OSLabs

+ <font color="red" face=Monaco size=3> Lab0 (amgame): 熟悉代码框架 </font>
+ **Lab1 (pmm):** `Physical memory management`
	+ 多处理器 (bare-metal) 上的 kalloc/free
+ **Lab2 (kmt):** `Kernel multi-threading`
	+ 中断和异常驱动的上下文 (线程) 切换
+ **Lab3 (uproc):** `User processes`
	+ 虚拟地址空间、用户态进程和系统调用
+ **Lab4 (vfs):** `Virtual file system`
	+ devfs, procfs, 简单的文件系统；ELF 加载器

### 硬件和软件的桥梁

我们已经知道如何写一个 “最小” 的 C 程序了：
minimal.S

不需要链接任何库，就能在操作系统上运行

“程序 = 状态机” 没问题

带来更多的疑问

但谁创建的这个状态机？？？

当然是操作系统了……呃……

<font color="red" face=Monaco size=3>  这个程序可以在没有操作系统的硬件上运行吗？
 </font>

“启动” 状态机是由 “加载器” 完成的

加载器也是一段程序 (状态机)

这个程序由是由谁加载的？


## 状态机模型的应用


`strace -T a.out &| nvim -`

## 操作系统上的进程



## 进程的地址空间


## 系统调用和 Shell


## C 标准库的实现



## fork的应用


## 什么是可执行文件

## 动态链接和加载


## xv6 代码导读

### 环境搭建


1. 下载源码
ARCH 环境

```bash
sudo pacman -S riscv64-linux-gnu-gcc

```

```
make qemu

```

![XV6 Source Code](https://github.com/mit-pdos/xv6-riscv) 

```bash

make -nB qemu | nvim -
# :set nowrap
# :%s/ /\r /g
<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> A </kbd> + <kbd class="keybord"> X </kbd>&ensp; 退出 QEMU

<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> A </kbd> + <kbd class="keybord"> C </kbd>&ensp; 启动 QEMU 的模拟器



```


我们可以将多处理器改为 1 `-smp 1`



2. 配置 VScode
> 生成一个 compile_commands.json

+ `bear`

```
bear make qemu
```

+ `compiledb`

![compiledb github link](https://github.com/nickdiego/compiledb) 


调试 xv6
运行 `gdb`

```
.gdbinit:2: Error in sourced command file:
Undefined item: "riscv:rv64".
```

如果在运行 gdb 时遇见上面的错误我们可以使用
`gdb-multiarch` 

在 linux 里我们可以安装 `riscv64-linux-gnu-gdb`

然后再开一个终端我们运行 `make qemu-gdb`

这时候我们成功在第一条指令上停下来了


## Xv6 上下文切换



## 处理器调度



## 操作系统设计

### 输入输出模型

查看 系统中总线上的设备

`lspci -tv` `lsusb -tv`


`/dev/` 中的对象

+ `/dev/pts/[x] - pseudo terminal`
+ `/dev/null - 'Null' 设备`
+ `/dev/zero - '零' 设备`
+ `/dev/random /dev/urandom - 随机数生成器`

`yes` 

`cat /dev/urandom | head -c 512 | xxd`
`cat /dev/zero | head -c 512 | xxd`

`stty -a`

`man termios`


GPU 编程


gcc -> nvcc

binutils -> cuobjdump

gdb -> cuda-gdb


perf -> nvprof

