

<img alt="Gif" src="http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/2313c11438a85401442bd2ef7252959a.gif" width="100%" />


## 环境搭建

### Golang 环境安装
1. [国外官方](https://golang.org/dl)
2. [中国镜像](https://golang.google.cn/dl)
3. [中文网站](https://studygolang.com/dl)




```bash
export GOROOT=/usr/lib/go # GOROOT 表示源码包路径
export GOPATH=/home/zh/Work/Go # GOPATH 开发Go项目的默认路径
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin
```

```bash
go --help
```

```bash
go version
```
1. **<font color="green" face=Monaco size=3> 简单的部署 </font> 方式**
+ 可直接编译成机器码
+ 不依赖其它库
+ 直接运行即可部署


2. **<font color="green" face=Monaco size=3> 静态类型 </font>语言**
+ 编译的时候检查出来隐藏的大多数问题

3. **语言层面的 <font color="green" face=Monaco size=3> 并发 </font>**
+ 天生支持并发
+ 充分的利用多核

4. **强大的标准库**
+ runtime 系统调度机制
+ 高效的 GC 垃圾回收
+ 丰富的标准库

5. **简单易学**
+ 25 个关键字
+ 类似C 语言,内嵌C语法支持
+ 面向对象特征
+ 跨平台



1. 云计算基础设施领域

代表项目：docker、kubernetes、etcd、consul、cloudflare CDN、七牛云存储等。

2. 基础后端软件

代表项目：tidb、influxdb、cockroachdb等。

3. 微服务

代表项目：go-kit、micro、monzo bank的typhon、bilibili等。

4. 互联网基础设施

代表项目：以太坊、hyperledger等。

---

4、Golang的不足

+ 包管理，大部分包都在github上

+ 无泛化类型

+ 所有Excepiton都用Error来处理(比较有争议)。

+ 对C的降级处理，并非无缝，没有C降级到asm那么完美



```bash
go run hello.go
go build hello.go
```

```go

```


golang 中的语句加分号和不加分号都可以，建议是不加


函数的 `{` 一定是和函数名在同一行内的，否则编译错误

```go
import "fmt"
import "time"

import(
	"fmt"
	"time"
)
```
`:=` 只能用在函数体内,全局变量不能使用


```go 
// 声明多个变量
var foo1 , foo2 int = 100,200
var(
  var1 int = 100
  var2 bool = true

)

```
![](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/blog_img/31-init.png)





常量

`iota` 只能配合 `const()` 一起使用


返回值

+ 函数名首字母大写代表该函数对外开放
+ 函数名首字母小写代表该函数不对外开放（私有）


匿名导包方式
在包名前面加个下划线即可，即使没有使用包里的内容，我们还能做该包内相关的的初始化

```go
package main

import (
	_ "init/lib1" // 匿名导包方式
//	mylib2 "init/lib2" // 起别名
	. "init/lib2"  // 静态导入,可直接使用
)

func main() {
	res := lib1.Lib1_str_merge("zhouhao", "COOOL")
	mylib2.Lib2_print(res)

}

```



```go
package main

import "fmt"

func main() {
	defer fmt.Println("main end1")
	defer fmt.Println("main end2")

	fmt.Println("Hello World")

}
```
`defer` 相当与析构函数,而多个 defer 的执行流类似于栈

```go
package main
func main(){
	var myArray1 [10]int
	for i := 0; i<len(myArray1); i++
	{
		fmt.Println(myArray1[i])
	}

}
```
<++>

