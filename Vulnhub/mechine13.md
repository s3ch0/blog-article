> 靶机环境介绍
+ [doubletrouble]() 
+ 难度等级 <font color=yellow> 中</font>

目标:
+ 取得两台靶机 root 权限

**所用技术栈**
+ 主机发现
+ 端口扫描
+ WEB 信息收集
+ 开源 CMS 漏洞利用
+ 隐写术
+ 密码爆破
+ GTFOBins 提权
+ SQL 盲注
+ 脏牛提权

## 主机发现与端口扫描

主机发现

```bash
sudo arp-scan -l
```

