

# Study Docker


![KMWVWF1SBN9FY.svg](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8b7acbecfcab2ebd57f503493b04be0d.svg)

## 安装Docker

>  环境查看

```bash
# 使用uname查看系统
┌──(root Arch)-[/]
└─# uname -r
5.11.11-arch1-1

# 查看系统的版本等信息
┌──(root Arch)-[/]
└─# cat /etc/os-release 
NAME="Arch Linux"
PRETTY_NAME="Arch Linux"
ID=arch
BUILD_ID=rolling
ANSI_COLOR="38;2;23;147;209"
HOME_URL="https://www.archlinux.org/"
DOCUMENTATION_URL="https://wiki.archlinux.org/"
SUPPORT_URL="https://bbs.archlinux.org/"
BUG_REPORT_URL="https://bugs.archlinux.org/"
LOGO=archlinux

```

>  安装

帮助文档

![Snipaste_20210331_111740.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/085f503938568d81ec4788f55367aa9b.png)

### kali里安装Docker

```bash
# 卸载 
sudo apt-get remove docker docker-engine docker.io
# 安装Docker
sudo apt-get install docker-ce

# kali 安装Docker
# 切换清华镜像
curl -fsSL https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/gpg | sudo apt-key add -
# 配置docker apt 
echo 'deb https://mirrors.tuna.tsinghua.edu.cn/docker-ce/linux/debian/ buster stable' | sudo tee /etc/apt/sources.list.d/docker.list
# 安装
sudo apt-get install docker-ce
```

权限管理
[官方操作文档](https://docs.docker.com/engine/install/linux-postinstall/) 

```bash


```
创建 docker 组
```bash
sudo groupadd docker
```
添加主机用户给 docker 组
```bash
sudo usermod -aG docker $USER
```
Log out and log back in so that your group membership is re-evaluated.

If testing on a virtual machine, it may be necessary to restart the virtual machine for changes to take effect.

On a desktop Linux environment such as X Windows, log out of your session completely and then log back in.

On Linux, you can also run the following command to activate the changes to groups:

 newgrp docker 
Verify that you can run docker commands without sudo.

docker run hello-world
This command downloads a test image and runs it in a container. When the container runs, it prints a message and exits.

If you initially ran Docker CLI commands using sudo before adding your user to the docker group, you may see the following error, which indicates that your ~/.docker/ directory was created with incorrect permissions due to the sudo commands.

WARNING: Error loading config file: /home/user/.docker/config.json -
stat /home/user/.docker/config.json: permission denied
To fix this problem, either remove the ~/.docker/ directory (it is recreated automatically, but any custom settings are lost), or change its ownership and permissions using the following commands:

```bash
sudo chown "$USER":"$USER" /home/"$USER"/.docker -R
sudo chmod g+rwx "$HOME/.docker" -R
```
[关于 docker.sock 问题的解决方法](https://newbedev.com/got-permission-denied-while-trying-to-connect-to-the-docker-daemon-socket-at-unix-var-run-docker-sock-get-http-2fvar-2frun-2fdocker-sock-v1-24-images-json-dial-unix-var-run-docker-sock-connect-permission-denied-code-example) 




## Docker的常用命令

### 帮助命令

``` bash
docker version		# 显示docker的版本信息
docker info			# 显示docker的系统信息,包括docker的镜像和容器的数量
docker 命令 --help   # 常用
```
Docker的官方文档: [https://docs.docker.com/](https://docs.docker.com/)

![Snipaste_20210330_182612.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/b2c39b4e25dd84413883abd28a7bc487.png)

### 镜像命令

>  docker images 查看所有本地的主机镜像

```bash
┌──(root Arch)-[/home/zhouhao]
└─# docker images
REPOSITORY                        TAG       IMAGE ID       CREATED         SIZE
tomcat                            latest    0ce438e89a29   2 days ago      667MB
nginx                             latest    b8cf2cbeabb9   3 days ago      133MB

# 解释
REPOSITORY 镜像的仓库源
TAG        镜像的标签
IMAGE ID   镜像的ID
CREATED    镜像的创建时间
SIZE	   镜像的大小

# 可选项
Options:
  -a, --all    #列出所有镜像 
  Show all images (default hides intermediate images)
  
  -q, --quiet  #只显示镜像ID
  Only show image IDs
  
```

>  docker search 搜索镜像

```bash
┌──(root Arch)-[/home/zhouhao]
└─ # docker search mysql
NAME                              DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
mysql                             MySQL is a widely used, open-source relation…   10676     [OK]       
mariadb                           MariaDB Server is a high performing open sou…   4010      [OK]       
# 可选项, 通过搜索来过滤
--filter=STARS=3000 # 搜索出STARS大于3000的镜像

```

>  docker pull 下载镜像

```bash
# 下载镜像 docker pull 镜像名:tag  (tag为版本号)
# 不指定版本号默认是下载最新版本的镜像
┌──(root Arch)-[/home/zhouhao]
└─# docker pull centos                                                           
Using default tag: latest # 如果不写tag 默认是lastest
latest: Pulling from library/centos
7a0437f04f83: Pull complete  # 分层下载
Digest: sha256:5528e8b1b1719d34604c87e11dcd1c0a20bedf  # 签名
Status: Downloaded newer image for centos:latest
docker.io/library/centos:latest # 真实地址

docker pull centos  # 等价于 docker pull docker.io/library/centos:latest

# 指定版本下载
```



### 容器命令

```bash
docker start 容器ID #启动容器
docker attach 容器id #进入容器
删除全部容器： docker rm $(docker ps -aq)
docker image rm -f 镜像ID # 删除对应ID的镜像
需要注意删除镜像和容器的命令不一样。
# docker rmi ID  ,其中 容器(rm)  和 镜像(rmi)

```

### 其他重要命令

#### 1. 容器保存为镜像

+ 我们可以通过以下命令将容器保存为镜像

```bash
docker commit ubuntu pwn
# ubuntu是容器名称
# pwn是新的镜像名称
```

#### 2. 镜像的导出导入

有时我们需要将一台电脑上的镜像复制到另一台电脑上使用，除了可以借助仓库外，还可以直接将镜像保存成一个文件，再拷贝到另一台电脑上导入使用。

1. 使用export 和 import命令

   ```bash
   # 导出镜像
   # 使用docker export 命令根据容器 ID 将镜像导出成一个文件。
   
   docker export f299f501774c > pwn.tar
   
   # 导入镜像
   # 使用 docker import 命令则可将这个镜像文件导入进来。
   docker import  pwn.tar pwn.t
   ```

   

```shell

# 保存镜像
# 下面使用 docker save 命令根据 ID 将镜像保存成一个文件。
docker save 0fdf2b4c26d3 > pwn.tar

（2）我们还可以同时将多个 image 打包成一个文件，比如下面将镜像库中的 tomcat 和 centos 打包：
docker save -o images.tar tomcat:9.6 centos:3.4

# 载入镜像
使用 docker load 命令则可将这个镜像文件载入进来。

docker load <  .tar

# 两种方案的差别
特别注意：两种方法不可混用。
如果使用 import 导入 save 产生的文件，虽然导入不提示错误，但是启动容器时会提示失败，会出现类似"docker: Error response from daemon: Container command not found or does not exist"的错误。

# 1，文件大小不同
export 导出的镜像文件体积小于 save 保存的镜像

# 2，是否可以对镜像重命名
docker import 可以为镜像指定新名称
docker load 不能对载入的镜像重命名

# 3，是否可以同时将多个镜像打包到一个文件中
docker export 不支持
docker save 支持

# 4，是否包含镜像历史
export 导出（import 导入）是根据容器拿到的镜像，再导入时会丢失镜像所有的历史记录和元数据信息（即仅保存容器当时的快照状态），所以无法进行回滚操作。
而 save 保存（load 加载）的镜像，没有丢失镜像的历史，可以回滚到之前的层（layer）。

# 5，应用场景不同
docker export 的应用场景：主要用来制作基础镜像，比如我们从一个 ubuntu 镜像启动一个容器，然后安装一些软件和进行一些设置后，使用 docker export 保存为一个基础镜像。然后，把这个镜像分发给其他人使用，比如作为基础的开发环境。
docker save 的应用场景：如果我们的应用是使用 docker-compose.yml 编排的多个镜像组合，但我们要部署的客户服务器并不能连外网。这时就可以使用 docker save 将用到的镜像打个包，然后拷贝到客户服务器上使用 docker load 载入。

```







## 容器数据卷

### 什么是数据卷

如果数据都在容器中，那我们把容器删除，数据就会丢失 需求:数据可以持久化

比如我们有一个MySQL数据库，如果把容器删除了，相当有删库跑路！需求：MySQL数据可以存储在本地！

<font color=red>容器之间可以有一个数据共享的技术！Docker容器中产生的数据，同步到本地！</font>

这就是卷技术！目录挂载，将我们容器内的目录，挂载到Linux上面！

---

总结一句话： 容器的持久化和同步操作！容器间也是可以数据共享的！

### 使用数据卷

> 方式一：直接使用命令挂载 -v

```bash
docker run -it -v 主机目录:容器目录

# 测试
[zhouhao@Arch] sudo docker run -it -v /home/Docker:/home ubuntu /bin/bash

# 容器启动后我们可以使用 docker inspect 容器ID -->查看信息

```

### 实战：安装MySQL

思考：MySQL数据持久化的问题

```bash

# 运行容器，需要做数据挂载
# 安装MySQL，需要配置密码，！！
# 官方测试：
docker run --name some-mysql -e MYSQL_ROOT_PASSWORD=my-secret-pw -d mysql:tag
# 运行
-d 后台运行
-p 端口映射
-v 卷挂载
-e 环境配置 [MYSQL_ROOT_PASSWORD : 为设置MySQL的密码]
--name 容器名字
# docker run -d -p 3310:3306 -v /home/mysql/conf:/etc/mysql/conf.d -v /home/mysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123.com --name mysql_01 mysql

# 测试连接数据库
mysql -h127.0.0.1 -uroot -p123.com -P3310
```



### 具名和匿名挂载

```bash
#匿名挂载
-v 容器内路径
-P 随机指定端口映射
docker run -d -P --name nginx_01 -v /etc/nginx nginx

docker volume --help #查看关于docker卷的命令

#查看所以volume的情况
docker volume ls
local   4aa455fa5eef0bcba61b28ac8963661f88f35396a8b7ef37bbfa08abfb8a8f88
# 这种就是匿名挂载 我们发现这种挂载我们在-v后面只接了容器内路径，没有写容器外路径

# 具名挂载
┌──(root💔kali)-[~]
└─# docker run -d -P --name pwn -v work-space:/usr/local docker_pwn:18.04
06792438d549dc6145c498170987d445790f2251ff684a6d1068ab441abf0c27
┌──(root💔kali)-[~]
└─# docker volume ls
DRIVER    VOLUME NAME
local     work-space
# 通过 -v 卷名:容器路径
# docker volume ls 查看卷

┌──(root💔kali)-[~]
└─# docker volume inspect work-space 
[
    {
        "CreatedAt": "2021-05-23T00:51:13-04:00",
        "Driver": "local",
        "Labels": null,
        "Mountpoint": "/var/lib/docker/volumes/work-space/_data",
        "Name": "work-space",
        "Options": null,
        "Scope": "local"
    }
]

```

![Docker01.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/6a1b41b069fa569f13c14ca2b14c8493.png)


拓展:

```bash
# 通过 -v 容器内路径,ro rw 来改变读写权限
ro readonly  # 只读
rw readwrite # 可读可写
# 一旦设置了容器权限,容器对我们挂载出来的内容就有限定了!
docker run -d -P --name pwn -v work-space:/usr/local:ro docker_pwn:18.04
docker run -d -P --name pwn -v work-space:/usr/local:rw docker_pwn:18.04
# ro 只要看到ro就说明这个路径只能通过宿主机来操作,容器内部是无法操作
```



### 初识Dockerfile

Docckerfile 就是用来构建 docker 镜像的构建文件 (命令脚本)

通过这个脚本可以生成镜像,镜像是一层一层的

```python
# 创建一个dockerfile文件, 名字可以随机 建议Dockerfile
# 文件中的内容 指令(大写)  参数
FROM centos
VOLUME ["volume01","volume02"]
CMD echo "----end----"
CMD /bin/bash
# 这里的每一个命令,就是镜像的一层


```



![Docker02.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/a9151af13b1f68578718fe59c21408b8.png)

### 数据卷容器

![Docker03.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4dd8e8517d2f4d8c5fc054ea2f51faf9.png)

> 快捷键 <kbd>Ctrl+P+Q</kbd> --> 不关闭地退出当前容器

```bash
# 启动三个容器 (使用刚刚用Dockerfile生成的镜像)
# 启动第一个容器
docker run -it --name docker01 zhouhao/centos:1.0
```

![Docker04.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5ca9ea247374ed57eea080810585603d.png)

```bash
# 启动第二个容器
docker run -it --name docker02 --volumes-from docker01 zhouhao/centos:1.0
```











1. 容器保存为镜像

我们可以通过以下命令将容器保存为镜像
```bash
docker commit pinyougou_nginx mynginx

# pinyougou_nginx是容器名称
# mynginx是新的镜像名称
```

## Dockerfile

### Dockerfile介绍

> Dockerfile 用来构建docker镜像的文件! --> *命令参数脚本*

构建步骤:

1. 编写一个dockerfile文件
2. dockerbuild 构建成为一个镜像
3. docker run 运行镜像
4. docker push 发布 (DockerHub , 阿里云镜像仓库)

官方的做法:


![Docker06.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c4e4b00a09b0d7ae508dad4d97657ed2.png)

>  很多官方镜像都是基础包,好多功能和命令都没有.所以我们可以使用 DockerFile 来自己搭建自己的镜像

### Dockerfile的搭建过程

**基础知识:**

1. 每个保留关键字(指令)都必须是大写字母
2. 执行从上到下执行
3. \# 号表示注释
4. 每一个指令都会创建提交一个新的镜像层,并提交. 



![Docker07.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/209bc6ce023584ede0c122b37dba1dc0.png)

DockerFile是面向开发的，我们以后要发布项目，做镜像都需要编写dockerfile文件，这个文件十分简单！
Docker 镜像逐渐成为企业交付的标准，必须要掌握！

---

**步骤**：开发，部署，运维...缺一不可

1. DockerFile：构建文件，定义了一切的步骤，源代码

2. DockerImage：通过DockerFile 构建生成的镜像，最终发布和运行的产品，原来是jar war

3. Docker容器：容器就是镜像运行起来提供服务的.

### Dockerfile的指令

```bash
FROM          # 基础镜像，一切从这里开始构建
MAINTAINER    # 镜像是谁写的，姓名+邮箱
RUN           # 镜像构建的时候需要运行的命令
ADD           # 步骤：tomcat镜像，这个tomcat压缩包！添加内容
WORKDIR       # 镜像的工作目录
VOLUME        # 挂载目录
EXPOSE        # 保留端口配置
CMD           # 指定这个容器启动的时候要运行的命令 ，只有最后一个会生效，可被替代
ENTRYPOINT    # 指定这个容器启动的时候要运行的命令，可以追加命令
ONBUILD       # 当构建一个被继承 DockerFile 这个时候就会运行 ONBUILD 的指令，出发指令。
COPY          # 类似ADD，将我们的文件拷贝到镜像中。但是COPY不会自动解压
ENV           # 构建的时候设置环境变量
```

### 实战测试

---

Docker Hub 中 99%镜像都是从这个基础镜像过来的 FROM scratch 



![Docker09.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/5d71bb24f3b876c8ac1565ff3e6ce082.png)

> 创建一个自己的 Centos

```shell
# 1. 编写Dockerfile的文件
FROM centos
MAINTAINER zhouhao<zhouhaobusy@163.com>

ENV MYPATH /usr/local
WORKDIR $MYPATH
RUN yum -y install vim
RUN yum -y install net-tools

EXPOSE 80
CMD echo $MYPATH
CMD echo"------end------"
CMD /bin/bash

# 2. 通过这个文件构建镜像
docker build -f dockerfile的路径 -t 镜像名:[tag]

```

![Docker10.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/29de5a4ea73fa0321d8e8411d9f9a5a8.png)





![Docker11.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/87b9033560162174c82329b7967dfbe6.png)



我们可以使用 docker history 来列出本地进行的变更历史

![Docker12.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/8e442d9cdad6ed830cfb69ff9c7a9aca.png)






![Docker08.webp](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/448a454e80cb4b0ff2a8bb0258d2406f.webp)

## Docker网络

### Docker0

```bash
# Docker容器带来的网卡,都是成对存在的
# evth-pair 就是一对的虚拟设备接口,他们都是成对出现的,一段连着协议,一段彼此相连
# 正因为有这个特性,evth-pair 充当一个桥梁,连接各个虚拟网络设备的
# OpenStac , Docker容器之间的连接 , OVS的连接,都是使用 evth-pair 技术
```

>  原理

1. 我们每启动一个Docker容器,Docker就会给Docker容器分配一个ip,我们只要安装了Docker,默认会自带有一个网卡Docker0 (桥接模式) 使用的技术是 evth-pair技术!



Docker 中的所有网络接口都是虚拟的 , (虚拟的转发效率高)

Docker 使用的是Linux的桥接 , 宿主机中是一个Docker容器的网桥 Docker0



### link

```bash
docker run -d -p --name tomcat03 --link tomcat02 tomcat
# 使用--link 连通tomcat03 和 tomcat02 的网络
# 使用--link 后可以tomcat3可以直接通过容器名来访问
# --link 本质其实就是在hosts配置中增加了一个映射 172.18.0.3 tomcat02 312857784cd4
# 但我们现在不推荐使用 --link
```

Docker0的问题: 他不支持容器名连接访问

### 自定义网络

查看所有的Docker网络

```
docker network ls
```



```shell
docker network create --driver bridge --subnet 192.168.0.0/16 --gateway 192.168.0.1 mynet  # 自定义网络
```



*连通网络*

```bash
docker network connect mynet tomcat01
# 连通tomcat01
# 一个容器 
```


