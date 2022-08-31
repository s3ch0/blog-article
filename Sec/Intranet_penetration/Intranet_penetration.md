# 内网渗透


![whatisahackerwhatishackingfeatured.webp](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/daa3cb19c0ad9848edd12b2c11191c1e.webp)

> 目标
1. 设定行动
2. 红队侦查
3. 确认活动范围


> 设定行动

在红队任务开始,我们需要对于我们的行动进行明确的规划

1. 网络侦查 
	+ (网络资产收集 , 供应链收集,等)
2. 情报收集
	+ (企业组织架构,业务信息,人员信息,历史攻击事件,内部通讯方式,等)
3. 基础建设
	+ (匿名线路,流量混淆,免杀Beacon,免杀WEBSHELL,扫描机,等)
4. 目标线路
	+ (拟出获取目标路径所有路线 [路线周期], 初步评估,确认战术)

> 红队侦查
1. 撕口子 (权限入口点)
2. 持久性 (权限维持分析)
3. 企业内部网络分析 (拓扑图) [tools: BloodHound]
4. 确定所处区域,内网范围,安全设备,所用杀软
5. 机器信息收集 (业务,用途,管理来源地址,时间,关系梳理)
6. 横向路径规划


> 确认活动范围
+ 通过红队侦查,明确活动范围,减少流量,和暴露行为,如何做到像蓝队一样行动
+ 业务段,DMZ区域,运维段,办公段,开发人员,等做好踩点

**例子:**
内部gitlab
+ 用户登入记录 ( IP地址 )
+ 浏览器指纹
+ XSS探针获取更多信息
+ 人员信息 (java组,PHP组,等)
+ 业务DB地址,业务服务器地址
 
## 域内信息收集

手机本机信息
在红队任务开始时,不论外网还是内网渗透,信息收集都是非常关键的一步,对内网每一台的机器,其所处内网的结构是什么,其角色是什么,使用这台机器的人的角色是什么,以及这台机器上安装了什么杀毒软件,这台机器是通过什么方式上网的,这台机器是笔记本,还是台式机器等问题,都需要通过信息收集


1. 手动信息收集

<font color=red>本机信息包括操作系统,权限,内网IP地址段,杀毒软件,端口,服务,补丁更新频率,网络连接 (可能会有类似 IP-Guard 这种监视软件),共享,会话等.</font>如果是域内主机,操作系统,应用软件,补丁,服务,杀毒软件

> 通过本机相关的信息收集,可以进一步了解整个域的操作系统版本,软件及补丁安装情况,用户命令方式

+ 查询网络配置信息
```cmd
ipconfig /all
ipconfig /displaydns
```
+ 查询操作系统及软件的信息
```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
rem 中文操作系统
systeminfo | findstr /B /C:"OS 名称" /C:"OS 版本"

rem 操作系统架构
echo %PROCESSOR_ARCHITECTURE%
wmic product get name,version
wmic process get name,executablepath,processid

```

+ 查看本机服务信息
```cmd
wmic service list brief
```

+ 查询最近操作,查看,打开过的文件
按 <kbd>Win</kbd> + <kbd>R</kbd> 后输入 `recent` 即可


+ 查询进程列表
```cmd
tasklist
rem 别的主机
tasklist /S 1127.0.0.1 /u username /p passwd
```

+ 查看启动程序信息

```cmd
wmic startup get command,caption
```

+ 查看计划任务

```cmd
schtasks /query /fo LIST /v
rem at 命令在win10已经禁用,现在使用 schtasks 命令
```

+ 查看主机开机时间

```cmd
net statistics workstation
```

+ 查询用户列表
 
```cmd
net user
rem 隐藏用户看不见
net user zh$ 123.com@ /add
net user zh$ :: 加上名字可以查看
```


+ 查看端口列表
```cmd
netstat -ano
```




![Snipaste_20220419_214911.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b38d1fad7e5658371f3c185b77801731.png)

+ 查看补丁列表

```cmd
systeminfo
wmic qfe get Caption,Description,HotFixID,InstalledOn
```
+ 查看本机共享列表

```cmd
net share
rem net use \\127.0.0.1\c$
wmic share get name,path,status
```
+ 查询路由表及所有可用接口的ARP缓存表

```cmd
route print
rem tracert www.baidu.com 跟踪路由
arp -a
```
+ 查看代理配置情况
```cmd
reg query "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Internet Settings"
```

查询当前权限
```cmd
whoami
rem 查看当前用户的权限
whoami /priv

net user 用户名
```
在获取一台主机权限后,有如下三种情况
1. 本地普通用户
2. 本地管理员用户
3. 域内用户

获取SID 
```cmd
whoami /all
```

> 除了SYSTEM权限,WINDOWS还有什么高权限?

Windows 7以上系统，除了SYSTEM以外，还有一个TrustedInstaller系统底层管理员账户。Windows7及以上系统中默认的管理权限最高的TrustedInstaller管理权限默认状态是未被激活的

```cmd
rem 查询域内zhouhaobusy用户
net user zhouhaobusy /domain 

```

## 判断是否存在域
1. 使用 `ipconfig` 命令
使用 `ipconfig /all` 可以查看网关IP地址,DNS的IP地址,域名,本机是否和DNS服务器出域同一网段等信息
`nslookup zhouhaobusy.org`
通过反向解析查询命令nslookup来解析域名的IP地址.用解析得到的IP地址进行对比,判断域控制器和DNS服务器是否在同一台服务器上

2. 查看系统详细信息
```cmd
systeminfo
```
3. 查询当前登入域及登入用户信息
```cmd
net config workstation
```
4. 判断主域
```cmd
rem 执行下面命令如果报错,则不在域环境内
net time /domain
```
执行命令后会有三种情况
存在域,但当前用户不是域用户,会出现"发生系统错误,拒绝访问"
存在域,且当前用户是域用户,会成功执行命令
不存在域时,会有如下报错:
![Snipaste_20220419_223137.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d2f7f5f85ee1de4b102d9a566ddc9daa.png)

## 探测域内存活主机

1. 利用 NetBIOS 快速探测内网
NetBIOS 是局域网程序使用的一种应用程序编程接口 (API) 为程序提供了请求低级别服务的统一命令集,为局域网提供了网络及其他特殊功能.几乎所有局域网都是在 NetBIOS 协议的基础上工作的. NetBIOS 也是计算机的标示名,主要用于局域网中计算机的互相访问.工作流程为正常的机器名解析查询应答过程.

**可利用工具 `nbtscan` 探测**

[nbtscan 下载地址](http://www.unixwiz.net/tools/nbtscan.html#download)

2. 利用 ICMP 协议快速探测内网
```cmd
for /L %i in (1,1,254) DO @ping -w 1 -n 1 192.168.1.%i | findstr "TTL="

for /L %i in (1,1,255) do @ping -a 192.0.%i.1 -w 1 -n 1 | find /i "Ping"
```

3. 通过 ARP 扫描探测内网
```cmd
arpscan
```
4. 通过常规 TCP/UDP 端口扫描探测内网
5. 扫描域内端口
6. 自动信息收集



## 域分析工具 BloodHound


### BloodHound 介绍


### BloodHound 安装



### BloodHound 使用


### BloodHound 分析



