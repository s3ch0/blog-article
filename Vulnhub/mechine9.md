> 靶机环境介绍
+ [Vikings](https://download.vulnhub.com/vikings/Vikings.ova) 
+ 难度等级 <font color=green>低 - 中</font>

目标:
取得 root 权限 + 2 Flag


**所用技术栈**
+ 主机发现
+ 端口扫描
+ WEB 信息收集
+ 编码转化/文件还原
+ 离线密码破解
+ 隐写术
+ 二进制文件提取
+ 素数查找/科拉茨猜想
+ RPC 漏洞提取


## 主机发现与端口扫描

```bash
sudo arp-scan -l
```

```bash
sudo nmap -p- 10.0.2.12
```

```bash
sudo nmap -p22,80 -sV -sC 10.0.2.12
```


当我们打开这个站点时，发现网站的响应速度及其缓慢，所以我就查看了一下网站源码，来弄清楚，到底为什么访问这个站点时，会这么慢。
