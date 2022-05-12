
# 操作系统学习

![operatingsystemsiconslinuxwindowsandroidmaciosiconsvector.jpg](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/56354a5b6630b31c15d5e9a0133ad33d.jpg)
+ [视频链接](https://space.bilibili.com/202224425/video)
+ [课件链接](http://jyywiki.cn/OS/2022/)
+ [Lab链接](https://nju-projectn.github.io/ics-pa-gitbook/ics2021/PA0.html)

## 操作系统概述





## 操作系统上的程序


## 多处理器编程



## 理解并发程序执行




## 并发控制

### 互斥

### 同步

> 如何在多处理器上协同多个线程完成任务？

+ 典型的同步问题：生产者-消费者；哲学家吃饭
+ 同步的实现方法：信号量、条件变量

**概念: 同步(Synchronization)**

<font color=green>两个或两个以上随时间变化的量在变化过程中保持一定的相对关系</font>

+ iPhone/iCloud 同步 (手机 vs 电脑 vs 云端)
+ 变速箱同步器 (合并快慢速齿轮)
+ 同步电机 (转子与磁场速度一致)
+ 同步电路 (所有触发器在边沿同时触发)

<font color="green" face=Consolas> 异步 (Asynchronous) = 不同步 </font>

上述很多例子都有异步版本 (异步电机、异步电路、异步线程)

并发程序中的同步

并发程序的步调很难保持 “完全一致”

线程同步: <font color="red" face=Monaco size=3> 在某个时间点共同达到互相已知的状态 </font> 




## 真实世界的并发编程



## 并发 BUG 与应对



## 操作系统的状态机模型



## 状态机模型的应用


## 操作系统上的进程


## 进程的地址空间


## 系统调用和 Shell


## C 标准库的实现



## fork的应用


## 什么是可执行文件

## 动态链接和加载


## xv6 代码导读



## Xv6 上下文切换



## 处理器调度



## 操作系统设计

