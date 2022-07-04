## Docker 容器的使用与简单操作

debconf: delaying package configuration, since apt-utils is not installed

问题描述
运行Dockerfile制作镜像过程中，出现如题一行红色字体。

基础镜像是Ubuntu:latest

解决方案
是说apt-utils 没有安装，对结果并没有什么危害，知识影响交互式安装。

这个apt-utils 可以实现在安装过程中交互式配置文件，可以通过：

RUN apt-get install --assume-yes apt-utils
1
忽略掉这个警告信息。


Reference
[warning] debconf: delaying package configuration
出现 debconf: delaying package configuration, since apt-utils is not installed


