> 靶机环境介绍
+ [y0usef](https://www.vulnhub.com/y0usef/y0usef.ova) 
+ 难度等级 <font color=green>低</font>

目标:
取得 root 权限 + 2 Flag


**所用技术栈**
+ 主机发现
+ 端口扫描
+ WEB 信息收集
+ 指纹探测
+ **403 Bypass**
+ 文件上传
+ 提权



## 主机发现与端口扫描

```bash
sudo arp-scan -l
```
![](./mechine8.assets/2022-07-01_18-26.png)


发现可疑主机 `10.0.2.9`

然后我们对可疑主机进行全端口扫描

```bash
sudo nmap -p- 10.0.2.9
```

![](./mechine8.assets/2022-07-01_18-27.png)
发现其开放 22 端口 和 80 端口
然后对端口进行应用版本的发现

![](./mechine8.assets/2022-07-01_18-32.png)

```bash
sudo nmap -p22,80 -sV -sC 10.0.2.9
```
我们安装惯例还是对该服务器的80端口开放的web服务进行访问

![](./mechine8.assets/2022-07-01_18-34.png)

然后试着查看一下该页面的源码,看看是否能有什么有价值的信息 
<font color="red" face=Monaco size=3> 如 有价值提示的注释信息，调用后端 API 接口的信息, 页面内隐藏的可以提交数据的注入点. </font>

查看网站页面源码的快捷键为:<kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> U </kbd>&ensp; 

![](./mechine8.assets/2022-07-01_18-36.png)

## 网站信息收集

刚刚我们试着查看了一下该靶机 80端口 的网页,并没有发现什么有价值的信息

这时候我们就要对该网站进行全方位的信息收集

我们试着使用一些工具来扫描并发现目标服务器一些软件的技术栈，网站架构组成的一些信息

```bash
whatweb http://10.0.2.9
```

![](./mechine8.assets/2022-07-01_18-49.png)

我们还需要对隐藏目录，隐藏页面进行扫描

```bash
dirsearch -u http://10.0.2.9
```

![](./mechine8.assets/2022-07-01_18-57_1.png)


发现了大量的403 响应的页面

![](./mechine8.assets/2022-07-01_19-20.png)
我们知道 403 响应码为拒绝用户访问
所以我们可以猜测目标主机上可能真实存在这些页面，但是由于我们的权限不够导致我们访问失败.

我们还发现一个特殊的重定向页面

![](./mechine8.assets/2022-07-01_18-57.png)

我们尝试一下访问该页面，发现访问失败

![](./mechine8.assets/2022-07-01_19-24.png)

为进一步确认我们是因为没有权限导致的，我们可以按 <kbd class="keybord"> F12 </kbd>&ensp; 打开开发者选项卡，查看我们请求该页面时，服务器给我们的响应码,发现确实是 403 响应码。

所以网站的建设者大概率是有做一些身份认证和权限限制方面的设置的，而 `adminstration` 这个目录也是有很大概率真实存在在目标服务器上的

> 虽然说网站开发者对网站进行了权限设置,但一般在未做安全方面测试的网站上权限划分和授权方面往往都或多或少存在一些相关漏洞或者薄弱性的。



## 403 Bypass

<font color="red" face=Monaco size=3> 针对所有服务器给我们返回403的场景，我们基本上都要做以下测试： </font>
1. 使用旁站的手段，看看能不能尝试绕过目标服务器403 权限的限制
2. 


### 使用旁站的方式

如果请求方式如下
```bash
# Request
  Get /auth/login HTTP/1.1
  Host : www.zhouhaobusy.com
# Response
  HTTP/1.1 403 Forbidden
```
如果网站开发者只针对 Host 头部为 `www.zhouhaobusy.com` 这样的请求做了权限的限制，造成了403访问被拒绝的结果

这时候我们就可以猜测如果说目标系统的建设者只针对这一个主机域名进行权限限制的话，当我们使用这个域里的其它主机名来访问同样URL的时候，目标服务器是否会给我们返回 200 OK 这样的响应码呢?


我们可以使用如下方式

```bash

# Request
  Get /auth/login HTTP/1.1
  Host : [xxx].zhouhaobusy.com
# Response
  HTTP/1.1 200 OK

```


![](./mechine8.assets/2022-07-01_19-26.png)

![](./mechine8.assets/2022-07-01_19-40.png)
