# Java Study


> Java的特点: 简单易学,安全性高,跨平台,多线程

[Awesome java](https://github.com/akullpp/awesome-java)

```java
class A{
    int i;
    int j;
}
class TestMemo{
    public static void main(String[] args){
        
        //new A(): 在堆中动态分配一块区域,被当做了A对象
        //aa 本身的内容是在栈中分配的
        //堆中内存的地址赋给了aa,也就是aa指向堆中的内容,aa代表了堆中的内存
        
        A aa = new A(); // 相当于 (A *)malloc(sizeof(A))
        aa.i = 10; // aa.i代表: aa这个静态指针变量所指向的动态内存中A对象的i这个成员
        aa.j = 20;
        System.out.printf("%d,%d\n",aa.i,aa.j) // 10.20
    }
      
    
}

```

## 类的访问控制符

类的访问控制符有四种:

1. public  *可以通过外部访问方式访问类内部的public成员*
2. protect
3. 默认(不加任何修饰符)
4. private   *不可以通过外部访问方式访问类内部的private成员*

在一个类的内部,所有的成员可以互相访问,访问控制符是透明的,==访问控制符是针对外部访问而言的==

外部访问包括两种方式:

+ 通过类名访问类内部的成员
+ 通过类对象名访问类内部成员





```bat
# 当运行bat脚本文件时,显示找不到javaw文件时,需要在bat文件里添加路径 如:
@echo off 
set path=C:\Program Files\Java\jdk1.8.0_301\bin # 添加这一条
start javaw -Dfile.encoding=utf-8 -Xbootclasspath/p:burp-loader-keygen.jar -Xmx1024m -jar burpsuite_pro_v2.0beta.jar
```



安装时需要添加

```shell
JAVA_HOME --> 对应的安装的jdk路径
PATH      --> 添加两个 1. %JAVA_HOME%/bin 2. %JAVA_HOME%/jre/bin #也可使用绝对路径

```

编写: 我们将编写的java代码保存在以".java"结尾的源文件中

编译: 使用javac.exe命令编译我们的java源文件>格式: `javac 源文件名.java`

运行: 使用java.exe命令解释运行我们的字节码文件. 格式: java 类名

在一个源文件中可以声明多个class 但是,只能最多有一个类声明为public,而且要求声明为public的类的类名必须与源文件名相同

程序的入口是main()方法.格式是固定的.

输出语句

`System.out.println("zhouhao");` : 先输出数据,然后换行

`System.out.print("zhouhao");` : 只输出数据（不换行)

```java
public class tmp01 {
  public static void main(String[] args) {
    System.out.println("zhouhao");
    System.out.print("zhouhao");
  }
}
```



快捷键

<kbd>Ctrl</kbd>+<kbd>Delete</kbd> : 将光标后面的代码删除,直到下一行



构造函数

就是每次在用类创建对象时会执行的代码

而构造函数的格式为:

`public 当前类的类名(){}` 相当于声明函数,只是函数名为相应类的名字

```java
class A{
    public A(){
        System.out.printf("---test---");
    }
}
class Demo01{
    public static void main(String[] args){
        A aa = new A();  // 会输出"---test---" 
    }
    
}
```

```java

this 关键字:
 
```

## IDEA

### 插件

```shell
# Codota           						：智能提示插件
# Key Promoter X   						：快捷键提示插件
# CodeGlance       						：代码侧边栏
# Lombok           						：简化臃肿代码插件
# CamelCase        						：驼峰命名和下划线命名转换
# Alibaba Java Coding Guidelines		：阿里巴巴代码规范检查插件
# SonarLint 							: 代码质量检查插件
# Save Actions							: 代码格式化插件
# Grep Console 							: 自定义控制台输出格式插件
# MetricsReloaded						: 代码复杂度检查插件
# Statistic								: 代码统计插件
# Translation							: 翻译插件
# Rainbow Brackets      				: 彩色括号插件

```



自定义创建 `live template` ,快速写代码
