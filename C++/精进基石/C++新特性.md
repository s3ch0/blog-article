
## 智能指针
C++程序设计中使用堆内存是非常频繁的操作
+ <font color='red' face=Monaco size=3>堆内存的申请和释放都由程序员自己管理。</font> 
+ 程序员自己管理堆内存可以提高了程序的效率
  + **但是整体来说堆内存的管理是麻烦的**
 
 
 C++11中引入了智能指针的概念，方便管理堆内存。**使用普通指针，容易造成堆内存泄露（忘记释放），二次释放，程序发生异常时内存泄露等问题等，使用智能指针能更好的管理堆内存。**

---

> C++里面的四个智能指针:

~~`auto_ptr`~~,**`unique_ptr`,`shared_ptr`, `weak_ptr`** 其中后三个是C++11支持，并且第一个已经被C++11弃用。


### `shared_ptr` 共享的智能指针

<font color='red' face=Monaco size=3>`shared_ptr` 是最常使用，也是使用最多的</font>

`std::shared_ptr` 使用引用计数，每一个 `shared_ptr` 的拷贝都指向相同的内存。再最后一个 `shared_ptr` 析构的时候，内存才会被释放。

`shared_ptr` 共享被管理对象，同一时刻可以有多个 `shared_ptr` 拥有对象的所有权，当最后一个 `shared_ptr` 对象销毁时，被管理对象自动销毁。

简单来说，`shared_ptr`实现包含了两部分，
+ 一个指向堆上创建的对象的裸指针，`raw_ptr`
+ 一个指向内部隐藏的、共享的管理对象。`share_count_object`

第一部分没什么好说的，第二部分是需要关注的重点：
use_count，当前这个堆上对象被多少对象引用了，简单来说就是引用计数

```bash
g++ -o main main.cpp -std=c++11
```

## 右值引用

## 匿名函数

## STL 容器

## 正则表达式

## thread 