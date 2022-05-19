
# `Git`

版本控制 `(VCS)`
> 版本控制系统 ( version control system ) -- 简称 VCS

+ [A Visual Git Reference](https://marklodato.github.io/visual-git-guide/index-en.html) : Git的学习网站
+ [Learning Git Branching](https://learngitbranching.js.org/)  
+ [Visualizing Git Concepts with D3](https://onlywei.github.io/explain-git-with-d3/): *网页版Git(方便你熟悉Git命令)*

1. 初始化 `Git` 仓库 ( 将文件夹初始化为`Git`仓库 )

```bash
git init # 执行完这条命令之后会在当前目录生成一个.git的文件
```

我们可以通过 `.gitignore` 这个文件来指定忽略的文件(不进行版本控制)

 `.gitignore` 里面的内容大致为这种类型:

```bash
# ! 代表否定 * 代表所有 
*
!*/
!*.c
!*.h
```

## Git 的一些基本命令

```bash
git init                  # 将文件夹初始化为Git仓库
git branch <name>         # 创建分支
git stash				  # 将当前目录拉入缓存
```

## Git暂存区命令

```bash
git add <file>             # 将工作区的指定文件放入暂存区
# git add .                # 将当前目录下的所有文件加入缓冲区
git status                 # 查看工作区和暂存区的状态
git checkout -- <filename> # 将暂存区的文件恢复到工作区
# git checkout -- .        # 将暂存区的文件,全部恢复到工作区
```

## Git提交相关命令

```bash
git commit -m '提交原因'    # 将缓存区的内容添加到仓库
git log                    # 查看提交日志 (历史提交记录)    
git reset --hard HEAD^     # 回到上一个版本
git reset --hard HEAD^^    # 回到上两个个版本(可接多个)
git reset --hard <ID>      # 回到指定的版本
# 删文件
git rm 你的文件
# 删目录
git rm -r 你的目录 # r: recursive 递归
git reflog #( 查看历史和未来版本(可以查看'未来'的版本)
```

**第一次将文件添加到仓库需要一般执行:**

```bash
git config --global user.email "zhouhaobusy@gmail.com" # 设置您的邮箱
git config --global user.name "name"  # 设置你使用版本控制时使用的名字
```

## Git服务器相关命令

```bash
git clone 你的仓库地址(url)  # 将远程仓库克隆到本地
git push # 将本地代码推到服务器(将工作成果同步到服务器) 
git pull # 同步远程仓库(将服务器更新同步到本地)
```

常用的国内代码托管平台

1. 码云 https://gitee.com
2. coding https://coding.net/


## 实际场景命令

设置 git commit 的编辑器为vim
1. 在 `.git/config/` 文件中 `[core]` 内添加 `editor=vim`

2. 运行命令 git config –global core.editor vi 修改更加方便,如添加vi

```bash
git config core.editor vi
```

### 修改最后一次commit的信息。

```bash
git commit –amend
```

修改最后一次commit的信息。

<font color="red" face=Monaco size=3> 分为两种情况，未推送到远程仓库和已推送到远程仓库。 </font>

情况一：已 commit 未 push
已经执行 commit，但还没有 push，要想更改 commit 信息（修改最近一次提交）。

```bash
git commit --amend
```
执行上述命令后，进入注释页面进行修改，修改后保存退出。

然后使用 `git log --pretty=oneline` 查看内容，可以发现已经成功修改了。

需要注意的是此项命令会修改提交时的 `commit-id`，即会覆盖原本的提交，需要谨慎操作。

---

情况二：已 commit 已 push
已经执行 commit，且已经 push 的提交（修改最近一次提交）。

```bash
git commit --amend
```
执行上述命令后，进入注释页面进行修改，修改后保存退出。

然后执行强制推送命令：


```bash
git push --force-with-lease origin master
```

