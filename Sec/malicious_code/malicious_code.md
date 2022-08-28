
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

+ [virustotal](https://www.virustotal.com/gui/)
+ [censys](https://search.censys.io/)
+ [triage](https://tria.ge/)

```cmd
get-filehash filepath
```

## 针对PE结构的恶意代码的应急响应

流程:

1. 取证
2. 分析
3. 处理
4. 报告



注意事项

时间优先,程序合规,要素全面,不要多操作

我们要先保存被攻击服务器的内存状态,

+ [dumpit](https://dumpit.soft32.com/)
+ [volalility](https://www.volatilityfoundation.org/26)

### 取证

**当前状态**

要素:

进程

网络

文件

用户

性能

注册表 [regshot](https://sourceforge.net/projects/regshot/)

服务 : 如果一个服务伪装成微软官方的服务,但是没有描述信息这个时候就应该注意了

宏观 : 公司被感染的面积,或者说受影响的面积/比例,这部分被感染的主机主要负责公司里面什么业务,主要是感染哪一部分

注意事项:

及时记录

记录全面

关系理清



过去状态

要素

日志 日志文件 `.evtx` 事件查看器

第三方产品

内容:

时间

地点:所处文件夹

人物

行为



注意事项

时间线很重要,不同地方的痕迹以时间的关系列出来



分析

分析到信息一定要和我们取证中的要素一一对应



3. 处理

如果利用我们分析到的信息做处理

进程相关:

找到根进程并结束,如果存在重复启动则需要进一步分析样本中是否对其他进程做操作,

该进程句柄,dll..是否挂在别的进程,驱动..上如果确实存在,则找到该文件存在路径删除,再进行相关操作.

网络相关:

1. 识别到的恶意网络流量以 **特征字符** 的识别去拦截
2. 关闭正在产生流量的端口和相关进程和服务
3. 将目的地址和端口加入黑名单中

文件相关

**以分析到的信息为准** 删除文件,如果存在删除文件或者替换

**在客户允许的前提下** 尽可能使用覆写删除的方式



用户相关

以分析到的信息为准对用户做相关操作

涉及到用户的所有操作 **必须** 对客户提前说明并尽可能要求客户提供事件前的用户列表



注册表相关

以分析到的信息为准对注册表做操作



服务相关

以分析到的信息为准对服务做操作

漏洞相关

如果样本中存在漏洞利用则需要修复相应漏洞并提前测试

如果存在未知漏洞利用,则需要进一步记录并向相关机构厂商提供相关信息

专杀相关

如果需要提供专杀工具则需要想客户说明工具授权,如果是开源工具则需要说明开源协议

4. 报告

取证中的要素和分析中的信息需要一一对应

取证,分析,处理的全过程**必须一一截图**,并且处理完成之后的状态也要有记录

样本的全流程要有 `att&ck` 的表

注意自己的法律风险并标注号相关信息

编译时间,编译工具,ttps,ios尽可能写出来,并尽可能判断出攻击关联

## 针对PE 结构的恶意代码的防护提示措施

思路

所有防护措施以业务为最高优先级,在结合自己的安全策略,对当前样本中涉及到的关键点做补充

常见的关键点

1. 权限与逻辑
2. 业务与攻击面
3. 数据与传输
4. 意识与管理

关键点的收集

1. 钓鱼过程
   1. 钓鱼的话术与场景设置:
      + 文化的熟悉程度
      + 具体的信息熟悉程度
   2. 钓鱼的渠道:
      + 具体产品的薄弱点
   3. 被钓鱼的意识
      + 管理结构
      + 权限结构
      + 安全意识培训

入侵过程

1. 入侵的面积
   + 先确定机器 --> 再确定机器所属安全范围 --> 再确定机器所属的业务范围 --> 再确定漏洞的所在点
   + 攻击面与彼那样产品的布置
2. 入侵的点
   + 产品的更新与检查
3. 入侵的路径
   + 内部产品的布置与网络结构的调整

时间与空间

1. 与同行沟通共享信息并获得攻击上的行业规律
2. 域名和网络流量分析攻击来源并获得攻击上的地区
3. 时间点分析攻击频率和时间节点并在威胁情报中收集规律
4. 将收集到的攻击规律与业务相结合优化自己的安全策略
5. 将收集到的攻击规律结合威胁情报优化自己的威胁情报收集系统



##  常见pe结构的恶意代码加壳

常见类型

加壳的实际意义:

>  防止别人了解源代码的运行逻辑.(主要是防止对可执行程序进行静态代码分析)

1. 普通壳 : 壳代码执行一些普通的功能,如压缩..
2. 加密壳: 执行解密功能
3. 指令壳: 把汇编运用的逻辑重新编写.

如 `xor eax,eax` 的含义是将两个 `eax` 寄存器进行与或运算

那么我们可以使用别的汇编指令达到相同的目的.

区别:

都是可代码的区别

加壳过程

[解决错误](https://stackoverflow.com/questions/21834833/argument-of-type-const-char-is-incompatible-with-parameter-of-type-lpcwstr)

工具加壳

**oep**

```bash
msfvenom -K -X
backdoorfactory
```

upx



手工加壳



oep



先找到想操作的入口点







[donut](https://github.com/TheWover/donut)
