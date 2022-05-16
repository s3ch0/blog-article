设置 git commit 的编辑器为vim

或者运行命令 git config –global core.editor vi 修改更加方便。
如添加vi
git config core.editor vi

4、git commit –amend

修改最后一次commit的信息。

分为两种情况，未推送到远程仓库和已推送到远程仓库。

情况一：已 commit 未 push
已经执行 commit，但还没有 push，要想更改 commit 信息（修改最近一次提交）。

git commit --amend
执行上述命令后，进入注释页面进行修改，修改后保存退出。

然后使用 git log --pretty=oneline 查看内容，可以发现已经成功修改了。

需要注意的是此项命令会修改提交时的 commit-id，即会覆盖原本的提交，需要谨慎操作。

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
