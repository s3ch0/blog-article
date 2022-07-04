# Python  Study      

![Python_logo](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python_logo.png)                 
## 基础知识

>  Python默认路径

`C:\Users\86178\AppData\Local\Programs\Python\Python36\`

 <font color=red>可以使用`sys.executable`来获取Python解释器的路径</font>

![Python3](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python3.png)
### **`pip`**

使用pip这个工具 ( *它其实也是一个 `python` 文件* ) 安装的Python库或者包

<u>而使用pip安装的包和库默认路径都在 :</u> <font face=Consolas color=red>Lib --> site-packages</font>

>  一般来说pip下载的源是国外的 (下载速度相对较慢)

**我们可以使用国内的源来进行下载 (命令:)**

`pip install pwntools -i https://mirrors.aliyun.com/pypi/simple/`

<font size=4 color=green>国内的一些镜像源:</font>	

```bash
# pip install 包名 -i 国内源名
清华
# https://pypi.tuna.tsinghua.edu.cn/simple/

中科大
# https://pypi.mirrors.ustc.edu.cn/simple/

阿里云   # (常用)
# https://mirrors.aliyun.com/pypi/simple/

豆瓣
# http://pypi.douban.com/simple/

```

<font color="red" face=Monaco size=3> 如果你那儿的网络总是不给力，又不想每次手动添加，可以加在配置文件里一劳永逸。 </font> 
> Windows：

在 windows 命令提示符（控制台）中，输入 `%APPDATA%`，进入此目录

在该目录下新建名为 pip 的文件夹，然后在其中新建文件 pip.ini。（例如：`"C:\Users\Administrator\AppData\Roaming\pip\pip.ini"`）

在文件中填入一下内容并保存（可替换为上述不同的镜像地址）：

或在 `c:/users/Administrator/pip/pip.ini`

```bash
[global]
index-url = http://pypi.douban.com/simple
[install]
trusted-host=pypi.douban.com
```

> Linux / Mac：

文件地址为 `~/.pip/pip.conf`,其余的差不多都相同




```bash
pip install -U pip                   #   
pip -V 								 # 查看pip的版本信息
pip list 							 # 列出匹配管理的包有哪些
pip install 包名 (pip install redis)  # 安装包
# pip install 包名==版本号            // 安装特定的版本包
pip uninstall 包名                    # 卸载包
pip freeze > requirements.txt        # 将项目依赖的包输出到指定的文档中requirements.txt
# pip install -r requirements.txt 	 # 使用pip安装requirements.txt中依赖的文件
```

```python
syntaxError #语法错误
NnameError  #名字错误
# Python 2 对中文的支持较差 , 如果要在Python 2.x程序中使用中文字符或者中文变量,则需要在Python源程序的第一行增加"#coding:utf-8",当然别忘了将源文件保存为utf-8字符集
```
### 后缀

1. <font color="green" face=Monaco size=3> 以 py 扩展名的文件是 Python 源码文件 </font>，由 python.exe 解释，可在控制台下运行。可用文本编辑器读写。
2. <font color="green" face=Monaco size=3> 以 pyc 为扩展名的是Python的编译文件。 </font>其执行速度快于 py 文件且不能用文本编辑编辑查看。所以 pyc 文件往往代替 py 文件发布。
Python 在执行时，首先会将 py 文件中的源代码编译成 PyCodeObject 写入 pyc 文件，再由虚拟机执行 PyCodeObject。当 Python 执行 import 时会先寻找对应的 pyc或 pyd（dll）文件，如果没有则将对应的py文件编译写入 pyc 文件。 <font color="red" face=Monaco size=3> pyc文件也可以通过 `python -m py_compile src.py` 生成 </font>
3. <font color="green" face=Monaco size=3> pyw 文件与 pyc 文件相似 </font> 但 pyw 执行的时候不会出控制台窗口。开发（纯图形界面程序）时可以暂时把 pyw 改成 py 以调出控制台窗口调试。
4. <font color="green" face=Monaco size=3> pyd 一般是 Python 外的其他语言如 C/C++ 编写的 Python 扩展模块，</font> 即 **Python 的一个动态连接库**，与 dll 文件相当。在Linux系统中一般为.so文件 



### 1.变量

>  所谓的声明变量实际上就是向*内存申请一段空间*

+ 常量 : 固定的值,值不能发生改变
+ 变量 : 里面存放的值随时可以发生改变 

Python是弱类型语言 :声明的变量赋什么值这个变量就是什么类型的.

```python
type(变量名)   # 返回该变量的类型
# 测试python的弱类型
money = 100
print(money, type(money))
money = '100元'
print(money, type(money))
```

![Python1](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python1.png)
代码的规范

*`Programs are meant to be read by humans and only incidentally for computers to execute. -D.E.Knuth`*

<font color=red face=华文仿宋>(程序首先是拿给人读的,其次才是被机器执行)</font>

>  **变量命名规则**

+ 可以以字母,数字,_命名  不能以数字开头
+ 严格区分大小写
+ 不能使用python的关键字命名

**查看python有哪些关键字**

```python
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```
![Python2](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python2.png)

#### **变量命名建议** 

>  pylint 可以检测变量命名的规范性,并测评其建议程度

1. 驼峰式 : `getName` `payMoney` 
   + <u>如果一个名字是由多个单词组成的,则除第一个单词之外以后的每个单词的首字母要大写</u>
   + *类: (GetName) 如果定义类名,每个单词的首字母都要大写*
2. 下划线式 : `pay_money`
   + `Python`中变量的,*函数命名*
   + `get_name` (Python推荐)
3. 无想法时:  `foo`  和 `bar/Fubar`  (`pylint` 极其不推荐使用这两个)
   + `foo` : `fuck up` 的缩写 (直译过来就是 操她娘的:smile:)
   + `bar` :  `beyond all recognition` 的缩写 (大概就是:不知道是个什么玩意的意思)
   + `fubar`: `fucked up beyond all recognition`的缩写  (被搞得面目全非的意思)

#### `globals/locals`
> return the dictionary containing the current scope's global variables.
```python
locals() #字典类型
globals()

```





### 2. print语句的使用

![Python4](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python4.png)

>  我们使用 help(print) 来查看print语句的帮助语句

```python
单词:
# Built-in (builtins)   内置;固有  
-------------------------------
print() # 为Python里的一个内置函数

print(r'Hello\the\dog') # r" raw 原样输出字符串的内容,即使有转义字符也不会转义.
print('HELLO','WORLD','YES')
print('HELLO','WORLD','YES',sep='+')
print('HELLO','WORLD','YES',end='')
print('HeLLO','WORLD','YES',sep='+',end='')
# 含有占位符时不能使用sep和end
'''
输出:
Hello\the\dog
HELLO WORLD YES
HELLO+WORLD+YES
HELLO WORLD YESHeLLO+WORLD+YES

'''

```

<font color=#41b6e6>`print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)`</font>

+ <font color=#ff585d face=楷体>sep 参数用来表示输出时,每个值之间使用哪种字符作为分隔,默认使用空格 作为分隔符</font>
+ <font color=#ff585d face=楷体>end 当执行完一个print语句以后,接下来要输出的字符.默认是换行符.</font>

---

[ 在Python里三引号的作用 ]

+ *保留格式的字符串使用*
+ 作为多行注释使用

![Python5](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python5.png)



### 3. 格式化输出

>  方式

1. 使用占位符
2. <font color="green" face=Monaco size=3> 使用format函数 </font>



1.**使用占位符**

```python
# 在Python里我们可以使用'+'符号对字符串进行拼接  str + int --> error
name = 'zhouhaobusy'
address = 'beijing'
phone = '1234512345'
print("名字是:'+name+'地址是:'+address+'联系方式:'+phone")
# 使用占位符 
print("名字是:%s 地址是:%s 联系方式是:%s" %(name,address,phone)) #输出相同

# 强制转换 # 强制转换中一定要有一个变量(容器)去接收转换后的值
# 
age = 100    # age = str(age) //将int类型转换为字符串类型
age = '100'  # age = 
# int(18.88) ==> 输出:18

------------------------------------------------------------------------

    // 1、%d 为整数占位符，10进制表示，默认有符号，占4字节
   
    // 2、%u 为整数占位符，10进制表示，无符号表示，最高位算作值的一部分
   
#   // 3、%o 为整数占位符，8进制表示

#   // 4、%x 为整数占位符， 16进制表示
   
    // 5、%f为浮点数占位符
  
    // 6、%s为字符串占位符
 
    // 7、%c为字符占位符
    
```

![Python6](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python6.png)


2. **使用format函数**

format函数的说明

```python
------------------------------------------------------------------------
format(self, *args, **kwargs): # known special case of str.format
        """
        S.format(*args, **kwargs) -> str
        
        Return a formatted version of S, using substitutions from args and kwargs.
        The substitutions are identified by braces ('{' and '}').
        """
------------------------------------------------------------------------
```

```python
name = 'zhouhaobusy'
age = 18
grade = 100.5
message = '我的名字叫{},今年年龄是{}岁,成绩是{}分'.format(name, age, grade)
print(message)
------------------------------------------------------------------------
# 也可以使用format格式化位数
print("g({0:.3f}) = {1:.3f}".format(x, y))

```

#### 输出对齐操作

> 占位符式对齐操作

```python
s1 = 'long long long .'
s2 = 'short.'
print ('%-30s%-20s' %(s1,s2)) #'%-30s' 含义是 左对齐，且占用30个字符位 
print ('%-30s%-20s' %(s2,s1))

```

> *`format`函数对齐操作* (常用)

```python
s1 = 'long long long .'
s2 = 'short.'
print ('{:>30}{:>20}' .format(s1,s2)) #{:30d}含义是 右对齐，且占用30个字符位 
print ('{:<30}{:<20}' .format(s1,s2)) #{:<30d}含义是 左对齐，且占用30个字符位 
print ('{:^30}{:^20}' .format(s1,s2)) #{:<30d}含义是 左对齐，且占用30个字符位 

```



```python
str1='1st_format'
str2='2nd_string'
width=30
s_tuple=(str1,str2)
s_list=[str1,str2]
s_dict=dict(str1='1st_format',str2='2nd string')
#30表示总长度30，*表示用*填充不足的部分
print('{:*^30}'.format(str1))  #居中对齐
print('{:*>30}'.format(str1))  #右对齐
print('{:*<30}'.format(str1))  #左对齐
# 按顺序读取各个参数
print('str1:{:>30},str2:{}'.format(str1,str2))
# 按位置读取各个参数
print('str2:{1:>30},str1:{0}'.format(str1,str2))
# 占位宽度以变量形式根据参数位置加入
print('str2:{2:>{1}},str1:{0}'.format(str1,width,str2))
# 占位宽度以变量按顺序加入
print('str1:{:>{}},str2:{}'.format(str1,width,str2))
# 支持元组和列表
print('str2:{1:>30},str1:{0}'.format(*s_tuple))
print('str2:{1:>30},str1:{0}'.format(*s_list))
# 通过字典关键字
print('str2:{str2:>30},str1:{str1}'.format(**s_dict))
# 直接format元组
print('str1,str2:{}'.format(s_tuple))
# 直接format字典
print('s_dict:{}'.format(s_dict))

#在Python3.6中加入了 f-strings 新特性 ：
print(f'str1:{str1},str2:{str2}')

```



### 4. 输入语句的使用

>  input函数 <font color=red>(使用input获取的内容都是字符串型的)</font>



![Python8](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python8.png)

```python
# prompt : 提示,促使,驱使,迅速
# 格式: 变量 = input("提示:") 
```

![Python9](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python9.png)



> 使用`input()` 函数时不管用户传过来的是什么,都会被转换成字符串!

![Python10](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python10.png)

> 有时候我们的输出

```python
#  
from contextlib import redirect_stdout
f = io.StringIO()
with redirect_stdout(f):
	log.info('Busy To Live')
out = f.getvalue()


```



### 5. 运算符

### 类型注释

```python
def test(a: int, b: str) -> str:
    print(a, b)
    return 200


if __name__ == '__main__':
    test('test', 'abc')

```









### 赋值运算符&内存分析



![Python11](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python11.png)



![Python12](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python12.png)



![绘图1](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/绘图1.jpg)

```python
# 扩展后的赋值运算符
+= -= *= /= ....
num = 10
num += 5 # num = num + 5
print(num) # 15

str1 = 'Hello'
str1 += 'World' # 等价于 : str1 = 'Hello' + str1 此时的'+'就是连接符
print(str1) # HelloWorld

```

#### 算数运算符

```



```



![Python14](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python14.png)

#### 关系运算符

```python
# 关系运算符: == != >= <= > < 'is' 'is not'

# is 和 is not 是通过比较内存来返回相应的bool值的


```

![Python15](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python15.png)



#### 逻辑运算符

```python
# and 逻辑与
# or  逻辑或
# not 逻辑非
# 逻辑运算符的运算结果也是返回True False

# 取反 ~

# xor异或运算  ^    相同为0 不同为1
# 左移        <<    m<<n 相当与m乘以2的n次方
# 右移        >>    m>>  相当与m除以2的n次方
```

>  三目运算符

**格式: 结果 if 表达式 else 结果**

```python
# 格式: 表达式 ? 真语句 : 假语句
# 在Python里这种格式并不支持
a = 5
b = 6
result (a+b) if a<b else (b-a)
# 表达式1 : (a+b)
# 判断语句 : a<b
# 表达式2 : (b-a)
# 如果 a<b为真则执行表达式1 若为假则执行第二条语句
'''
判断表达式是true还是False
如果是True则将if前面的内容进行运算,并将结果赋值给result
如果是False则将if后面的内容进行运算,并将结果赋值给result

'''
```

### 运算符的优先级









### 判断语句

#### IF语句

```python
'''
if语句里不接关系运算符 如上面 if username:
 # 判断变量是'' 0 None 默认为False
 # 如果变量有值eg: 'abc' '123'... ,则认为是true
'''
username = ''
if username:
	print("Welcome!")
print("OK!")

'''
if num:
	print('----')
等效于:
if num!=0:
	print('----')
'''

  
```

> 四种结构





```python
# range(n) ---> 0 ~ n-1
# range(m,n) ---> m ~ n-1
# range(m,n,step)
```

### 循环语句

```python
# 如果 for 和 else 同级 


for i in range(4):  # ,从0开始 0 1 2 3

# pass
# break 退出
# while 语句

for i in range(4):
    ....
else:
    print("这里的语句是循环 ")
```







## 字符串

### 基本操作

```python
# 我们可以使用 'in' 和 'not in' 来判断子字符串是否在父字符串里
# 使用''' ''' (三引号) 来格式化字符串
```

![Python16](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python16.png)

#### 字符串的截取

![Python17](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python17.png)

```python
# str[start:end:方向和步长]
	1  表示从左向右
    -1 表示从右往左   
# str = 'Hello World' 
	H   e   l   l   o       W   o   r   l   d
	0   1   2   3   4   5   6   7   8   9   10
   -11 -10 -9  -8  -7  -6  -5  -4  -3  -2   -1                           
# 练习 : Hello World
1. 逆序输出 World
2. 正向输出 Hello
3. 逆序输出 Hello World
4. 打印获取 oll
5. 打印获取 llo Wo
```

![Python18](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python18.png)



### 内建函数

: 声明一个字符串,默认可以调用内建函数 (系统准备好的一些函数)

#### 1. 大小写相关

+ `swapcase()`      # 将字符串中大写转换为小写，小写转换为大写 |
  
+ `capitalize()`      # 将字符串的第一个字符转成大写
+ `title()`             # 将字符串每个单词的首字母转成大写
+ `upper()`         # 将字符串全部转换成大写的表示形式
+ `lower()`          # 将字符串全部转换成小写的表示形式

> 如何函数前面带了 *' is '* 则返回的是布尔类型

```python
# istitle() isupper() islower() 

istitle()  # 判断字符串每个单词的首字母是否为大写
isupper()  # 判断字符串的每个字符是否全部为大写
islower()  # 判断字符串的每个字符是否全部为小写
```

---

*验证码实例*

```python
# 验证码的生成
import random

code = ''
code_pool = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890'
# print(len(code_pool)) # 求字符串的长度 len(str) 返回的是一个整形的数值
for i in range(4):
    code_tmp = random.randint(0, len(code_pool) - 1)  # 0 ~ 61 随机生成一个数字
    code += code_pool[code_tmp]  # 将字符进行拼接
print('您的验证码是: {}'.format(code))
while True:  # 循环
    user_code = input("请输入验证码:")
    if user_code.lower() == code.lower():  # 使用lower()这个内置函数将验证码和用户输入的字符都转换成小写
        print("验证码输入正确")
        break
    else:
        print("对不起,验证码输入错误")
        
```

#### 2. 查找,替换相关

+ `find()`              	   # 返回值为-1则代表没找到 (如果可以找到则返回字母第一次出现的位置)

+ `rfind()`                   # 从右查找

+ <font color=red>`lfind()` </font>            # 从左查找

+ `index()`                   #  与find()方法一样,只不过如果str不在字符串中会报一个异常**(返回索引下标)**
  + `rindex()`    

  + `lindex()`

+ `replace()`                 # 替换  ==`replace(self, old, new, count=None)`==

```python



```

#### <font color=red>3. 编码相关</font>

+ `encode()`		# 编码
+ `decode()`       # 解码

```




```

---



```python
int('1101',2)  # 将1101这个二进制转换成10进制
int('327',8)  # 将327这个八进制转换成10进制
int('f123',16) # 将f123这个16进制转换成1进制


ord('s')  # 将ASCII转换成10进制
chr('64') # 将十进制转换成对应的ASCII码
```





#### 4. 判断相关

+  `startswith()`		        # 判断字符串是否以...开头
+ <font color=red>`endswith()`</font>         #  判断字符串是否以...结尾
+  `isalpha()`                  # 字母判断(字符串里全为字母才返回真)
+  `isdigit()`                   # 数字判断(字符串里全为数字才返回真)

> startswith()  endswith()  返回值都是布尔类型 True False

```python
# 


```

#### 5. 连接与分割

+ join()                 # 以指定字符串作为分隔符,分割字符串 **(将什么加入到什么中)**
+ **split()                # 以 str 为分隔符截取字符串**

```python
# join() : '+'.join('abcd')  将abcd每个字母用'+'连接构成一个新的字符串
new_str = '+'.join('abcd')
print(new_str)

# python里列表 list1 = ['a','b','c','d']
list1 = ['a','b','c','d']
result = '-'.join(list1)
print(type(result))  # 返回的是str类型

# 
s = 'Hello World Ha Ha'
result = s.split(' ')
print(result)  # 返回的是列表类型 ['Hello', 'World', 'Ha', 'Ha']
result = s.split(' ',1)   # ['Hello', 'World Ha Ha']

```



#### 6. 其他

+ **count(args)         # 返回字符串中指定args的个数**
+ strip()               # 去除字符串两侧的空格(也可指定符号)
+ lstrip()              # 去除字符串左侧的空格
+ rstrip()              # 去除字符串右侧的空格 

```python
s = 'Hello World Ha Ha'
str_count = s.count(' ')
print(str_count)  # str_count = 4



# 用户输入字符
c = input("请输入一个字符: ")
 
# 用户输入ASCII码，并将输入的数字转为整型
a = int(input("请输入一个ASCII码: "))
 
 
print( c + " 的ASCII 码为", ord(c))
print( a , " 对应的字符为", chr(a))
```

> 将列表中的值拼接成一个字符串

```python

str = ' '
seq = ['There','is','a','book']
print(str.join(seq))
# There is a book # 输出结果

str = ''
seq = ['There','is','a','book']
print(str.join(seq))
# Thereisabook # 输出结果

```



## <font color=red>列表</font>

1. 列表中可放元素 (所有数据类型)
   + 整形
   + 字符串类型
   + 浮点型
   + 列表
   + 元祖
   + 字典
   + 对象
   
   

> 列表的类型转换

使用  **list( ) ** 这个函数实现强制转换

```python
# 类型转换
str()		# 强制转换为字符型 
int()		# 强制转换为整形

list()		# 强制转换为列表型
# 举例
iterable  可迭代的   # for ... in里面可以循环就是可迭代的

s = 'abcd'
result = list(s)  # ['a','b','c','d']

s = range(1,10,3)
result = list(s)


```

![Python19](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python19.png)

> 列表中可以使用的符号

```python
1. +       # 合并列表
2. *       # [] * num
# 举例
list1 = ['a','b','c']
result = list1 * 3  # result --> ['a','b','c''a','b','c''a','b','c']
3. in      #
4. not in  #
5. is      # 判断列表的地址是否相同
6. not is  # 


```



### 基本操作

```python
# 声明
names = ['tom','jack','lucy','ironman']  # 列表

# 元素获取使用 : 下标 索引
print(names[0])
print(names[1])



name = ['Busy To Live']
res, = name # res = 'Busy To Live'

# 获取最后一个元素
print(names[-1])   # 支持负号
[[]
# 删除

del list[index]  # 删除下标为index的元素

# 结合循环
for name in names:
    print(name)
# 查询names里面有没有保存钢铁侠 

for name in names:  # name = 'tom' name = 'jack'
    if name == 'ironman':
        print('Yes')
        break
	else:
        print('No')
        
# 列表也支持切片
list1 = ['one','two','three','four','five','six','seven','eight']
print(list1[3:6]) # 将截取的结果再次保存在一个列表中 ['four','five','six']
print(list1[-3:-1]) # ['six','seven','eight']

# 反方向
print(list1[-1::-1])
print(list1[-1::-2])  # 步长为2且反方向

```

```python
w = input("请输入一个单词:")
i = 0 # 表示下标
l = len(words)
while i<l:
    if w in words[i]:
        del words[i]
        l-=1
        # i-=l
        continue
    i+=1
print(words)
```

### 内建函数

#### 添加更新

+ append()        # 末尾追加
+ extends()        # 类似与列表的合并   *符号 '+' 也可以用于列表的合并*
+ insert()           # 指定位置插入   

#### 删除

>  **del list[index]   删除列表中下标为index的元素**

+ remove(e)			#  删除列表中第一次出现的元素e ,返回值是None

  ​							  如果没找到要删除的元素则包出异常

+ pop()               #  弹栈 ,移除列表中最后一个元素,返回值是删除的那个元素

  ​							  默认是删除最后一个,但是也可以指定index(下标) 删除

+ clear()              # 清除列表 (里面所有元素全部删除)

#### 其他

+ max()					     #  返回列表里最大的数
+ min()                      #  返回列表里最小的值
+ sorted()                   #  排序(默认是升序排列)   ascending order(升序)  descending order(降序)

+ sum()                     #  对列表中的数进行求和
+ **reverse()                #  反转列表**
+ **len()                      #  返回的是列表的长度值(int)**
+ count()                   # 返回指定元素的个数
+ enumerate()             # 遍历列表  (下标 + 值)



```python
# 排序
1. sorted(list,reverse=True) # 返回的是列表类型的
2. list.sort(reverse=True|False)

# enumerate的用法
'''
语法:
enumerate(sequence, [start=0])
参数:
sequence -- 一个序列、迭代器或其他支持迭代对象。
start -- 下标起始位置。
-------------------------------------------
# 使用普通的for循环:
-------------------------------------------
i = 0
seq = ['one', 'two', 'three']
for element in seq:
	print(i, seq[i])
	i +=1
# 输出结果:
0 one
1 two
2 three

# for循环使用enumerate:
------------------------------------------
seq = ['one', 'two', 'three']
for i, element in enumerate(seq):
	print (i, element)
# 输出结果:
0 one
1 two
2 three

'''
```

列表的分割

```python
list1 = [1,2,3,4,5]
a,*_,b = list1
# _ : [2,3,4] a就为1,b就为5

```







### <font color=red>列表推导式</font>

列表推导式[^1]

> 格式1: `[*i* for i in 可迭代对象]` (最终得到一个列表,第一个i可填一个表达式)

1. 获取一个从1到20的列表:

```python
list1 = [ i for i in range(1,21) ]
```

![python29](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python29.png)

> 格式2: `[ i for i in 可迭代对象 if 条件 ]`

2. 获取0-100间所有偶数

```python
# 方式一: [i for i in range(0,101,2)]
方式二: [i for i in range(101) if i%2==0]
```

![python30](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python30.png)

> 格式3: `[结果1 if 条件 else 结果2 for 变量 in 可迭代对象]`

3. 将一个列表中以z开头得则将其首字母大写,不是z开头得全部转为大写

```python
list1 = ['zhouhao','map','mad','zebra','affinition','100']
list2 = [word.title() if word.startswith('z') else word.upper() for word in list1]
```

![python31](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python31.png)

我们还可以在列表推导式中写多个for循环

```python
new_list = []
for i in range(1,3):
    for j in range(1,3):
        new_list.append((i,j))
print(new_list)
```

这种的我们也可以使用列表推导式来实现

```python
list1 = [(i,j) for i in range(1,3) for j in range(1,3) ]
# 执行顺序为: 前面的(越靠左边的就越先执行)
```

- [ ] **小测验**:

> 请编写出一段Python代码实现分组一个list里面的元素,eg: [1,2,3,4...100] -> [[1,2,3],[4,5,6]...]

```python
list1 = [i for i in range(1,101)]
list2 = [list1[i:i+3] for i in range(0,len(list1),3 )]
```



## 元组(tuple)

特点:

1. 定义的符号 为: ()
2. 元组中的内容不可修改
3. 关键字: tuple

> 定义只有一个元素的元组应该在后面加一个 **,** 否则和没加括号一样



### <font color=red>装拆包</font>

> 列表也支持装拆包



```python
# 拆包,装包
x,*y = (1,2,3,4,5,6) # x = 1  y = [2,3,4,5,6]

x,*_,y = [1,2,3,4,5,6] # x=1 _=[2,3,4,5] y=6

```

![Python20](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python20.png)

#### 字典的拆包

```python
dict1 = {'name':'zhouhao','stuid':1001,'stubirth':'2002-09-08'}
func(**dict1) # 相当于 func(name='zhouhao',stuid=1001,stubirth='2002-09-08')
#  
```





## <font color=red>字典</font>

### 基本操作

#### 与列表的对比

##### 增加



```python
# 列表:
list1 = []
list1.append(element)
```



```python
# 字典:
disct1 = {}
dict1[key]=value
```



```python
# 定义
dict1 = {}      # 空字典
# 可以使用dict()这个函数进行强制转换
dict2 = dict()  # 空字典 
list1 = list() # 空列表 
tuple1 = tuple() # 空元祖
dict3 = {'ID':'123','name':'zhouhao','age':18}
dict4 = dict([('name','zhouhao'),('age',18)])

# 增加

dict5 = {}
# 格式: dict5[key]=value
dict5['brand'] = 'play boy'   #{'brand':'playboy'}

# 修改
'''
列表:
list1[index] = newvalue # 列表使用下标

字典:
dict1[key] = newvalue   # 字典使用键值对

'''
dict1['brand'] = 'apple'

# 查询
'''
列表:
list1[index]   ----> element

字典:
dict1[key]     ----> value

'''
# 我们也可以使用 in 来对字典中key进行判断
dict1 = {'student1': 123, 'student2': 98, 'student3': 89}
print('student1' in dict1) # 输出 True
print('Alice' in dict1)    # 输出 False

```

#### 遍历字典

```python
dict1 = {'name':'zhouhao','ID':3,'grade':100}
for i in dict1:
    print(i)  # 输出:name ID grade 
# 默认遍历字典输出的为字典内所有的key
# 我们可以搭配函数对其进行遍历
items() values() keys()
'''
for i in dict1.items():
	print(i) #输出: ('name', 'zhouhao') ('ID', 3) ('grade', 100)

'''
for key,value in dict1.items():
    print(value) # 输出 zhouhao 3 100



```



#### 删除

```python
'''
列表:
list1=[1,2,3,4,5,6]
del list[1]
print(list1)

字典:
dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
del dict1['Alice']
print(dict1)
# del dict1['LiHua']  # KeyError
'''
# 字典的内置函数 : 删除
# remove()  --> 报错 字典内不能使用这个函数!
1. pop()
2. popitem()
3. clear()
# 例子




```





### 内置函数

#### 1. items()

1. 作用: items() 函数以列表返回可遍历的(键和值) 。
2. *将字典的键值对转成列表保存的形式*

```python
dict1 = {'name':'zhouhao','ID':3,'grade':100}
print(dict1.items())
# 输出：dict_items([('name', 'zhouhao'), ('ID', 3), ('grade', 100)])

# 可以搭配循环对字典进行遍历
```

#### 2. values()

1. *取出字典中所有值,并将其保存到列表中*

```python
dict1 = {'student1': 123, 'student2': 98, 'student3': 89}
print(dict1.values())
#输出: dict_values([123, 98, 89])

# 求所有学生考试成绩的平均分
dict1 = {'student1': 123, 'student2': 98, 'student3': 89}
scores = sum(dict1.values())
lens = len(dict1.values())
aver_dict1 = scores / lens
print(aver_dict1) # 103.33


```

#### 3. keys()

1. *获取字典中所有key键*

```python
dict1 = {'student1': 123, 'student2': 98, 'student3': 89}
print(dict1.keys())
# 输出: dict_keys(['student1', 'student2', 'student3'])

```

> **可以使用`list(),tuple()` 将`<class 'dict_keys'> `转换成对应类型**

```python
list(dict1.keys())
# 输出 ['student1', 'student2', 'student3']
```



#### <font color=red>4. get()</font>

1. 获取字典中相应key对应的value

```python
# 我们知道根据key获取值,如果key在字典里没有存在则报出keyError
dict1 = {'student1': 123, 'student2': 98, 'student3': 89}
print(dict1.get('student1')) # 123
'''
get(key)   ---> value  如果取不到值也不会报错,真返回None
get(key,default)   ---> value 如果能够取到值则返回字典中的值,如果取不到则返回default的值.
'''

dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
# result = dict1['lihua'] # KeyError: 'lihua'
result = dict1['Alice']
print(result)  # 123
result = dict1.get('Mark')
print(result)  # 98
result = dict1.get('lihua')
print(result)  # None
result = dict1.get('lihua',100)
print(result)  # 使用默认值100 输出: 100
```

> 如果`get()` 函数有两个参数则表示如果第参数一个值是字典的键，那么返回该键对应的值，如果该值不是字典的键，那么返回第二个值

#### 5. pop()

1. *根据key删除字典中的键值对,(只要删除成功,则返回键值对的value)*

2. pop的默认值,往往是在删除的时候没有找到对应的key,则返回default默认值

```python
# pop(key,[default])
dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
val = dict1.pop('Mark')
result = dict1.pop('LiHua','字典中没有此键') # 字典中没有此键
print(dict1) # {'Alice': 123, 'Tom': 89}
print(val)   # 98

```

#### 6. popitem()

1. 随机删除字典中的键值对(一般是从末尾开始删除元素)
2. *返回值为字典中被删除的键值对* ( 而pop() 返回的只是值 )

```python
dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
val = dict1.popitem()  
print(dict1) # {'Alice': 123, 'Mark': 98}
print(val) # ('Tom', 89) --- > 与pop()这个函数的区别

```

#### 7. clear()

1. 清空字典中所有键值对

```python
dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
result = dict1.clear()
print(result) # None
print(dict1)  # {}
```

#### 8. update()

1. *将两个字典进行合并* `dict1.update(dict2)    # dict1将为合并的那个字典`

```python

dict1 = {'Alice': 123, 'Mark': 98, 'Tom': 89}
dict2 = {'Lihua': 150, 'Mark': 100, 'Bob': 120}
result = dict1.update(dict2)
print(result) # None
print(dict1) 
# 输出: {'Alice': 123, 'Mark': 100, 'Tom': 89, 'Lihua': 150, 'Bob': 120}
'''
1. 如果合并的两个字典中有相同的key,则默认替换为后面那个字典key对应的值
(如上面例子中的Mark)
2. 合并之后,前面的那个字典,将变为合并之后的字典
'''
```

#### 9. fromkeys()

> 形式: <font color=red>`dict.fromkeys(seq,[default])`</font>

1. 将seq转成字典的形式,如果没有指定默认的value则使用None
2. 如果指定default,则用default替代None这个value值

```python
list1 = ['a','b','c','d']
new_dict = dict.fromkeys(list1)
print(new_dict) 
# 输出: {'a': None, 'b': None, 'c': None, 'd': None}
new_dict = dict.fromkeys(list1,100)
# 输出: {'a': 100, 'b': 100, 'c': 100, 'd': 100}

```

### 其他

#### 根据value查key

1. 将字典列表化

   ```python
   student = {'Mark': '100', 'Mills': '120', 'Tom': '130', 'Alice': '140'}
   result = list(student.keys())[list(student.values()).index('130')]
   print(result)  # 输出为Tom
   ```

2. 定义一个函数

   ```python
   def get_key (dict, value):
       return [k for k, v in dict.items() if v == value]
   get_key(student, '120')
   ```

3. **把字典的key与val互换**

```python
new_dict = {v : k for k, v in student.items()}
new_dict ['100']
# 输出:Mark
```

```python
# 读入一个字符串，统计字符串中每个字符出现的次数，输出结果按次数降序排序。
a = input()
result: dict = {}
for i in set(a):
    result[i] = a.count(i)
b = sorted(result.items(), key=lambda x: x[1], reverse=True)
for i in b:
    print("{} : {}".format(i[0], i[1]))

```



#### 将两个list转dict

>  使用zip函数, 把key和value的list组合在一起, 再转成字典(dict).

```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dictionary = dict(zip(keys, values))
print dictionary
# 输出:
{'a': 1, 'c': 3, 'b': 2}
```

#### 获取字典的键和值

```python
# 获取字典的键
dict1 = {}
result_list = list(dict1.keys())

#
keys = item.keys()
sql = {}.format(','.join(keys))
```





### 字典推导式

> **同列表推导式**

```python
# 将key和value互换
newdict = { val :key for key,value in dict1.items() }

```



## 集合

> 关键字: set (无序的*不重复*元素)

```python
# 声明集合
set1 = set() # 创建空集合,(只能使用set())
set2 = {1,2,5,4} 
print(type(set1)) # set
print(type(set2))　# set
# 字典: {key:value,key:value...}
# 集合: {element1,element2,element3...}

# 应用: 如果有一个列表快速去重使用: set()
list1 = [1,2,3,4,3,3,3,2,4,5,6,7,5,4,3]
s2 = set(list1) # {1, 2, 3, 4, 5, 6, 7}
```

### 基本操作

创建集合后，您无法更改其集合，但可以添加新的数据.

#### 增加元素

##### `add()`

```python
# add 函数只能添加一项到集合里.
# 例如将'Hello','Luck' 添加到集合 set1 里:
'''
set1 = set()
set1.add('Hello')
set1.add('Luck')
print(set1)
'''
```

> 输出: <font color=red>`{'Hello','Luck'}`</font>

##### `update()`

要将另一个集合中的项目添加到当前集合中，我们可以使用 `update()` 方法。

```python
set1 = {'lucy', 'bob', 'alice'}
set2 = {'mark', 'luis', 'alice'}
set1.update(set2)
print(set1)
```

> 输出: <font color=red>`{'alice', 'mark', 'luis', 'bob', 'lucy'}`</font>

<u>当然 `update` 方法中的对象不一定是集合, 它可以是任何可迭代对象 (元祖,列表,字典 等)</u>

update 方法中的对象在不同迭代对象的情况:

+ 当 `update()` 函数内的类型为字符串时会把字符串拆分成每个字母,(不会重复)
+ 如果为字典的话,则默认会将字典的key放入其中.

```python
set1 = {'lucy', 'bob', 'alice'}
dict1 = {'student': 'hellen', 'teacher': 'hennay'}
str1 = 'zhouhao'
set1.update(str1)  # 输出1
set1.update(dict1) # 输出2
```

> 输出1: <font color=red>` {'z', 'a', 'bob', 'h', 'o', 'alice', 'lucy', 'u'}` </font>
>
>  输出2: <font color=red>` {'lucy', 'bob', 'student', 'alice', 'teacher'}` </font>

#### 删除元素

##### `discard()`

**discard     丢弃,废弃,抛弃**



##### `remove()`



##### `pop()`



##### `clear()`



```python


# 删除
# 使用 remove() pop() clear()  discard() 函数

1. remove() # 如果元素存在则删除,不存在则报错KeyError
2. pop() # 随机删除(一般删除第一个元素)
3. clear() # 清空
4. discard # 类似于remove()  但是在移除不存在的时候不会报错

```

### 交并差集运算

```python
set1 = {1,2,3,4,5}
set2 = {4,5,6,7}
- : set1 - set2 # 差集      difference()
& : set1 & set2 # 交集      intersection()
| : set1 | set2 # 并集      union()
^ : set1 ^ set2 # 对称差集   symmetric_difference()
# symmetric : 对称的
set1 = set1.difference(set2)
```

![集合](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/集合.png)

### 集合推导式

> 与列表推倒式几乎完全一致 格式为 { }

[^1]:一种简明扼要创建列表的方式

在列表推导式的基础上,添加了一个*去除重复项*的功能








## 可变/不可变类型

> 可变: 对象所指向的内存中的值是可以改变

+ **可变类型:     dict  list**

==因为`list`, `dict` 是可变类型,使用时一定要注意!==

1. 可变类型重新赋值只是相当于多了一个指向它的指针
2. 在循环时一定要多加注意 `(如以下场景)`

```python
# 你想将爬取的每一条数据(字典)用列表保存下来
## error ##
def parse_data(web_element):
	result_list = []  # 结果列表
	item_dict = {}    # 一条数据的字典
	for item in web_element:
    	item_dict[name] = item[0]
    	item_dict[gender] = item[1]
    	item_dict[grade] = item[2]
    	item_dict[id] = item[3]
        result_list.append(item_dict)
    return result_list
# 如果是这样子写的,那么恭喜你result_list里面是最后一条数据的字典*n
```







> 不可变: 对象所指向的内存中的值是不可以改变的

+ 不可变类型:            *int  str  float  tuple*







## ==函数==

>  <font size=3>将重复的代码,封装成函数,只要使用,就可以调用函数,从而达到增强代码的模块化和提高代码的重复利用率.</font>

```python
# Python函数的格式
def 函数名([参数,参数...]):
    函数体(重复的代码)

```

> *注意: 1. 必须使用关键字def 2. 函数提注意缩进 3. 函数名() 4. 冒号*

```python


```

### 参数

#### 可变参数



```python
# 可变参数 
# 注意: 可变参数必须放在后面
def add(*args):    # 相当 
    print(args)
add()  # 空元祖
add(1,2,3)
add(1,2,3,4)

def add(name,*args):  # 可支持多个参数(name,age,*args)
    result = sum(args)
    print('%s计算的结果为:%s'%(name,result))
add('Alice',1,2,3,4,5)  # 结果为 Alice计算的结果为:15


```

#### 关键字参数

```python
# 关键字参数: key=value
def add(a,b=0):  # 如果没指定第二个参数,默认为value值
    result =a+b
    print(result)
add(5)    #  5
add(4,9)  # 此时的9 

# 可以通过key=value指定特定的值



```

```python
students = {'001':('Alice',19),'002':('Bob',21),'003':('Mark',31)}
def print_boy(persons):
    if isinstance(persons,dict):
        values = persons.values()
        print(values)
        for name,age in values:
            print('{}的年龄是:{}'.format(name,age))
           
# **kwargs就说明:只要函数体外给函数送值,送的值就必须是 key = value

students = {'001':('Alice',19),'002':('Bob',21),'003':('Mark',31)}
def func(**kwargs):  # key word arguments
    print(kwargs)
    
func(**student)   #拆包


# 我们可以在要传递的参数上加一个或两个*号来对列表,元祖,字典进行拆包
def func(*args, **kwargs):
    print(*args)
    if isinstance(args, list):
        for i in args:
            print(args)
    else:
        print('args is not a list!')

    for v, k in kwargs.items():
        print('这个字典的键为{},值为{}'.format(k, v))


list1 = [1, 2, 3, 4, 5]
dict1 = {'luis': 100, 'rose': 150}
func(*list1, **dict1)

'''
[1, 2, 3, 4, 5]
args is not a list!
这个字典的键为100,值为luis
这个字典的键为150,值为rose
'''

```

### 返回值

```python

def main(**kwargs):
    key_list = []
    value_list = []
    for k, v in kwargs.items():
        key_list.append(k)
        value_list.append(v)
    return key_list, value_list


dict_grade = {'zhouhao': 100, 'zhangyuchao': 0, 'Mark': 50}
# result = main(**dict_grade)
# print(result)  # 返回类型  --> 元组
key, value = main(**dict_grade)
print(key, value, sep='---')

```



return 返回值

1. return后面可以是一个参数  接收 result = add(1,2)

2. return 后面也可以是多个参数,如果是*多个参数则底层会将多个参数先放在一个元组*中,将元祖作为整体返回

3. 接收的时候也可以是多个: 

   ```python
   key, value = main(**dict_grade)
   print(key, value, sep='---')
   ```

   
   

### 闭包

> 在函数中提出的概念:*在函数内部定义了另外一个函数并返回了该函数的地址,这种方式称为闭包*

- [x] ==*Hint*: 我们可以使用 *`locals()`* 这个函数来获取函数内部所声明的变量==

**闭包的条件:**

1. 外部函数中定义了内部函数
2. 外部函数是有返回值的
3. 返回值为: *内部函数名*
4. 内部函数引用了外部函数的变量

格式:

```python
def 外部函数():
    .......
    def 内部函数():
        ......
    return 内部函数   # -->记得内部函数的后面不要加括号(返回的为地址,而非调用函数)
```

![python28](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python28.png)

#### 闭包的作用与缺点

> 作用: 保存闭包时的状态,(*保存外层函数的变量*)

1. 可以使用同级的作用域
2. 读取其他元素的内部变量
3. 延长作用域

**缺点:**

1. 作用域没有那么直观
2. 因为变量不会被回收,所以有*一定的内存占用问题*

> 例子:计数器

```python
# 计数器
def generate_count():
    container = [0]
    def add_one():
        container[0] = container[0] +1
        print('当前是第{}次访问'.format(container[0]))
    return add_one
counter = generate_count()
counter() # 第一次
counter()
counter() # 第三次

```

==总结:==

1. 闭包拟优化了变量,原理需要类对象来完成的工作,闭包也可以完成
2. 由于闭包引用了外部函数的局部变量,则外部函数的局部变量没有及时释放,消耗内存
3. 使代码简洁,便于阅读代码
4. 闭包是理解装饰器的基础

### 装饰器

> 装饰器是设计模式的一种，被用于有切面需求的场景，较为经典的有插入日志、性能测试、事务处理等

定义装饰器

```python
# 定义一个装饰器
def decorate(func)  # 传递的参数一定要为函数
	a = 10
    def wrapper():
        print('operation one')
        func() # 调用函数
        print('operation two')
        print(a)
	return wrapper

# 使用装饰器
@decorate
def testfunc():
    print('......')
```

> 加了`@decorate`后

1. `@decorate`下面的函数就成了被装饰函数 (*testfunc*)
2. 将被装饰函数作为参数传给装饰器decorate
3. 执行decorate函数
4. 将返回值又赋值给了被装饰函数(testfunc)  *也就相当于testfunc就是装饰器内层的wrapper函数*



![python32](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python32.png)

为了提高装饰器的兼容性,我们一般采用以下方式建立装饰器

```python
def decorate(func):
    def wrapper(*args,**kwargs):
        func(*args,**kwargs)
        pass
	return wrapper
# 这样的话参数不管为什么的函数,都可以接收,而不会报错
```



#### 带参数的装饰器

> 装饰器带参数,就是有三层

```python
def outer(args): # 第一层负责接收装饰器的参数的
    def decorate(func): # 第二层是负责接收函数的
        def wrapper(*args,**kwargs): # 第三层负责接收函数的参数的
            func(*args,**kwargs)
            pass
        return wrapper # 返回第三层函数地址
    return decorate # 返回第二层函数地址

@outer(10)
def test(time):
    print('-----')


```













**使用场景:**

1. 在实际工作中，如果你怀疑某些函数的耗时过长，导致整个系统的延迟增加，想在线上测试某些函数的执行时间，那么，装饰器就是一种很常用的手段。(*性能测验*)
2. 用于网站等应用上的身份认证
3. 用于输入合理性检查

4. 一般来说在一个项目里,有*好多模块都使用了同一个函数*,但是只有*一些模块需要增加或修改该函数的内容*时,这个时候我们一般也使用装饰器







#### 场景案例

*场景1*: 性能测试

```python
# 性能测试
import time
import functools
def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end - start) * 1000))
        return res
    return wrapper

```

*场景2*: 合理性检测

```python
# 合理性检查
import functools
def validation_check(input):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ... # 检查输入是否合法
```











### 匿名函数

> 格式: lambda 参数1,参数2... : 运算

作用:简化函数定义

```python
func = lambda x, y: x ** y  # lambda 参数:返回结果
result = func(2, 3)
print(result)


# 匿名函数作为参数
def main(x,y,func):
    print(x,y)
    print(func)
    result = func(x,y)
    print(result)
main(1,2,lambda a,b:a+b)

```

### 高阶函数

#### `map|reduce`

Python内建了`map()`和`reduce()`函数。

如果你读过Google的那篇大名鼎鼎的论文“[MapReduce: Simplified Data Processing on Large Clusters](http://research.google.com/archive/mapreduce.html)”，你就能大概明白map/reduce的概念。

我们先看map。`map()`函数接收两个参数，一个是函数，一个是`Iterable`，`map`将传入的函数依次作用到序列的每个元素，并把结果作为新的`Iterator`返回。

举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list `[1, 2, 3, 4, 5, 6, 7, 8, 9]`上，就可以用`map()`实现如下：

```ascii
            f(x) = x * x

                  │
                  │
  ┌───┬───┬───┬───┼───┬───┬───┬───┐
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

 [ 1   2   3   4   5   6   7   8   9 ]

  │   │   │   │   │   │   │   │   │
  │   │   │   │   │   │   │   │   │
  ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼   ▼

[ 1   4   9  16  25  36  49  64  81 ]
```

现在，我们用Python代码实现：

```
>>> def f(x):
...     return x * x
...
>>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> list(r)
[1, 4, 9, 16, 25, 36, 49, 64, 81]
```

`map()`传入的第一个参数是`f`，即函数对象本身。由于结果`r`是一个`Iterator`，`Iterator`是惰性序列，因此通过`list()`函数让它把整个序列都计算出来并返回一个list。

你可能会想，不需要`map()`函数，写一个循环，也可以计算出结果：

```
L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)
```

的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

所以，`map()`作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

```
>>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
['1', '2', '3', '4', '5', '6', '7', '8', '9']
```

只需要一行代码。

再看`reduce`的用法。`reduce`把一个函数作用在一个序列`[x1, x2, x3, ...]`上，这个函数必须接收两个参数，`reduce`把结果继续和序列的下一个元素做累积计算，其效果就是：

```
reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
```

比方说对一个序列求和，就可以用`reduce`实现：

```
>>> from functools import reduce
>>> def add(x, y):
...     return x + y
...
>>> reduce(add, [1, 3, 5, 7, 9])
25
```

当然求和运算可以直接用Python内建函数`sum()`，没必要动用`reduce`。

但是如果要把序列`[1, 3, 5, 7, 9]`变换成整数`13579`，`reduce`就可以派上用场：

```
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> reduce(fn, [1, 3, 5, 7, 9])
13579
```

这个例子本身没多大用处，但是，如果考虑到字符串`str`也是一个序列，对上面的例子稍加改动，配合`map()`，我们就可以写出把`str`转换为`int`的函数：

```
>>> from functools import reduce
>>> def fn(x, y):
...     return x * 10 + y
...
>>> def char2num(s):
...     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
...     return digits[s]
...
>>> reduce(fn, map(char2num, '13579'))
13579
```

整理成一个`str2int`的函数就是：

```
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
```

还可以用lambda函数进一步简化成：

```
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
```

也就是说，假设Python没有提供`int()`函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！

lambda函数的用法在后面介绍。





#### `filter`

Python内建的`filter()`函数用于过滤序列。

和`map()`类似，`filter()`也接收一个函数和一个序列。和`map()`不同的是，`filter()`把传入的函数依次作用于每个元素，然后根据返回值是`True`还是`False`决定保留还是丢弃该元素。

例如，在一个list中，删掉偶数，只保留奇数，可以这么写：

```
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
# 结果: [1, 5, 9, 15]
```

把一个序列中的空字符串删掉，可以这么写：

```
def not_empty(s):
    return s and s.strip()

list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
# 结果: ['A', 'B', 'C']
```

可见用`filter()`这个高阶函数，关键在于正确实现一个“筛选”函数。

注意到`filter()`函数返回的是一个`Iterator`，也就是一个惰性序列，所以要强迫`filter()`完成计算结果，需要用`list()`函数获得所有结果并返回list。

> 用 filter 求素数

计算[素数](http://baike.baidu.com/view/10626.htm)的一个方法是[埃氏筛法](http://baike.baidu.com/view/3784258.htm)，它的算法理解起来非常简单：

首先，列出从`2`开始的所有自然数，构造一个序列：

2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...

取序列的第一个数`2`，它一定是素数，然后用`2`把序列的`2`的倍数筛掉：

3, ~~4~~, 5, ~~6~~, 7, ~~8~~, 9, ~~10~~, 11, ~~12~~, 13, ~~14~~, 15, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...

取新序列的第一个数`3`，它一定是素数，然后用`3`把序列的`3`的倍数筛掉：

5, ~~6~~, 7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...

取新序列的第一个数`5`，然后用`5`把序列的`5`的倍数筛掉：

7, ~~8~~, ~~9~~, ~~10~~, 11, ~~12~~, 13, ~~14~~, ~~15~~, ~~16~~, 17, ~~18~~, 19, ~~20~~, ...

不断筛下去，就可以得到所有的素数。

用Python来实现这个算法，可以先构造一个从`3`开始的奇数序列：

```
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
```

注意这是一个生成器，并且是一个无限序列。

然后定义一个筛选函数：

```
def _not_divisible(n):
    return lambda x: x % n > 0
```

最后，定义一个生成器，不断返回下一个素数：

```
def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
```

这个生成器先返回第一个素数`2`，然后，利用`filter()`不断产生筛选后的新的序列。

由于`primes()`也是一个无限序列，所以调用时需要设置一个退出循环的条件：

```
# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break
```

注意到`Iterator`是惰性计算的序列，所以我们可以用Python表示“全体自然数”，“全体素数”这样的序列，而代码非常简洁。





#### `sorted`

> 排序算法

排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，因此，比较的过程必须通过函数抽象出来。

Python内置的`sorted()`函数就可以对list进行排序：

```
>>> sorted([36, 5, -12, 9, -21])
[-21, -12, 5, 9, 36]
```

此外，`sorted()`函数也是一个高阶函数，它还可以接收一个`key`函数来实现自定义的排序，例如按绝对值大小排序：

```
>>> sorted([36, 5, -12, 9, -21], key=abs)
[5, 9, -12, -21, 36]
```

key指定的函数将作用于list的每一个元素上，并根据key函数返回的结果进行排序。对比原始的list和经过`key=abs`处理过的list：

```
list = [36, 5, -12, 9, -21]

keys = [36, 5,  12, 9,  21]
```

然后`sorted()`函数按照keys进行排序，并按照对应关系返回list相应的元素：

```ascii
keys排序结果 => [5, 9,  12,  21, 36]
                |  |    |    |   |
最终结果     => [5, 9, -12, -21, 36]
```

我们再看一个字符串排序的例子：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'])
['Credit', 'Zoo', 'about', 'bob']
```

默认情况下，对字符串排序，是按照ASCII的大小比较的，由于`'Z' < 'a'`，结果，大写字母`Z`会排在小写字母`a`的前面。

现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。

这样，我们给`sorted`传入key函数，即可实现忽略大小写的排序：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
['about', 'bob', 'Credit', 'Zoo']
```

要进行反向排序，不必改动key函数，可以传入第三个参数`reverse=True`：

```
>>> sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
['Zoo', 'Credit', 'bob', 'about']
```

从上述例子可以看出，高阶函数的抽象能力是非常强大的，而且，核心代码可以保持得非常简洁。

### 小结

`sorted()`也是一个高阶函数。用`sorted()`排序的关键在于实现一个映射函数。

## 文件操作

### open函数

```python
stream = open(path/filename,'rt') # 返回值: stream(流) 管道
```

我们可以用一个变量来接收流中的数据

**读操作:**

```python
container = stream.readable() # 判断是否可读
container = stream.read() #一次性读取管道内所有内容
container = stream.readline() # 一次只读一行内容
container = stream.readlines() # 读取所有行，并将其保存在列表里
```

**写操作:**

```python
mode 为'w'表示就是写操作(默认会覆盖原有的东西) 'a'表示追加模式(append)
stream = open(path/filename,'w')
# 方法:
write(内容)  # 写当前内容
writelines(Iterable) # 没有换行效果
stream.writelines(['cell1\n','cell2\n']) # 需要换行要使用这种方式
```

---

```python
mode: r w rb wb
    r: read   # 读操作
    w: write  # 写操作
    b: binary # 二进制
'''
rb: read binary
# 这两种方式一般用在图片,音乐,电影,等的读写操作
wb: write binary
'''
# open官方文档 # 默认使用rt
'''
========= ===============================================================
    Character Meaning
    --------- ---------------------------------------------------------------
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing
    'a'       open for writing, appending to the end of the file if it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)
========= ===============================================================
'''
        

```

### ==OS模块==

**with结合open使用,可以帮助我们自动释放资源**

```python
with open(r'path','mode') as stream:
    pass
```

#### os.path

1. 基本使用

```python
os.path # 返回os模块库的路径
os.path.dirname(__file__) # 获取当前文件所在的文件目录(绝对路径)
os.path.join(path,'str') # 返回的是一个拼接后的新路径
eg: result = os.path.join(os.getcwd(),'file','note','Linux')
# 每多一个参数就多一层路径
```

2. *通过相对路径得到绝对路径*

```python
path = os.path.abspath('aa.txt')
```

3. 获得当前文件的绝对路径

```python
path = os.path.abspath(__file__)
```

4. 获取当前文件所在的目录的路径

```python
path = os.getcwd() # 类似于 os.path.dirname(__file__)
```

5. 分割路径

```python
result = os.path.split(path) # 分割文件名与路径(以元组返回)
result = os.path.splittext(path) # 分割文件与文件扩展名(以元组返回)
```

6. 获取文件大小

```python
python = os.path.getsize(path # 单位为字节
```

7. 判断文件或文件夹是否存在

```python
os.path.exists(r'c:\usr\local\')
```



#### Others

1. **返回指定目录下所有文件和文件夹**

```python
all = os.listdir(r'c:\user\local\')
all --> 为一个列表 (返回值为所有文件夹和文件名组成的列表)
```

2. 删除,创建文件夹

```python
os.mkdir # 创建文件夹
os.remove # 删除文件
# os.removedirs # 删除空文件夹
os.rmdir # 删除空文件夹


```

3. 切换目录

```python
os.chdir()
```



## 异常处理

**格式**:

```python
try:
    #可能出现异常的代码
except:
    #如果有异常将执行的代码    
finally:
    无论是否存在异常都会被执行的代码    
```

*情况1*:

```python
try:
    #可能出现异常的代码
except 异常类型1:  # ZeroDivisionError ValueError ...
    # ......
except 异常类型2:
    # ......
except Exception:
    pass
# 如果是多个except, 异常类型的顺序需要注意,最大的Exception要放到最后
```

 我们也可以使用这种方式来显示出错的原因(*系统自动报出的*)

*情况2*:

```python
try:
    # 可能出现异常的代码
except ZeroDivisionError:
    pass
except ValueError:
    pass
except Exception as err: # 获取Exception错误的原因
    print('some error occured!',err)
```

*情况3:*

```python
try:
    pass
except ValueError:
    pass
else:
    print('----') # 没有发生异常时才会执行的代码块
    pass

```

> 返回值问题

```python
def func():
    stream = None
    try:
        stream = open(r'c:/zhouhao/busy.txt')
        container = stream.read()
        print(container)
        return 1
    except Exception as err:
        print(err)
        return 2
    finally:
        print('--finally--')
        if stream:
            stream.close()
        return 3
# 不管是出错了没返回的结果都为3 (都会进到finally里面去)
result = func()

```

### raise

> 程序员可以通过raise自定义错误抛出机制,和提示机制

```python
def register():
    username = input('Please enter your username:')
    if len(username) < 2:
        raise Exception('The lenth less then two!')
    else:
        print('Your name is:',username)
try:
    register()
except Exception as err
	print(err)
	print('sorry! register error!')
else:
    print('register success!')
   

```













## 生成器

背景:

> 通过列表推导式,我们可以直接创建一个列表,但是,受到内存的限制,*列表容量肯定是有限的*.而且,创建一个包含100万个元素的列表,不仅*占用很大的存储空间*,如果我们仅仅需要访问前面几个元素,那后面*绝大多数元素占用的空间都白白浪费*了,所以,如果列表元素可以按照某种算法推算出来,拿我们是否可以*在循环的过程中不断推算出后续的元素*呢?这样就不必创建完整的list,从而节省大量的空间,在Python中,*这种一边循环一边计算的机制,称为生成器*: *generator*

### 定义生成器

1. 使用列表推导式

```python
generator = ( x*2 for x in range(10) )
```

2. *函数加yield关键字*
   + 定义一个函数,函数中使用yield关键字
   + 调用函数,接收调用的结果

```python
def generator():
    i = 2
    while true:
        n = i**2
        yield n # 相当于 return n + 暂停的操作
g = generator()
next(g)

```

在yield后还有return XXX,就是在得到StopIteration后的提示信息

```python
def gen():
    i=0
    while i<5:
        temp = yield i 
        print('temp',temp)
        i+=1
    return '没有更多数据了!'
        
```





### 生成器方法

1. \__next__() :  获取下一个元素
2. send(value): 向每次生成器调用中传值 *( 注意: 第一次调用时要传一个空值None )  ---  send(None)*



### 应用

> 协程

```python
def task1(n):
    for i in range(n):
        print('[{}]working...(task1)'.format(i))
        yield None
def task2(n):
    for i in range(n):
        print('[{}]working...(task2)'.format(i))
        yield None
g1 = task1(5)
g2 = task2(5)
while True:
    try:
        g1.__next__()
		g2.__next__()
    except:
        pass

```








## 迭代器

> 可以被next()函数调用并不断返回下一个值的对象称为迭代器: Iterator

迭代是访问集合元素的一种方式.迭代器是一个可以记住遍历的位置的对象>

迭代器对象从集合的第一个元素开始访问,直到所有的元素被访问完结束

迭代器只能往前,不会后退

可迭代对象: 

1. 生成器
2. 元组
3. 列表
4. 集合
5. 字符串

- [ ] 如何判断一个对象是否是可迭代?
  - 可以使用*`isinstance()`函数* 而`Iterable` 需要导入`collections`这个库

```python
from collections import Iterable
list1 = [1, 2, 3, 4]
result = isinstance(list1, Iterable)
print(result)
```

- [x] 可迭代的是不是肯定就是迭代器?
  + 生成器是可迭代的,也是迭代器
  + List是可迭代的,但不是迭代器(*它不能被next()函数调用*)





## ==面向对象==

> 专有名词

1. 类
2. 对象
3. 属性
4. 方法

```python
# 所有的类名要求首字母大写, 多个单词使用驼峰式命名法
# ValueError TypeError StopIterable
# 在python里默认所有类继承 object
# 格式:
'''
class 类名[(父类)]:
    属性: 特征

	方法: 动作

'''
class Phone:
    brand = 'iphone'


print(Phone)

# 使用类创建对象
object1 = Phone()  # 对象object1
object2 = Phone()  # 对象object2
print(object1)
print(object2)

```

![python25](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python25.png)

### 1. 对象属性







### 2. 构造器&\__init__

```python
class Phone:
# 魔术方法之一 格式: __名字__()
    def __init__(self)   # init 初始化,初始的
	
```



### 3. 类方法

```python

@classmethod
def test(cls):   # cls -->class
    print(cls)
    print(cls.)
```

> 特点

1. 定义需要依赖*装饰器*

2. 类方法中参数不是一个对象,而是类

   print(cls)   # <class '\_\_main\_\_.Dog'>

3. 类方法中只可以使用类属性

4. 类方法中不能使用普通方法

> 作用

因为只能访问类属性和类方法,所以可以在对象创建之前,完成一些动作和功能.



### 4. 静态方法

1. 需要装饰器 @staticmethad
2. 静态方法是无需传递参数的 (cls,self)
3. 也只能访问类的属性和方法,对象的是无法访问的
4. 加载时机同类方法



### 5.魔术方法

> 魔术方法就是一个类/对象中的方法，和普通方法唯一的不同是，普通方法需要调用！而魔术方法是在特定时刻自动触发

#### 1. `__init__`

```python
初始化魔术方法
触发时机: 初始化对象时触发 (不是实例化触发,但是和实例化在一个操作中)
参数: 至少有一个self,接收对象
返回值: 无
作用: 初始化对象成员
注意: 使用该方法初始化的成员都是直接写入对象中,类中无法具有
```

#### 2. `__new__`

```python
实例化魔术方法
触发时机: 在实例化对象时触发
参数: 至少一个cls接收当前类
返回值: 必须返回一个对象实例
作用: 实例化对象
注意: 实例化对象是Object类底层实现,其他类继承了Object的__new__才能实现实例化对象,没事别碰这个魔术方法,先触发__new__才会触发__init__
```

#### 3. `__call__`

```python
对象调用方法
# 触发时机: 将对象当做函数调用时触发 对象()
# 参数: 至少一个self接收对象, 其余根据调用时参数决定
返回值: 根据情况而定
作用: 可以将复杂的步骤进行合并操作,并减少调用的步骤,方便使用
注意: 无
```

#### 4. `__del__`

```python
析构魔术方法
# 触发时机: 当对象没有用(没有任何变量引用)的时候被触发
参数: 一个self
返回值: 无
作用: 使用完对象是回收资源
注意: del不一定会触发当前方法,只有当前对象没有任何变量接收时才触发
  
'''
1. 对象赋值
	p = Person()
	p1 = p
	说明: p和p1共同指向同一个地址
2. 删除地址的引用
	del p1 # 删除p1对地址的引用
3. 查看对地址的引用次数:
	import sys
	sys.getrefcount(p)

'''
```

#### 5. `__str__`





```python
触发时机:使用print(对象)或者str(对象)的时候触发
参数：一个self接收对象
返回值：必须是
字符串类型
作用：print（对象时）进行操作，得到字符串，通常用于快捷操作
注意：无
```

#### 6. `__len__`

```python
触发时机：使用len(对象) 的时候触发
参数：一个参数self
返回值：必须是一个整型
作用：可以设置为检测对象成员个数，但是也可以进行其他任意操作
注意：返回值必须必须是整数，否则语法报错，另外该要求是格式要求。

```

#### 7.`__getattr__`

```python
触发时机: 仅当属性不能在实例的__dict__或它的类(类的__dict__),或父类的__dict__中找到时，才被调用
# 适合
    
```

```python
class Color:
    # 定义颜色类型
    colors = {  # Format: (ansi, pygments)
        # foreground
        "white": ("", "#white"),
        "text": ("", "#text"),
        "success": ("\033[32m\033[1m", "#success"),
        "black": ("\033[30m", "#ansiblack")
    }
    def __getattr__(self, attr):
        return self.colors.get(attr, [""])[0]
    # 这个时候就可以通过对象名加colors字典内的
```





#### 8. `__repr__`

```python
是由repr()内置函数调用，用来输出一个对象的“官方”字符串表示。返回值必须是字符串对象，此方法通常被用于调试。内置类型 object 所定义的默认实现会调用
```



### 6. 私有化

> 封装: 1. 私有化属性 2. 定义公有set和get方法

1. 隐藏属性不被外界随意修改
2. 可以使用函数对其进行修改
3. `--属性名` 这种形式来私有化属性

`私有化后系统默认会在属性前面加_类名`

```python
xx: 公有变量
_x: 单前置下划线,私有化属性或方法，from somemodule import *禁止导入,类对象和子类可以访问
__xx：双前置下划线,避免与子类中的属性命名冲突，无法在外部直接访问(名字重整所以访问不到)
xx:双前后下划线,用户名字空间的魔法对象或属性。例如:init , __ 不要自己发明这样的名字
xx_:单后置下划线,用于避免与Python关键词的冲突
```

![Python26](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Python26.png)

私有化属性后,我们会发现对属性的修改变得较为麻烦( *每次修改和获取都要调用 `set()` ,和 `get()`* ) 我们有没有一种方法让对属性进行私有化,但使用的时候和没有私有化一样呢?

```python
# 我们可以通过@property这个装饰器来实现:

@property
def age(self):
    return self.__age
@age.setter
def age(self,age):
    if age > 0 and age < 100:
        self.__age = age
    else:
        print('Not within the specified range!')

```



### 7. 单例模式

```python
# 默认写法
class Singleton:
    # 私有化 单例的地址就存在于__instance
    __instance = None
    name = 'Busy To Live'
    # 重写__new__
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = object.__new_(cls)
		return cls.__instance
    
```



































































































































## 模块/包

### 模块

#### 基本概述

在Python中,模块是代码组织的一种方式, *把功能相近的函数或者类放到一个文件中, 一个文件 `.py` 就是一个模块( `module` )*模块名就是文件名去掉后缀`py` 这样做的好处是:

+ 提高代码的 ==可复用性 可维护性==。一个模块编写完毕后,*可以很方便的在其他项目中导入*
+ 解决了命名冲突,不同模块中相同的命名不会冲突

>  我们在导入模块时,计算机会将==模块内的代码自动加载到内存中==

```python
# 当我们不想代码内的函数被调用时,可以使用__name__
# 在自己的模块里面__name__就叫: __main__
# 如果在其他模块中通过导入的方式调用的话:__name__: 为模块名
# 用法:
    if __name__ =='__main__':
        # Code
```

**当你导入一个模块,Python解释器对模块位置的搜索顺序是:**

1. 当前目录
2. 如果不在当前目录,`Python`解释器则搜索在`shell`变量`PYTHONPATH`下的每个目录
3. 如果找不到,`Python`会察看默认路径.`Unix`下,默认路径一般为`/usr/local/lib/python/`
4. 模块存储路径存储在`system`模块的 `sys.path` 变量中. 变量包含当前目录,`PYTHONPATH`和由安装过程决定的默认 

```python
# 在模块里我们可以通过__all__来限制*号所导入的内容
__all__ = ['',''] #列表内的就是*号可以导入的东西
```

**导入模块的几种方式**

```python
# 导入模块  	
1. import 模块名

# 使用: 模块名.变量 模块名.函数 模块名.类		
2. form 模块名 import 变量/函数/类 #(这样在代码中就可以直接使用变量/函数和类了)	
3. from 模块名 import * # 这样是导入模块中所有内容	
# 但是如果想限制获取的内容,可以在模块中使用 __all__ = [使用*可以访问到的内容]	['','']	
```

#### ==内置模块==

##### `random`



##### `hashlib`



##### `inspect`

##### ==`itertools`==





生成 $A^4_4$ 的全排列

```python
import itertools
for val in itertools.permutations('ABCD'): # 生成ABCD的全排列 (参数为可迭代对象)
    print(val)
```

生成 $A^2_4$ 的排列数

```python
for val in itertools.permutations('ABCD',2): 
    print(val)
```

生成组合数

```python
for val in itertools.combinations('ABCD',2):
    print(val)
```



笛卡尔集

```python
for val in itertools.product('ABC','1234'):
    print(val)
#结果:    
('A', '1')
('A', '2')
('A', '3')
('A', '4')
('B', '1')
('B', '2')
('B', '3')
('B', '4')
('C', '1')
('C', '2')
('C', '3')
('C', '4')
```





##### `time`



##### `collections`

```python
init_dict = defaultdict(int)
```



##### `functools`

<font color=#fe6254 size=4>`partial`</font>

偏函数的作用：和装饰器一样，它可以扩展函数的功能，但又不完成等价于装饰器。

通常应用的场景是当我们要*频繁调用某个函数时，其中某些参数是已知的固定值，通常我们可以调用这个函数多次*，但这样看上去似乎代码有些冗余。

举一个很简单的例子，比如我就想知道 100 加任意数的和是多少，通常我们的实现方式是这样的：

```python
# 第一种做法：
def add(*args):
    return sum(args)

print(add(1, 2, 3) + 100)
print(add(5, 5, 5) + 100)

# 第二种做法
def add(*args):
    return sum(args) + 100  # 对传入的数值相加后，再加上100返回

print(add(1, 2, 3))  # 106
print(add(5, 5, 5))  # 115 
```

但上面两种做法都会存在有问题：

1. 第一种：100这个固定值会返回出现，代码总感觉有重复；
2. 第二种：就是当我们想要修改 100 这个固定值的时候，我们需要改动 add 这个方法。下面我们来看下用 parital 怎么实现：

```python
from functools import partial

def add(*args):
    return sum(args)

add_100 = partial(add, 100)
print(add_100(1, 2, 3))  # 106

add_101 = partial(add, 101)
print(add_101(1, 2, 3))  # 107
```



大概了解了偏函数的例子后，我们再来看一下偏函数的定义：

```python
类func = functools.partial(func, *args, **keywords)
```

我们可以看到，partial 一定接受三个参数，从之前的例子，我们也能大概知道这三个参数的作用，简单介绍下：

```python
func:          # 需要被扩展的函数，返回的函数其实是一个类 func 的函数
*args:        # 需要被固定的位置参数
**kwargs: # 需要被固定的关键字参数
# 如果在原来的函数 func 中关键字不存在，将会扩展，如果存在，则会覆盖
```

用一个简单的包含位置参数和关键字参数的示例代码来说明用法：

```python
# 同样是刚刚求和的代码，不同的是加入的关键字参数
def add(*args, **kwargs):
    # 打印位置参数
    for n in args:
        print(n)
    print("-"*20)
    # 打印关键字参数
    for k, v in kwargs.items():
       print('%s:%s' % (k, v))
    # 暂不做返回，只看下参数效果，理解 partial 用法

# 普通调用
add(1, 2, 3, v1=10, v2=20)
"""
1
2
3
--------------------
v1:10
v2:20
"""

# partial
add_partial = partial(add, 10, k1=10, k2=20)
add_partial(1, 2, 3, k3=20)
"""
10
1
2
3
--------------------
k1:10
k2:20
k3:20
"""

add_partial(1, 2, 3, k1=20)

"""
10
1
2
3
--------------------
k1:20
k2:20
"""
```

最后，我们来看一下官方文档中的解释，相信有了前面的介绍，再回头来看官方文档，应该会比较好理解了，同时也能加深我们的印象：

> functools.partial(func, *args, **keywords)
> Return a new partial object which when called will behave like func called with the positional arguments args and keyword arguments keywords. If more arguments are supplied to the call, they are appended to args. If additional keyword arguments are supplied, they extend and override keywords. Roughly equivalent to:

简单翻译: 它返回一个偏函数对象，这个对象和 func 一样，可以被调用，同时在调用的时候可以指定位置参数 (*args) 和 关键字参数(**kwargs)。如果有更多的位置参数提供调用，它们会被附加到 args 中。如果有额外的关键字参数提供，它们将会扩展并覆盖原有的关键字参数。它的实现大致等同于如下代码：

```python
# 定义一个函数，它接受三个参数
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*args, *fargs, **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```

> The partial() is used for partial function application which “freezes” some portion of a function’s arguments and/or keywords resulting in a new object with a simplified signature. For example, partial() can be used to create a callable that behaves like the int() function where the base argument defaults to two:

简单翻译：partial() 是被用作 “冻结” 某些函数的参数或者关键字参数，同时会生成一个带有新标签的对象(即返回一个新的函数)。比如，partial() 可以用于合建一个类似 int() 的函数，同时指定 base 参数为2，代码如下：

```text
# 这个代码很简单，就不啰嗦了
>>> from functools import partial
>>> basetwo = partial(int, base=2)
>>> basetwo.__doc__ = 'Convert base 2 string to an int.'
>>> basetwo('10010')
```













### 包

>  <kbd>ALT </kbd>+ <kbd>ENTER</kbd>   *# 快速提醒, 快速导入包(Pycharm 快捷键)*



####` __init__.py` 文件

> 当导入包的时候,默认会调用`__init__.py`文件

==作用:==

1. 当导入包的时候,把一些初始化的函数,变量,类定义在`__init__.py`文件中
2. 此文件中函数,变量等的访问,只需要通过包名,函数...
3. *结合`__all__` = [通过可以访问的模块]*

```python
文件夹 一般存放非py文件

包一般存放多个py文件(包含一个__init__.py)
# 一个包中可以存放多个模块
# 项目 > 包 > 模块 > 类 > 函数 > 变量

from 模块名 import *  # 默认可以使用模块里面的所有内容,(如果没有定义__all__所有的都可以访问)

from 包名 import *   # 默认该包中的内容(模块)是不能访问的,就需要在__init__.py文件中定义__all__
# 格式: __all__ = [相要通过*能够访问的模块]
```








```python
sys.path   # 路径
sys.argv  # 参数
sys.verson # 版本


```



```python
t = time.time()
s = time.ctime(t)      # 将时间戳转换成字符串
t = time.localtime(t)  # 将时间戳转换成元组
t = time.mktime(t)     # 将元组转换成时间戳
# 元组时间: t.tm_year t.tm_ 
# 将元组的时间(或当前时间戳)转换成字符
s = time.strftime('%Y-%m-%d %H:%M:%S')
print(s)

#将字符串转换成元组的方式
r = time.strptime('2019/06/20','%Y/%m/%d')
print(r)


random模块

item = random.random.randrange(1,10,2)  # rangrange(start,end,step) 1~10 step=2
item = random.randint(1,10)

list1 = ['item1','item2','item3']
item = random.choice(list1)  # 常用可以随机取出列表里的值
result = random.shuffle(list1)  # shuffle-->洗牌 
# result -> None 将列表乱序排列


# 验证码案例
def func():
    code=''
    for i in range(4):
        ran1 = str(random.randint(0,9))
        ran2 = chr(random.randint(65,90))
        ran3 = chr(random.randint(97,122))
        
        r = random.choice([ran1,ran2,ran3])
        code+=r
       return code
code = func()
print(code)
# 获取随机小数
random_float = random.uniform(1.0,3.0)
round(random_float,2) # ( )







```



### hashlib





```python
import hashlib


def main():
    digester = hashlib.md5()
    with open('analyse.py', 'rb') as file_stream:
        data = file_stream.read(1024)
        while data:
            digester.update(data)
            data = file_stream.read(1024)
        print(digester.hexdigest())


if __name__ == '__main__':
    main()
  
# 代码优化

def main():
    digester = hashlib.md5()
    with open('analyse.py', 'rb') as file_stream:
        for data in iter(lambda: file_stream.read(1024), b''):
            digester.update(data)
        print(digester.hexdigest())
```





## 正则表达式

正则表达式,又称正规表示法,常规表示法 etc (英语: **Regular Expression **)在代码中常简写为( **regex , regexp , RE** )

![regex](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/regex.png)



### re模块

#### compile

> 作用: 判断要判断的字符与匹配字符是否完全一致(*只有完全一致才匹配*)

```python


```



#### match

> 作用: 从开头匹配一次

```python




```



#### search

> 作用: 查找整个字符串(也只匹配一次)

```python



```



#### findall

> 作用: 查找所有(匹配所有符合正则的字符)

```python




```

#### sub

> 作用: 替换匹配得到字符串(可接收函数)

```python
# (正则表达式,'新内容',string) 替换 (新内容可以为函数)

```

#### split

> 作用: 将字符串根据正则表达式进行匹配后分割,并将内容保存在列表里

```python
result = re.split(r'[,:]',java:99,python:95')
# 在字符串中搜索如果遇到:或者,就分割,并将分割内容保存到列表里


```











```python
s = 'zhouhaobusy@163.com'

result = re.match('zhouhao',s)
print(result)
result = re.search('zhouhao',s)
print(result)
print(result.span())
 
```

### 正则的匹配符号



| <font face=楷体 size =5>符号</font> | <font face=楷体 size=5>符号所代表的正则含义</font>           |
| ----------------------------------- | ------------------------------------------------------------ |
| ' ^ '                               | <font color=#FF3502>用于匹配字符串的开始</font>              |
| ' . '                               | 用于匹配除换行符(\n)之外的所有字符                           |
| ' $ '                               | <font color=#FF3502>用于匹配字符串的末尾(末尾如果有' \n ',就匹配 \n 前面的哪个字符),及行尾</font> |
| ' * '                               | 用于将前面的模式匹配0次或多次 ( 贪婪模式, 即尽可能多的匹配 ) |
| ' + '                               | 用于将前面的模式匹配一次或多次 ( 贪婪模式 )                  |
| ' *? , +? , ?? '                    | 即上面三种特殊符号的非贪婪模式 ( 尽可能少的匹配 )            |
| ' {m,n} '                           | 用于将前面的模式匹配 m 次到 n 次 (贪婪模式) , 即最小匹配m次,最大匹配n次 |
| ' {m,n}? '                          | 即上面 ' {m,n} ' 的非贪婪版本                                |
| ' \\\\ '                            | ' \ '是转义字符,在特殊符号前面加上\ , 特殊字符就失去了其所代表的含义 |
| ' [] '                              | 用于表示一组字符,如果 ^ 是第一个字符,则它所表示的是一个补集, [0-9] 表示所有的数字, [\^0-9] 代表除数字外的字符 |
| ' \| '                              | 表示'或' 比如 A\|B 用于匹配A或B                              |
| ' (...) '                           | 用于匹配括号中的模式,可以在字符串中检索或匹配我们所需要的内容 |
| ' {m} '                             | 用于将前面的模式匹配m次                                      |
| ' {m,} '                            | 匹配m次及以上                                                |

---







| 符号 | 含义                                                         |
| ---- | ------------------------------------------------------------ |
| \A   | 表示从字符串的开始处匹配                                     |
| \Z   | 表示从字符串的结束处匹配,如果存在换行,只匹配到换行前的结束字符串 |
| \b   | 匹配一个单词边界,也就是指单词和空格间的位置.例如: ' py\b ' 可以匹配 'python'中的 'py' 但不匹配 'openpyxl' 中的 'py' |
| \B   | 匹配非单词边界. ' py\B ' 可以匹配 'openpyxl'中的 'py' 但不匹配 'python' 中的 'py' |
| \d   | 匹配任意数字,等价于[0-9]   # digit                           |
| \D   | 匹配任意非数字字符,等价于[\^\\d]                             |
| \s   | 匹配任意空白字符,等价于  [\\t\n\r\f]  # space                |
| \S   | 匹配任意非空白字符, 等价于 [\^\s]                            |
| \w   | 匹配任意字母数字及下划线,等价于 [a-zA-Z0-9_]                 |
| \W   | 匹配任意非字母数字及下划线,等价于 [\^\w]                     |
| \\\  | 匹配原意的反斜杠                                             |



```python
# 量词
*  >=0
+  >=1
?  0,1

{m}  固定m位
{m,} >=m
{m,n} 
#Python里数量词默认是贪婪的(在少数语言里默认是非贪婪的) 

贪婪模式 --> 总是尝试匹配尽可能多的字符
非贪婪模式(相反) --> 总是尝试匹配尽可能少的字符 
```

```python
# number
result = re.match 





```

> 起名匹配

```python
import re
# 起名的方式 (?P<名字>正则)  
# 使用: (?P=名字)
msg = '<html><h1>zhouhaobusy</h1></html>'
result = re.match(r'<(?P<name1>\w+)><(?P<name2>\w+)>(.+)</(?P=name2)></(?P=name1)>')


```



## 资源管理

> `CPU`密集型 ( `CPU-bound` )

*`CPU`密集型: 也叫计算密集型,是指`I/O`在很短的时间就可以完成,CPU需要大量的计算和处理,特点是CPU占用率相当高*

例如: 压缩解压缩,加密解密,正则表达式搜索

> `I/O`密集型 ( `I/O bound` )

*`I/O`密集型: 指的是系统运作大部分的状况是`CPU`在等`I/O`(硬盘/内存)的读/写操作,`CPU`占用率仍然较低*

例如: 文件处理程序.网络爬虫程序,读写数据库程序

**`什么是GIL`**

全局解释器锁 ( `Global Interpreter Lock` 缩写 `GIL` )

是计算机程序设计语言解释器用于1同步线程的一种机制,它使得任何时刻仅有一个线程在执行.即使在多核处理器上,使用GIL的解释器也只允许同一时间执行一个线程



### 线程 `Thread`

> Python里`threading`实现 

### 进程 `Process`

> Python里`multiprocessing`实现 



### 协程 `Coroutine`

> Python里`asyncio`实现 



### 池子

>   当需要创建的子进程数量不多时,可以直接利用multiprocessing中的Process动态生成多个进程,**但如果是上百甚至上千个目标,手动的去创建进程的工作量巨大**,此时就可以用到multiprocessing模块提供的Pool方法.初始化Pool时,可以指定一个最大进程数,当有新的请求提交到Pool中时,如果池还没满,那么就会创建一个新的进程用来执行该请求;但如果池中的进程数已经达到指定的最大值,**那么该请求就会等待.直到池中有进程结束,才会创建新的进程来执行**

### 线程

```python
import threading
from time import sleep


def func1():
    for i in range(10):
        sleep(0.3)
        print('working... func1')


def func2():
    for i in range(10):
        sleep(0.3)
        print('working... func2')


# target 需要的是一个函数,用来指定线程需要执行的任务
t1 = threading.Thread(target=func1)  # 创建了线程1
t2 = threading.Thread(target=func2)  # 创建了线程2
# 启动线程
t2.start()
t1.start()

```









### 协程

## 虚拟环境

> 虚拟环境的安装: **pip install virtualenv**

1. 创建虚拟环境 ( 就是在PATH变量最前面添加了一条虚拟环境可执行文件的路径 )

```shell
virtualenv env
source env/bin/activate
# activate 是一个shell脚本(就是拿来修改PATH变量用的)

# 这时候就进入了虚拟环境()
which python # /usr/local/Python_Code/grayhat/env/bin/python
```

2. 如果使用 `pycharm` 打开,指定 `env` 下的虚拟解释器即可
3. 也可以自己添加PATH变量来实现

```shell
export PATH="/usr/local/python_project/Demo/env/bin:$PATH"
# /usr/local... 为虚拟环境(可执行文件)的路径

```

**deactivate**

退出虚拟环境

1. 获取当前`pip` 使用了哪个python解释器

```shell
which pip
# 查看pip文件
cat $(which pip) # 在第一行就指定了pip的python解释器的路径
```

我们也可以修改pip文件的第一行来指定pip安装的包到哪个python解释器

比如下面这个pip文件 第一行就指定了`/usr/bin/python3` 这个解释器 

```python
#!/usr/bin/python3 
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==20.3.4','console_scripts','pip'
import re
import sys
# for compatibility with easy_install; see #2198
```

```shell
export PS1="(env)"
# PS1就是代表终端前面的东西
# 我们可以修改PS1来修改终端前面的提示符
( )
```



在windows里导出虚拟环境安装的包

```python
import os
import platform
import sys
import subprocess

# 找到当前目录
project_root = os.path.dirname(os.path.realpath(__file__))
# project_root = os.path.realpath(__file__)
print('当前目录' + project_root)

# 不同的系统，使用不同的命令语句

if platform.system() == 'Linux':
    command = sys.executable + ' -m pip freeze > ' + project_root + '/requirements.txt'
if platform.system() == 'Windows':
    command = '"' + sys.executable + '"' + ' -m pip freeze > "' + project_root + '\\requirements.txt"'
# # 拼接生成requirements命令
print(command)
#
# 执行命令。
# os.system(command)  #路径有空格不管用
os.popen(command)  # 路径有空格，可用
# subprocess.call(command, shell=True)  #路径有空格，可用
```







## 代码编辑器

### ipython



在变量,函数,对象后面加个 `?` 后可显示相应的文档



![Snipaste_2022-01-06_17-41-18](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Snipaste_2022-01-06_17-41-18.png)




在变量,函数,对象后面加两个 `??` 后可显示相应的源码

![Snipaste_2022-01-06_17-39-06](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Snipaste_2022-01-06_17-39-06.png)


我们可以使用 `clear` 或者  <kbd>Ctrl + L</kbd> 进行清屏

`! + 命令` 在`ipython`里执行`shell`命令



![Snipaste_2022-01-06_23-54-11](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/Snipaste_2022-01-06_23-54-11.png)


#### 魔法函数

查看有哪些魔法函数 : `%lsmagic`

> 一些常用的魔法函数

1. `%time` 计算语句的执行时间
2. `%edit` 使用默认编辑器编辑代码 ( 保存并退出之后就会执行编辑后的代码 )





#### 配置

默认的`ipython`的配置文件路径  `~/.ipython/profile_default/startup/`

如果在 `startup` 文件夹里没有 `startup.py` 文件的话 (文件名无所谓) 就创建一个 

```python
import time
import json
import random
import collections
import sys
import os

print("imported time,json,random,sys,os,collections,re")
```



### Jupyter

> 我们也可以使用谷歌的 [<font color=red>Colaboratory</font> ](https://colab.research.google.com/notebooks/intro.ipynb)(用法和Jupyter一样)

<font color=red>`[!]` 在使用Colaboratory时有些包,其未默认安装,需要我们使用以下方式进行安装:</font> (默认安装 数据分析,机器学习等包)

```python
# 如安装cartopy (!后面接终端命令如 pip , apt-get ...)
!pip install cartopy
import cartopy
```

---



`Jupyter Notebook` 有两种键盘输入模式。

1. **编辑模式**，允许你往单元中键入代码或文本；这时的单元框线是绿色的。
2. **命令模式**，键盘输入运行程序命令；这时的单元框线是灰色。

#### 命令模式

>  (按键 Esc 开启)快捷键

|                        |                              |
| ---------------------- | ---------------------------- |
| <kbd>Enter</kbd>       | 转入编辑模式                 |
| <kbd>Shift-Enter</kbd> | 运行本单元,并选中下个单元    |
| <kbd>Ctrl-Enter </kbd> | 运行本单元                   |
| <kbd>Alt-Enter</kbd>   | 运行本单元并在其下插入新单元 |
| <kbd>A</kbd>           | 在上方插入新单元             |
| <kbd>B</kbd>           | *在下方插入新单元*           |
| <kbd>C</kbd>           | 复制选中的单元               |
| <kbd>Y </kbd>          | 单元转入代码状态             |
| <kbd>M </kbd>          | 单元转入markdown状态         |
| <kbd>R</kbd>           | 单元转入raw状态              |







14. **Up :** 选中上方单元
15. **K :** 选中上方单元
16. **Down :** 选中下方单元
17. **J :** 选中下方单元
18. **Shift-K :** 扩大选中上方单元
19. **Shift-J :** 扩大选中下方单元
20. **A :** 在上方插入新单元
21. **B :** 在下方插入新单元
22. **X :** 剪切选中的单元
23. **C :** 复制选中的单元
24. **Shift-V :** 粘贴到上方单元
25. **V :** 粘贴到下方单元
26. **Z :** 恢复删除的最后一个单元
27. **D,D :** 删除选中的单元
28. **Shift-M :** 合并选中的单元
29. **Ctrl-S :** 文件存盘
30. **S :** 文件存盘
31. **L :** 转换行号
32. **O :** 转换输出
33. **Shift-O :** 转换输出滚动
34. **Esc :** 关闭页面
35. **Q :** 关闭页面
36. **H :** 显示快捷键帮助
37. **I,I :** 中断Notebook内核
38. **0,0 :** 重启Notebook内核
39. **Shift :** 忽略
40. **Shift-Space :** 向上滚动
41. **Space :** 向下滚动

#### 编辑模式 ( Enter 键启动)下快捷键

1. **Tab :** 代码补全或缩进
2. **Shift-Tab :** 提示
3. **Ctrl-] :** 缩进
4. **Ctrl-[ :** 解除缩进
5. **Ctrl-A :** 全选
6. **Ctrl-Z :** 复原
7. **Ctrl-Shift-Z :** 再做
8. **Ctrl-Y :** 再做
9. **Ctrl-Home :** 跳到单元开头
10. **Ctrl-Up :** 跳到单元开头
11. **Ctrl-End :** 跳到单元末尾
12. **Ctrl-Down :** 跳到单元末尾
13. **Ctrl-Left :** 跳到左边一个字首
14. **Ctrl-Right :** 跳到右边一个字首
15. **Ctrl-Backspace :** 删除前面一个字
16. **Ctrl-Delete :** 删除后面一个字
17. **Esc :** 进入命令模式
18. **Ctrl-M :** 进入命令模式
19. **Shift-Enter :** 运行本单元，选中下一单元
20. **Ctrl-Enter :** 运行本单元
21. **Alt-Enter :** 运行本单元，在下面插入一单元
22. **Ctrl-Shift-- :** 分割单元
23. **Ctrl-Shift-Subtract :** 分割单元
24. **Ctrl-S :** 文件存盘
25. **Shift :** 忽略
26. **Up :** 光标上移或转入上一单元
27. **Down :**光标下移或转入下一单元





### ==Pycharm==

![pycharm](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/pycharm.png)

编辑区代码字体选择

`Source Code Pro`

`Consolas`



#### 插件

1. `Key Promoter X`

```shell
# 该插件会对用户的一些鼠标操作,进行一些快捷键提示 (释放鼠标指日可待!)
```



2. `Code Glance`

```shell
# 该插件会在界面的右方出现
```



3. `Tabnine / kit`

```python
# 代码补全插件
# Tabnine 的全称为 Tabnine AI Code Completion- JS Java Python TS Rust Go PHP & More
```





#### 快捷键

快捷键相关名词

`Caret` : 光标

`rectangular` : 矩形的

<kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>L</kbd> *格式化代码*

<kbd>Alt</kbd> + <kbd>J</kbd>  *一次性选中并修改多个相同的变量*

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>↑/↓</kbd> 将光标处的代码往上/下移动

---

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>-/+</kbd> 将代码完全收缩(折叠)或展开 (不包括import部分)

<kbd>Ctrl</kbd> + <kbd>-/+</kbd> 将光标处的代码块折叠/展开

---

<kbd>Alt</kbd> + <kbd>1</kbd> 将右侧project栏展开或收缩

<kbd>Shift</kbd> + <kbd>Enter</kbd> 任意位置换行

<kbd>Ctrl</kbd> + <kbd>Q</kbd>  查看文档

<kbd>Alt</kbd> + <kbd>Enter</kbd> 智能提示

<kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>U</kbd> 实现一键变量大小写转换

<kbd>Shift</kbd> + <kbd>Enter</kbd> 当前行保持不变并换行



<kbd>Delete</kbd> 将右边的一个字符删除

<kbd>Ctrl</kbd> + <kbd>Delete</kbd>  将右边的字符串删除











> 推荐添加的快捷键



```python
Clone Caret Above # 将光标克隆到上一行  (推荐快捷键) Ctrl+Shift+<
Clone Caret Below # 将光标克隆到下一行  (推荐快捷键) Ctrl+Shift+>
```









#### Debug



### ==Vscode==







## 项目实战

1. 一定先别着急去写代码 *(不然后期的代码逻辑会不严谨,并且代码的维护也会变得很困难)*
2. 明确自己项目的方向与功能 (如图形化界面,命令行工具,还是网站等等...)
3. 根据自己的需求,尽可能多地去寻找相关的资料,文献和相关的库如: [各种领域的Python库或资料](https://github.com/vinta/awesome-python)

4. 熟悉,阅读自己寻找到的相关库,(文献,资料),并选择自己要使用的框架,或者库
5. 有想法,和思路的话,最好先将自己 <font color=red>项目的各个结构,模式设置好</font>

6. 根据结构,模式编写相应功能的代码

如我们要将我们的项目做成命令行的工具 *(这时我们首先要去网上寻找是否有相关的框架,和库)* 如下图:

![python33](https://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/python/Python.assets/python33.png)





### 代码优化



```python
import hashlib

def main():
    digester = hashlib.md5()
    with open('Demo_05.txt','rb') as file_streame:
        data = file_streame.read(1024)
        while data:
            digester.update(data)
            data = file_streame.read(1024)
        print(digester.hexdigest())

if __name__ == '__main__':
    main()
```



优化代码

```python

import hashlib


def main():
    digester = hashlib.md5()
    with open('Demo_05.txt', 'rb') as file_streame:
        file_iter = iter(lambda: file_streame.read(1024), b'')
        for data in file_iter:
            digester.update(data)
        print(digester.hexdigest())


if __name__ == '__main__':
    main()
```

> 编写项目图标时,可以将其弄成列表然后遍历(可以参考scapy里的main.py里的代码)







### Readme/Doc

---

我们可以使用`pydoc`来生成一个基础文档

```shell
python -m pydoc module_name

python -m pydoc -w module_name # 生成 
```

我们也可以使用`help()`函数来

## 杂项

```python
#　将字符串转换成bytearray
byte_array = bytearray(b"flag{This_Isflag}")
# 将数字转换成ASCII码
chr(64)
# 将ASCII转换成数字
ord('a')
# 将列表中的字符串合并在一起
result = ''.join(res)

# 将任何进制转换成10进制
int('10101010',2)
int('1234567',8)
int('ffaa',16)
```

`u/U`:表示unicode字符串 
不是仅仅是针对中文, 可以针对任何的字符串，代表是对字符串进行unicode编码。 
一般英文字符在使用各种编码下, 基本都可以正常解析, 所以一般不带u；但是中文, 必须表明所需编码, 否则一旦编码转换就会出现乱码。 
建议所有编码方式采用utf8

r/R:非转义的原始字符串 
与普通字符相比，其他相对特殊的字符，其中可能包含转义字符，即那些，反斜杠加上对应字母，表示对应的特殊含义的，比如最常见的”\n”表示换行，”\t”表示Tab等。而如果是以r开头，那么说明后面的字符，都是普通的字符了，即如果是“\n”那么表示一个反斜杠字符，一个字母n，而不是表示换行了。 
以r开头的字符，常用于正则表达式，对应着re模块。

b:bytes 
python3.x里默认的str是(py2.x里的)unicode, bytes是(py2.x)的str, b”“前缀代表的就是bytes 



```python
# 16进制的bytearray
hex_array = bytearray.fromhex(end_data)
```









```python
## 2.输入语句的使用

> python里使用input内置函数接收用户的输入

+ <font color=#ff585d face=楷体>input()    ---括号里写提示信息</font>



---

## 3.不同进制数据的表示方式

==python里的数据类型==

><font color=#41b6e6 face=楷体>整型(int)  浮点型(float)  复数(complex)</font>  
>
><font color=#41b6e6 face=楷体>字符串(str)  布尔(bool)  列表(list)  字典(dict)  集合(set)  元组(tuple)   </font>



​```python
a = 0b101010101  #以0b开头的数字表示的是二进制(BIN)
a = 0o101010101  #以0o开头的数字表示的是八进制(OCT) [在python2里以0开头得数字也是八进制]
a = 101010101    #python默认使用10进制(DEC)
a = 0x2abcdef19  #以0x开头的数字表示的是十进制(HEX)  
​```



使用内置函数实现进制转换

​```python
c = 100  (在pycharm里可以使用bin(c).print快速输入代码)
print(bin(c)) #使用bin内置函数可以将数字转换为二进制
print(oct(c)) #使用oct内置函数可以将数字转换为八进制
print(hex(c)) #使用hex内置函数可以将数字转换为十六进制
​```

pass关键字在python里没有意义,只是单纯用来占位,保证语句的完整

python里可以使用连续的区间判断

eg: 60 > score >=0

ctrl+alt+l  :快速格式化代码

alt/ctrl+shift+上下箭头  :上下移动一行代码

ctrl+/ 快速注释

ctrl + 左右键  :快速跳转到行首/行尾

**一次性选中并修改多个相同的变量**

1.将光标置于要修改的变量名后面
2.多次按alt+j，这样就可以在相同的变量名后面添加光标
3.此时可以同时删除并修改这些已经选中的变量名了。






try:
    import requests
    HAS_REQUEST = True
except ImportError:
    HAS_REQUEST = False

```

> 建立一个微型的web服务

```python
python -m http.server
#将当前目录设为一个小型的web服务

```

> 在linux里编写Python时,一般会配置vim的配置文件

1. 在家目录下建立一个vim配置文件 `.vimrc`

2. 在配置文件里加入如下这几行代码

```shell
set nu # 设置行号
syntax on # 高亮显示代码
set ts=4 # 设置一个制表键为4个空格的大小(在vim里默认是8个大小)
set expandtab # 将一个制表符改为多个空格的形式
set autoindent # 自动缩进代码
set ruler # 在右下方显示光标的位置
set nohls # 

nc -nvv 132.232.82.54 2021

`


```python
from collections import namedtuple
# Python code to demonstrate namedtuple()

from collections import namedtuple

# Declaring namedtuple()
Student = namedtuple('Student', ['name', 'age', 'DOB'])

# Adding values
S = Student('Nandini', '19', '2541997')

# Access using index
print("The Student age using index is : ", end="")
print(S[1])

# Access using name
print("The Student name using keyname is : ", end="")
print(S.name)

# the output
The Student age using index is : 19
The Student name using keyname is : Nandini
```



namedtuple
