## Makefile

```make
test:
	@echo "hello test"
all: 
	@echo "hello all"
```
make 不带目标，那默认是执行第一个目标


makefile 伪对象 `.PHONY:`

如果在当前目录存在一个与makefile里执行目标同名的文件的话会报错

```make
.PHONY: clean

```
依赖关系是从左到右


## Cmake
