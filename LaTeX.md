## 学习使用 LaTeX
[Arch Wiki 官方手册](https://wiki.archlinux.org/title/TeX_Live#Installation) 

修复 tlmgr 的bug
```bash
# 将下面这段加入到自己.bashrc/.zshrc 等终端初始化文件中

alias tlmgr='TEXMFDIST/scripts/texlive/tlmgr.pl --usermode'
# Arch 默认为 : /usr/share/texmf-dist
alias tlmgr='/usr/share/texmf-dist/scripts/texlive/tlmgr.pl --usermode'

```

并修改 `tlmgr.pl` 文件
将 `$Master = "$Master/../..";` 替换成 `$Master = "${Master}/../../..";`



```bash
# 添加阿里云镜像
tlmgr option repository https://mirrors.aliyun.com/CTAN/systems/texlive/tlnet

```

```bash
tlmgr install ctex
```

[LaTex 介绍文档](https://github.com/CTeX-org/lshort-zh-cn) 

中括号内填写编码格式,花括号里面填写文章的类型

+ `artical` 代表普通文章类型
+ `book` 代表书籍类型
+ `report` 代表报告类型
+ `beamer` 代表幻灯片类型



```tex
\documentclass[UTF8]{artical}
\documentclass[UTF8]{book}
\documentclass[UTF8]{report}
\documentclass[UTF8]{beamer}
```

我们可以使用 `\maketitle` 来将上面定义好的标题给显示出来

```tex
\documentclass[UTF8]{article}
\title{First glance of LaTex}
\author{ZhouHaoBusy}
\date{2022.6.26}

\begin{document}
\maketitle
this is my first \LaTeX() page,
hope it can help you to study \LaTeX()
   
\end{document}
```

**可以中文和英文混用的格式**
```tex
\documentclass[UTF8]{ctexart}
```
> 新产生一个段落需要两个换行符来实现,一个换行符只会生成一个空格


+ 设置粗体为 `\textbf{}`
	+ `bf` 为 `bold font` 的缩写
+ 设置斜体为 `\textit{}`
	+ `it` 为 `italic` 的缩写
+ 设置下划线为 `\underline{}`


```tex
\textbf{}
\textit{}
\underline{}
```


开启一个新的章节 花括号内代表章节名字

```tex
\section{}
\subsection{}
\subsubsection{}

```

如果是书籍排版等需要生成比 section 更大的排版我们可以使用 `\chapter{}` 通常来表示书籍的第几章

```tex
\chapter{}
```

比`\chapter{}` 还要的的还有 `\part{}` 通常来表示书籍中的第几部分

如果我们需要在文档中添加图片我们需要引入 `graphicx` 包 然后使用 `\includegraphics{}`花括号内填入图片名称 可以省略掉后面的 png 扩展名


```tex
\usepackage{graphicx}
\includegraphics{head}
```

`textwidth` 代表当前文本区域的宽度

```tex
\includegraphics[width=0.5\textwidth]{head}

```

如果我们需要给图片添加一个标题

我们可以先将图片嵌套在一个 `figure` 环境(标签)中

+ 使用 `\caption` 来设置图片标题
+ 使用 `\centering`来将图片居中显示

```tex
\begin{figure}
\centering
\includegraphics[width=0.5\textwidth]{head}
\caption{This is a simple title}
\end{figure}
```

列表
要使用列表我们需要先切换到列表的环境
`environment` 
> `environment` 是 LaTeX 中的一个专用术语,它就像编程语言里面的作用域


任何介于 `\begin{}` 和 `\end{}` 之间的内容都属于同一环境,位于同一环境中的内容将会共享相同的文字格式

对于无序列表的创建我们可以使用 `itemize` 环境
列表中的每个元素都需要以 `\item` 开头

对于有序列表(也就是前面带编号的列表) 我们则可以使用 `enumerate` 环境 与无序列表相同，列表中的元素同样需要以 `\item` 开头


数学公式

行内公式需要写在两个美元符号之间 `$...$`

如这段代码`$E=mc^2$` 将会生成爱因斯坦的质能方程
$E=mc^2$


如果我们希望将公式写在单独的一行我们则可以使用 `equation` 这个环境

`equation` 这个环境我们可以简写成 `\[E=mc^2\]`

对于复杂的公式我们需要单独记忆这些表达式

如 `\over` 代表几分之几

```tex
\begin{equation}
d={k \varphi(n)+1} \over e
\end{equation}
```

[在线 LaTeX 公式编辑器](https://latex.codecogs.com/eqneditor/editor.php) 

表格
我们可以使用 tabular 环境在当前位置创建一个表格

+ `c` 代表 `centering` 居中
+ `l` 代表 `left` 向左对齐
+ `r` 代表 `right` 向右对齐



```tex
\begin{tabular}{c c c}
Cell1 & Cell2 & Cell3 \\
Cell4 & Cell5 & Cell6 \\
Cell7 & Cell8 & Cell9
\end{tabular}
```
我们可以使用 `\hline` 来添加横线 在上面 `tabular` 后面那个花括号添加`|` 来添加竖线 并还可以通过 `p{2cm}` 来指定单列长度 `p` 代表 `paragraph`是一种允许设置列宽的列格式



```tex
\begin{document}
\begin{tabular}{|p{2cm}|c|c|}
\hline \hline
Cell1 & Cell2 & Cell3 \\
\hline
Cell4 & Cell5 & Cell6 \\
\hline
Cell7 & Cell8 & Cell9 \\
\hline
\end{tabular}
\end{document}
```

如果我们需要给表格添加一个标题
我们可以先将整个表格放在一个 `table` 环境里随后我们可以通过 `\caption{}` 命令指定表格的标题并通过 `\center` 






