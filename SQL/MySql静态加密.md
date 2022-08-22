## 主密钥在MySQL中的应用

> MySQL支持静态数据加密。
[主密钥知乎](https://zhuanlan.zhihu.com/p/34712401) 
+ <font color="red" face=Monaco size=3>  使用主密钥进行静态数据加密的目的是为了防止保存在磁盘上的文件被非法盗用 </font>

+ 使用该功能可以确保数据库的表空间，日志等文件即使是被盗用，也无法读取里面的敏感数据。


InnoDB通过两层密钥架构实现静态数据加密功能。

当表空间文件进行加密时， <font color="green" face=Monaco size=3> 会产生一个加密的表空间密钥，该密钥保存在表空间文件的文件头.</font> 当应用程序或者合法用户对表进行访问时，InnoDB会使用一个主密钥将加密的表空间密钥解密。主密钥可以进行轮换，表空间密钥无法更改，除非对表空间重新进行加密。


<font color="red" face=Monaco size=4> 下面将使用 最新 `Docker MySQL::last` 版本来进行操作演示   </font>

<div style='border-radius:15px;display:block;background-color:#a8dadc;border:2px solid #aaa;margin:15px;padding:10px;'>
 由于有一些伙伴可能没用过 Docker，所以下面列举了这次实验可能需要用到的 Docker 命令</div>

### 环境搭建

运行一下命令如果提示我们权限不够，那么我们可以使用 `sudo` 来运行以下命令
+ [How to run docker without sudo](https://github.com/sindresorhus/guides/blob/main/docker-without-sudo.md)

**使用 Docker 安装 mysql**
```bash
sudo docker pull mysql
```
**1. 开启mysql**


```bash
docker run -d --name mysql-test -p 3306:3306 -v /home/Docker:/home -e MYSQL_ROOT_PASSWORD=123.com mysql
```
> 参数相关解释

+ `-d` : <font color='red' face=Monaco size=3>让容器在后台运行</font>，并且不回显日志输出
+ `--name mysql-test`
  + 给我们的容器起个名字叫 （mysql-test），方便我们后续启动，进入,关闭容器
+ `-p 3306:3306` 
  + 映射主机与 Docker 容器的端口 `3306`
+ `-v /home/Docker:/home`
  + <font color='red' face=Monaco size=3>将主机的 `/home/Docker` 与 Docker 容器内的 `/home` 路径同步</font> 
+ `MYSQL_ROOT_PASSWORD=123.com`
  + 设置 mysql 服务初始密码为 `123.com`

当我们运行完上面的这条命令，我们就能在后台启动 Mysql 这个容器了,当然我们还要进入到容器内，所以我们可以在启动容器的时候就加一个 `-it` 最后面接 `bash` 来**启动容器并进入到容器**,如下：

![alt](./MySql%E9%9D%99%E6%80%81%E5%8A%A0%E5%AF%86.assets/2022-08-22_01-08.png)
**2. 进入容器**

```bash
docker exec -it mysql-test bash
```
![alt](./MySql%E9%9D%99%E6%80%81%E5%8A%A0%E5%AF%86.assets/2022-08-22_01-17.png)

**3. 查看容器ID**

```bash
sudo docker ps -a
```

**4. 重启容器**

```bash
sudo docker restart 6f8991a7baf3 # container ID
```

在我们

**更新系统源**
```bash
deb http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster main non-free contrib
deb http://mirrors.aliyun.com/debian-security buster/updates main
deb-src http://mirrors.aliyun.com/debian-security buster/updates main
deb http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-updates main non-free contrib
deb http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
deb-src http://mirrors.aliyun.com/debian/ buster-backports main non-free contrib
```


**添加vim基本配置**
```vim
syntax on
noremap L $
noremap H 0
noremap J 5j
noremap K 5k
inoremap jk <ESC>
noremap ; :
```
**安装 `keyring_file` 插件来开启该功能**

在 `/etc/mysql/my.cnf` 中添加以下内容

```bash
early-plugin-load=keyring_file.so
keyring_file_data=/data/3306/mysql-keyring/keyring
```

```bash
mkdir -p /data/3306/mysql-keyring
chown -R mysql.mysql /data/3306/mysql-keyring
chmod 750 /data/3306/mysql-keyring
```

```sql
INSTALL PLUGIN keyring_file soname 'keyring_file.so';
```
```sql
-- 查看 keyring 插件信息

select * from information_Schema.plugins where plugin_name like '%keyring%'\G

-- 查看插件状态

SELECT PLUGIN_NAME, PLUGIN_STATUS FROM INFORMATION_SCHEMA.PLUGINS WHERE PLUGIN_NAME LIKE 'keyring%';

```

这些UDF用于管理密钥，举个例子看一下，使用kering_key_generate来生成一个密钥，然后再通过keyring_key_fetch查看一下密钥：

```sql
INSTALL PLUGIN keyring_udf SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_generate RETURNS INTEGER
  SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_fetch RETURNS STRING
  SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_length_fetch RETURNS INTEGER
  SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_type_fetch RETURNS STRING
  SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_store RETURNS INTEGER
  SONAME 'keyring_udf.so';
CREATE FUNCTION keyring_key_remove RETURNS INTEGER
  SONAME 'keyring_udf.so';

```


卸载相关插件
```sql
UNINSTALL PLUGIN keyring_udf;
DROP FUNCTION keyring_key_generate;
DROP FUNCTION keyring_key_fetch;
DROP FUNCTION keyring_key_length_fetch;
DROP FUNCTION keyring_key_type_fetch;
DROP FUNCTION keyring_key_store;
DROP FUNCTION keyring_key_remove;
```
---

```sql
-- 创建数据库
create database test;
use test;
-- 创建表
create table test(id int unsigned auto_increment primary key ,username varchar(50),text varchar(100));

-- 查看test表的字段
show columns from test;

insert into test(username,text) values("zhouhaobusy","Busy To live Or Busy To Die,Busy To live Or Busy To Die");

```

数据已经写入表中了，这时我还没有启用keyring插件的主密钥功能, <font color="red" face=Monaco size=3> 让我们看看表空间文件里能否查到我这条记录： </font> 

执行`hexdump -C test.idb | less` 可以查看并 <font color="green" face=Monaco size=3>  检索表空间文件里是否包含刚才插入的字符 </font> 

**默认路径： `/var/lib/mysql/`**

```sql
-- 生成密钥
select keyring_key_generate("MySecKey","DSA",256);

-- 查看密钥
select HEX(keyring_key_fetch("MySecKey"));

-- 对表进行加密
alter table test.test encryption='y';

```

查看所安装的插件

```sql
show plugins
```



插入第二条值

```sql
insert into test(username,text) values("Hacker","The Second One Text");

```



---

## 日志加密

接下来演示一下redo日志的加密。让我们先看一下redo日志里面的内容。

`hexdump ./binlog.000002`
没有加密之前，是可以在redo日志里面找到相关记录的。确认一下参数值 <font color="red" face=Monaco size=3> 查找关键字 Busy </font>，开启加密：

文件形式 `iblogfile0`

```sql
-- 查看是否开启 redolog 加密
show global variables like '%innodb_redo_log_encrypt%';

-- 将redolog 加密功能开启

set persist innodb_redo_log_encrypt = ON;

```
再次确认一下redo日志里面的内容，已经无法找到第二条记录


---

## Binlgo 加密
接下来，我们开启binlgo加密，在开启之前，先确认一下日志的加密情况。

```sql
show binary logs;
```
开启加密

```sql
set persist binlog_encryption = 1;
```


## 主密钥轮换
```sql
alter instance rotate innodb master key;

alter instance rotate binlog master key;
```
最后一个环节，让我们看一下如何管理密钥，进行主密钥轮换。

可以通过performance_schema里面的keyring_keys查看当前密钥：内容包括ID，所有者信息。

```sql
select * from performance_schema.keyring_keys;
```
需要注意的是，不要在服务器运行和正在启动时轮换密钥，可能会发生无法读取数据的情况，造成数据丢失事故。

以上内容是对MySQL静态数据加密做的一个简介




