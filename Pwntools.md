# PWNTOOLS 基本使用

![logo.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2532f6edb5383bf7fa5c8c997b6e39ed.png)





**现有一程序如下:**

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

![20220525_0104.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/82adb7a0cd260b8467c600a2b02c5141.png)

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

![20220525_0108.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/ab126c6bfbbabd967444fbd1b4409754.png)

> 这时候你就会问,为什么不直接输入来获得 Shell 而要使用 编写 Python 脚本这种方式来获得 Shell？

其实在我们写 PWN 题,或者真实环境中往往并没有一个友好的交互界面给我们,往往只提供给我们一个开放的端口,接口... **所以我们需要使用 pwntools 来简化对该开放的端口进行交互所需要编写的代码**,也就是发送数据和接收数据.


如以下程序,我们很明显无法通过交互式方式获得shell (90s 内完成 1000 道算数题目)

```c
#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

void handler(int signum) {
  puts("Timeout");
  _exit(1);
}

int main() {
  setvbuf(stdout, 0, _IOLBF, 0);
  setvbuf(stdin, 0, _IOLBF, 0);
  signal(SIGALRM, handler);
  alarm(90);

  unsigned seed = (unsigned)time(NULL);
  srand(seed);

  unsigned int magic;
  printf("Give me the magic number :)\n");
  read(0, &magic, 4);
  if (magic != 3735928559) {
    printf("Bye~\n");
    exit(0);
  }

  printf("Complete 1000 math questions in 90 seconds!!!\n");
  for (int i = 0; i < 1000; ++i) {
    int a = random() % 65535;
    int b = random() % 65535;
    int c = random() % 3;
    int ans;
    switch (c) {
    case 0:
      printf("%d + %d = ?", a, b);
      scanf("%d", &ans);
      if (ans != a + b) {
        printf("Bye Bye~\n");
        exit(0);
      }
      break;
    case 1:
      printf("%d - %d = ?", a, b);
      scanf("%d", &ans);
      if (ans != a - b) {
        printf("Bye Bye~\n");
        exit(0);
      }
      break;
    case 2:
      printf("%d * %d = ?", a, b);
      scanf("%d", &ans);
      if (ans != a * b) {
        printf("Bye Bye~\n");
        exit(0);
      }
      break;
    }
  }
  printf("Good job!\n");
  system("sh");

  return 0;
}
```

而我们使用 pwntools 就能很容易实现,我们先通过`recvuntil` 来接收掉程序的提示输出,没被接收掉的数据会被输出到屏幕上,如下图

![20220525_1042.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4033518fc3b271c97590b5f125dad0c0.png)

分析该程序发现该程序一开始需要我们输入一个 magic number 然后判断我们输入的是否与 3735928559 相同, 我们发现这一长串数字,而程序只能接收 4 个字节数据,所以我们尝试对该串数据转换成 16 进制数据为 `0xdeadbeef` 我们将 `0xdeadbeef` 通过 `send()` 函数将数据发送给程序 发现出现了以下输出:
![20220525_1047.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/83d763c929b4fc58822bb1491ae75fe6.png)

我们可以通过接收数据发送数据的方式解决这 1000 个题目后: 我们成功获得shell

![20220525_1059.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/d23e55c51c129b0804cd742bef7aca76.png)

```python
from pwn import *

if __name__ == '__main__':
    proc = process(b'./pwntools')
    proc.recvuntil(b'number :)\n')
    payload = p32(0xdeadbeef)
    proc.send(payload)
    proc.recvline()
    for i in range(1000):
        res = proc.recvuntil(b' = ?').replace(b' = ?', b'')
        log.info(res)
        ans = eval(res)
        proc.sendline(str(ans))

    proc.interactive()
```

---


## `pwnlib.tubes`

pwntools 所有跟数据交互相关的 API 都在 存放在 `pwnlib.tubes` 这个模块里


<font color="DimGray" face=Monaco size=3> 你可能会有这个疑问，我们上面那个脚本代码并不是使用 `from pwnlib.tubes import process` 类似这种的代码. 而是直接一行 `from pwn import *` 就能使用所有的 API 了. 那是因为 pwntools 为简化导入过程,将常用的 API 都放到 pwn 这个模块里了,当然还有向上兼容的成分因素在里面. </font>


+ [pwnlib.tubes 英文文档](http://docs.pwntools.com/en/latest/tubes.html)
+ [pwnlib.tubes 中文文档](https://pwntools-docs-zh.readthedocs.io/zh_CN/dev/tubes.html)



在本地运行一个进程,如果没传可执行文件的路径,默认会运行本地存在的命令
```python
# p = process("./demo")
p = process("python2")
```
我们甚至还可以运行 `ls` 等命令,使用`recv()` 系列函数同样获得了我们想要的输出效果

![20220525_1121.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e6a92cd84e1b06b5078405139ccd31e2.png)

向运行的进程发送信息

```python
p.sendline(b"print 'Hello world'")
p.sendline(b"print 'Wow, such data'");
```

因为这个进程的发送数据流并没有断开，所以我们并不能接收到该进程返回结果数据流,所以我们运行下面代码将返回 `True`

```python
b'' == p.recv(timeout=0.01)
# True
```
我们可以将程序的接收数据流关闭 这个操作相当于将操作系统中 stdin 的标准流关闭
```python
p.shutdown('send')
p.proc.stdin.closed
# True 
p.connected('send')
# False
```
发现成功关闭程序的接收数据流


![20220525_0205.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/dc5864a7d093e7390101a71b3d829342.png)
这时候我们就可以使用 `recv` 系列的函数对程序的返回结果进行接收


+ `recvline()` : 接收一行数据相当于 `recvuntil('\n')`
	+ 接收到返回值 `Hello world\n`
+ `recvuntil()` : 一直接收数据直到数据内容与函数内字符串相匹配时则停止
	+ 如下面我们接收到 `Wow,`

+ `recvregex()` : 使用正则表达式的方式接收相应数据
+ `recv()` : 接收所有返回数据流


![20220525_0209.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/3d00561c8cdb37509f6eb9d597309b3b.png)



