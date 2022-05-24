# PWNTOOLS 基本使用
![logo.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2532f6edb5383bf7fa5c8c997b6e39ed.png)

![20220525_0104.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/82adb7a0cd260b8467c600a2b02c5141.png)

![20220525_0108.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ab126c6bfbbabd967444fbd1b4409754.png)

![20220525_0205.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dc5864a7d093e7390101a71b3d829342.png)

![20220525_0209.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3d00561c8cdb37509f6eb9d597309b3b.png)

+ [ ] <font color="red" face=Monaco size=3> PWNTOOLS 是用来干嘛的？ </font>



现有一程序如下:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
  puts("Please enter your name:");
  char name[20];
  scanf("%s", name);
  int flag = strcmp(name, "Hacker");
  if (flag == 0) {
    puts("Hello, Hacker!");
    system("/bin/bash");
  } else {
    puts("Sorry!");
  }
}
```

分析可知,我们只需要输入 `Hacker` 回车后就能获得一个 bash shell

我们当然可以手动输入来实现,但如果我们想通过 Python 程序的方式来实现上面的操作，我们需要怎么操作呢？

**这个时候我们使用 PWNTOOLS 就能很轻松地解决上面那个问题**

我们只需要运行下面这段代码即可

```python
from pwn import *

if __name__ == '__main__':
    my_process = process(b"./hello_pwn")
    my_process.recvuntil(b"Please enter your name:")
    my_process.sendline(b"Hacker")
    my_process.interactive()
```

> 这时候你就会问,为什么不直接输入来获得 Shell 而要使用 编写 Python 脚本这种方式来获得 Shell？

其实在我们写 PWN 题,或者真实环境中往往并没有一个友好的交互界面给我们,往往只提供给我们一个开放的端口,接口... **所以我们需要使用 pwntools 来简化对该开放的端口进行交互所需要编写的代码**,也就是发送数据和接收数据.



---

## 数据交互相关

pwntools 所有跟数据交互相关的 API 都在 存放在 `pwnlib.tubes` 这个模块里


你可能会有这个疑问，我们上面那个脚本代码并不是使用 `from pwnlib.tubes import process` 类似这种的代码. 而是直接一行 `from pwn import *` 就能使用所有的 API 了. 那是因为 pwntools 为简化导入过程,将常用的 API 都放到 pwn 这个模块里了,当然还有向上兼容的成分因素在里面.

+ [pwnlib.tubes 英文文档](http://docs.pwntools.com/en/latest/tubes.html)
+ [pwnlib.tubes 中文文档](https://pwntools-docs-zh.readthedocs.io/zh_CN/dev/tubes.html)

```python
```

