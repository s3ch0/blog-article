# Flask

## 虚拟环境



+ `flask` 轻量级
+ `tornado` 解决`c10k`问题

+ `django` 重量级


### 创建虚拟环境

> 输入命令: <font face=Consolas>virtualenv</font> 环境名

如果有多个python版本,可以通过命令: <font face=Consolas color=red>virtualenv -p (Python路径) 环境名</font> 来创建虚拟环境

进入环境下的`Scripts`文件夹下输入命令执行脚本:  <font face=consolas color=red>activate</font>

然后就可以在虚拟环境下使用`pip` 安装各种包了

### 退出虚拟环境

> 输入命令: <font face=Consolas>deactivate</font> 环境名

### 管理虚拟环境

虚拟环境还可以通过一些工具来管理,从而使用起来更加方便,这里推荐使用 <font face=consolas>virtualenvwrapper</font>

> 输入命令: <font face=Consolas> pip install virtualenvwrapper-win (Windows版)</font> 下载 <font face=Consolas>virtualenvwrapper</font>

安装完之后还需在`~/.bashrc` `(~/.zshrc)`添加以下配置 如果使用

```sh
# virtualenvwrapper 的配置
export WORKON_HOME=$HOME/myenv  # 指定虚拟环境的路径
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3 # 指定Python解释器的路径
source /home/zhouhao/.local/bin/virtualenvwrapper.sh # 指定安装后virtualenvwrapper的路径
# 一般来说会在python site-packages 上一目录下的bin目录里
```

**常用命令**

创建虚拟环境 : `mkvirtualenv`

**进入虚拟环境: `workon` 环境名**

退出虚拟环境: `deactivate`

删除虚拟环境: `rmvirtualenv` 环境名

列出虚拟环境: `lsvirtualenv`

 进入到虚拟环境目录: `cdvirtualenv` 环境名

## Flask基础

### Flask项目结构

项目名:

+ `static` : 存放静态资源
+ `templates` : 存放模板
+ `app.py` : 管理运行和启动

**`web`项目**

*`mvc`*模式:

+ `model`  模型
+ `view`  视图
+ `controler`  控制器

*`mtv`*模式:

+ 

