> 靶机环境介绍
+ [Fawkes](https://download.vulnhub.com/harrypotter/Fawkes.ova) 
+ 难度等级 <font color=red>难</font>

目标:
+ 取得 root 权限 +  3个Flag

**所用技术栈**
+ 主机发现
+ 端口扫描
+ WEB 信息收集
+ **FTP 服务攻击**
+ 缓冲区溢出
+ 模糊测试
+ 漏洞利用代码编写
+ 流量转包分析
+ 堆溢出漏洞攻击
+ Metasploit (MSF)
+ 手动修复 EXP 代码
+ 本地提权

## 主机发现与端口扫描

主机发现

```bash
sudo arp-scan -l
```


```bash
sudo nmap -p21,22,80,2222,9898 -sV -sC 10.0.2.16
```