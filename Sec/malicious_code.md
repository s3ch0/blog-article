# 恶意代码分析

![080317_bug.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8de959d522b108e54e0acf6a39e57dab.png)

+ [看雪](https://bbs.pediy.com/)
+ [吾爱破解](https://www.52pojie.cn/)

## 基础知识

### Windows 操作系统中的文件类型

> 可执行文件与不可执行文件 分类是怎么来的?

+ windows操作系统
  + 可执行文件: windows操作系统中有一些文件是原生就支持windows环境的,
  + PE:
    + 一种代码结构,是windows定义的固定格式

`exe,dll,sys`


2. windows下运行代码的基本过程

内存颗粒其实就相当于有好多个小钢珠,而传输二进制时,遇到1就通高一点电流,0就低一点电流,而钢珠会因为电流的不同而发生不同的形变,从而保留了数据

3. windows下恶意代码的常见类型和危害

### 常见的恶意代码类型:

#### 木马
+ **木马特点:**
  + 一定会有通信模块
  + 功能模块上的执行一定是针对性的

举例: 如果我们现在想下载目标机器上的一个文件 基本思路是:
+ 运行exe --> 找文件 --> 上传文件 
+ 而木马则是当 XXX 触发时 执行 XXX



#### 病毒
破坏原有计算机的环境
勒索病毒:破坏原本计算机的文件环境
xxx.exe --> xxx.jiami
1. 识别环境
2. 修改环境
3. 还原环境(大部分有) 勒索软件...

勒索软件有通信功能 代表它有解密的可能性

特点:
绝大部分有密码学相关的东西

密钥的实现:
触发恶意代码的时间
用户名称
操作系统内核版本

本地: --> 简单,容易被破解
生成时间
随机数


#### 蠕虫,捆绑与挖矿算不算一个单独的类型?
> 不算
他们只能算是一种行为

什么叫恶意?
所有触发不符合我们预期结果的行为都叫恶意行为

> hack_browse_data.exe 获取浏览器信息


CIA

有哪些:
1. 破坏环境(文件,操作系统)
2. 计算机相关的 (开机,关机)
3. 信息被泄露
4. 信息被修改


一些关于恶意样本的网站:
+ [微步云](https://s.threatbook.cn/)
+ [Triage](https://tria.ge/)
+ [吾爱破解](https://www.52pojie.cn/forum-32-1.html) 
+ [any.run](https://any.run/)


```c
#include <windows.h>
// 直接可以调用windows默认提供的dll
// 不能调用所有的dll 如 ntdll.dll windows有一部分不开源的函数保存在这个dll里面
// 不能调用自己写的dll

GetProcAddress
// 可以调用所有的
// 可以调用自己的,但是有条件: 这个自己的dll必须在操作系统中提前被使用

LoadLibrary
// 可以调用所有的
// 可以调用自己的
// 不能够调用已经运行的函数地址

```

静态链接
```cpp
#pragma comment (lib,"..//Debug//foo.lib")
```

> 动态链接和静态链接的区别

+ 动态: 在第58行用到了 api 函数才在这里开始导入这个函数
+ 静态: 我不管用不用,导进来再说


![Snipaste_20220410_184020.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7403d67b93776564ef0b57f0d5612684.png)



![Snipaste_20220410_183620.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0fa8bbf90859948a436ff4b84e7131e8.png)

## IDA的使用

功能结构


空格


![Snipaste_20220416_151432.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/08db2843454c0bcbaf51ad67699fccb3.png)




![Snipaste_20220416_152439.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/88128b3bf9f325c20a7178949cad0a20.png)





![Snipaste_20220416_153044.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3c80c884db5be2d29b35c706cac74949.png)


快速定位地址: 按 <kbd>G</kbd> 键就能进行跳转


![Snipaste_20220416_185328.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e10335ec14f19ebbdc1724d9fa46570e.png)


交叉引用的图模式:查看某个函数下还调用了哪些函数,调用关系(一定要选中要查看的函数)

![Snipaste_20220416_190724.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6229e3e91c9b3dbb9188c52a2da406b1.png)

查看某个 函数/字符串 的交叉引用: 按 <kbd>Ctrl</kbd> + <kbd>X</kbd> 键查看函数的交叉引用
> 字符串等,也可以使用 <kbd>Ctrl</kbd> + <kbd>X</kbd> 来进行交叉引用跳转

![Snipaste_20220416_192640.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/94f71cbb528b55f8100e603a872fc8c1.png)

<kbd>Shift</kbd> + <kbd>F12</kbd> 打开IDA的字符串窗口,双击对应的字符串就可以进入到如下界面,然后可以按 <kbd>Ctrl</kbd> + <kbd>X</kbd> 查看该字符串的引用,并跳转

![Snipaste_20220416_193059.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b8773a2011e1747aaaef9cc8b4658ec0.png)


更改函数名字,和变量名字


![Snipaste_20220416_200045.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/203a7bf5a1eaff1112c5ab03935010b6.png)

![Snipaste_20220416_200350.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c8798ea1ec11a4f87891f59b526e9d43.png)



在 IDA 里函数颜色为粉红色且函数尾有 A W 这种字母的,这种函数一般来说是 API 

### IDA插件编写



```python
ea = ScreenEA()
for i in range(0x00,0x50):
    b= Byte(ea+i)
    decode_byte = b ^ 0x55
    PatchByte(ea+i,decode_byte)
	
```

```C++
#include <idc.idc>
static main(){
  auto ea = ScreenEA(),i,b,decode_byte;
  for(i=0x00;i<0x50;i++){
    b = Byte(ea+i);
    decode_byte = b ^ 0x50;
    PatchByte(ea+i,decode_byte);
  }
}

```


```c++
#include <idc.idc>

static list_callers(bad_func)
{
  auto func,addr,xref,source;
  func = LocByName(bad_func); // 根据函数名在ida中寻找到相应的函数地址
  if( func == BADADDR )
  {
    Warning("Not found: %s",bad_func);	
  }
  // 获得该函数的交叉引用
  else
  {
    // 遍历该函数的所有交叉引用
    for(addr = RfirstB(func); addr != BADADDR; addr = RnextB(func,addr) )
    {
      xref = XrefType(); 
      // 筛选出近调用和远调用的引用
      if( xref == fl_CN || xref == fl_CF)
     
      {
        source = GetFunctionName(addr);
        Message("%s is called from 0x%x in %s\n",bad_func,addr,source);
      }
    }
  }
}
static main()
{
  list_callers("");
}

```
想要了解更多关于 IDA 插件的知识,我们可以 STFW 去搜索 IDC

> IDA 用户手册 :在 IDA 里按 <kbd>F1</kbd> 键即可

## 静态分析的结构与经验


### 分支结构
满足条件走绿色
不满足条件走红色
switch
cmp [地址+偏移量] 里面装的是前面几个的跳转条件(一般大于6个才会使用这种方式)
蓝色的线是前面几个 case
绿色的线是 default 条件



### 网络结构

+ TCP: SOCK_STREAM
+ UDP: SOCK_DGRAM
socket 流程
SOCKET: WS2_32
调用 `socket`,有一个前提条件,就是使用 wsa ( windows socket 对象)
例如: `sadata` `wsaData` `WsaStartUp`
1. wsa 相关的
2. socket
3. connect
4. recv / send
5. closesocket
6. wsacleanup




> 在恶意代码分析中,只要存在 GetTickCount , 80%的概率都是确定目标的 uid

遇到勒索软件怎么提高解密的成功几率?
- 记录下被勒索的具体时间 (至少要精确到秒)
  - 原因: 很多的勒索软件的密钥由于需要一对一, 就会使用 GetTickCount 或者是能唯一识别的东西来做密钥的基础.

HTTP: wininet.h
恶意代码 http 使用场景:
攻防对抗环境下:
+ http 协议下命令和结果传输
APT 环境下:
1. 勒索文本的存放
2. 公有环境下存放一些敏感信息
	+ 尤其是遇到 [pastebin](https://pastebin.com/) 类似的网站
	+ 密钥,或者是某个函数的某个参数,某个变量的值
3. 结果存放在网站上



### 文件结构
1. 释放文件:
LoadResource: 从资源文件中找到位置
CreateFile: 创建文件

2. 从变量里直接创建文件
看变量的 HEX 是否存在 PE 相关的东西

3. 从网络去释放文件
	+ 创建结构,下载内容
	+ 先会创建一个 PE 结构,但是没有内容,并保存这个指针
	+ recv 之后 (接收过来的其实就是 meterpreter 的文件结构,以msf举例) 指向刚才的指针
	+ 就可以选择是创建文件,还是直接在内存运行





### 加解密结构

1. 使用微软自带的加解密工具
	Microsoft Base Cryptographic Provider

2. 自己写的加解密算法,但是有随机数的情况
	注册表操作 + 带 RNG 这种字样
	
```shell
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\WOW6432Node\Microsoft\Cryptography\DRM_RNG
```


![Snipaste_20220418_193050.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a686699f6642bd728d02833680eebb9a.png)


3. 自己写的加解密,自己的密钥
	<kbd>F5</kbd> 后看到很多循环语句,循环里面有很多异或操作,位移等运算操作

> 密钥的选择: 比较能够唯一识别 如 MAC地址 GetTickCount 网卡信息...


密码体系
明文 ----- 加密的密钥 ----- 密文 : 对称密钥体系
明文 ----- 公钥 -- 私钥 --  密文  : 非对称密钥体系


## OD 基础
[metasploit-framework](https://github.com/rapid7/metasploit-framework)
[shellcode](https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x86/src/block/block_api.asm)

hash算法搜索获得api函数地址的实现
+ [文章1](https://www.cnblogs.com/bokernb/p/6407484.html)
+ [文章2](https://bbs.pediy.com/thread-86216.htm)

如何判断恶意样本中是否采用 hash 算法搜索获得api函数地址的方式进行系统API的调用?
有很多以**立即数** 为基础来做一些循环和偏移.







因为一般是拿 指针,寄存器来操作 很少有以立即数为基础来做一些循环和偏移

明确我们的使用目的:
> 在恶意样本分析中,我们使用od通常都是用来补充一些详细信息或者是寻找一些特殊的东西

### 动态看得到的有哪些?
堆栈具体的值

### 基本使用

结合 IDA 

+ 地址的问题
00401093 <font color=red>一般来说直接对应IDA地址和OD地址的后四位就行</font>
	+ 如果是 **0040** 开头的话,就直接看后面四位
	+ 如果不是 **0040** 开头,比如 0041 那就用前四位加一即可 (**0034**0000 + 10000) 
> 在 win7 里面 IDA 的地址完全对应 OD 里面的地址


![Snipaste_20220420_173906.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/bb2a1720808adee7f917545636168a34.png)
	

![Snipaste_20220420_180439.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/df631d59359bd664a0dac33e250246af.png)


+ **下断点**

	+ 使用快捷键 <kbd>F2</kbd> ( 如果成功设下断点, OD 地址处的颜色会变红)
	+ 或右键对应指令处选择 断点 --> 切换 进行设置普通断点,

+ 运行到断点处
	+ 使用快捷键 <kbd>F4</kbd> ( 如果成功运行到断点处, OD地址处的颜色会变灰)
	+ 或右键选择 断点 --> 运行到指定位置

+ 指令执行方式
	+ 单步步入: 快捷键 <kbd>F7</kbd>
<font color=green>使用场景: 运行的汇编代码中有 `call` 如果想看 `call` 的函数的具体代码,就使用 <kbd>F7</kbd></font>
	+ 单步步过: 快捷键 <kbd>F8</kbd>
<font color=green>使用场景: 运行的汇编代码中没有 `call` 或者你不想看函数的中间过程,就使用 <kbd>F8</kbd></font>
	+ 自动步过: 快捷键 <kbd>Ctrl</kbd> + <kbd>F8</kbd>
<font color=green>使用场景: 循环语句,经常和 <kbd>F12</kbd> (暂停) 一起使用 </font>

快速找到内存中的值

![Snipaste_20220421_014532.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3915d0f6483ea0321d2e7f316cd74de0.png)

## promon 和 procexp 等工具的使用

1. 本地
样本在目标环境下做的行为

环境监视工具:
1. 针对单一对象的监视
2. 针对整个操作系统的监视


使用方式
1. 先打开工具并设置号
2. 然后启动恶意样本
3. 观察

如果是dll
1. 使用 denpendencywalker 找到导出函数
2. 执行 cmd 命令
```cmd
rundll32.exe dll的名称,导出函数的名字

```

### procexp的使用
[procexp download link](https://docs.microsoft.com/en-us/sysinternals/downloads/process-explorer)

![Snipaste_20220421_025218.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7c0575e86c445c2b1129e9542f9f7e8b.png)



<font color=red>%temp%  这个是缓存文件夹,如果某个应用释放了 PE 结构的东西在这里,那么就要格外注意该应用</font>



![Snipaste_20220421_122508.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0d806801d72f6460daafc9ec681c85a9.png)



![Snipaste_20220421_122902.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8b42cb9e7f95009285f004498df32084.png)

> 该功能在日常生活中可以用来<font color=red>查杀一些恶意捆绑,弹窗软件</font>


主要用这个工具就是观察 dll 和 句柄 的使用

进程镂空/傀儡进程

### promon

[procmon download link](https://docs.microsoft.com/en-us/sysinternals/downloads/procmon)

![Snipaste_20220421_130457.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c7a85b70ef2ce614500fe9ff940931f9.png)


**<font color=red>注册表相关的知识</font>**

![Snipaste_20220421_141812.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f8683ad3b7f5d80980abaf7a2201cae8.png)

打开
regopenkey

查询
query
在恶意样本分析中存在的场景:
1. 获得操作系统信息 ( 语言,时区...)
2. RNG随机数 ( 一般与加解密有关 )
3. 获得反沙盒,反病毒信息
4. set 设置之后再来使用这个键值

设置
set
1. 用户操作
2. 开机启动 
> 在恶意样本中,几乎 90% 的设置操作都跟上面两种行为相关 

`计算机\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run`

![Snipaste_20220421_150723.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fb446cdcc9090aade6a6d9f464dd7bf5.png)

文件相关
场景:
1. 勒索形式的,基本上就是对文件的修改
最重要的特征就是在 write 之前会循环遍历盘符或者大量文件 (在write之前会看到大量的 read 或者 query)
2. 释放其他功能模块文件
3. 开机启动 (开机启动目录)
4. 文件修改 -- 举例 (修改host文件,通过修改文件来修改计算机环境)

进程和线程相关:
恶意代码分析中,涉及到进程和线程的操作的场景:
释放功能模块 (就有可能是 shellcode 或者是 pe)
如果存在进程镂空或者傀儡进程,这个恶意样本会创建一个其他程序的 (非dll的) 名字的地址的线程

释放: 本来是一个 exe 结果变成多个 exe `loadResourceA()`
提前知道了有创建线程这样一个操作,那么就要有上面释放这个过程的心理准备


### Wireshark 等工具的使用
如果识别不出来网卡
1. 卸载 npcap 和 wincap 还有 wireshark
2. 下载一个 [npcap](https://npcap.com/)
3. 先安装 npcap 再重新安装 wireshark
4. cmd 开启 npcap 服务
```cmd
net start npcap
```
5. 启动 wireshark

网络模拟：
dns: 样本里面有 http 请求而且这个请求是指向一个域名的

场景：
静态分析的时候发现这个请求是经过加密的，然后你又不想手动解密

步骤：
1. 改测试环境的 hosts 文件
2. 添加目标域名到 hosts 文件指向一个你可以使用的 ip 地址
3. 指向的 ip 地址使用一个监听或者嗅探工具


### 威胁情报平台的使用



```cmd
get-filehash filepath
```

