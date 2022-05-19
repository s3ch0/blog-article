## 一些实用的内置库

### collections

#### Counter
#### namedtuple


### functools

####  partial


### itertools


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








## 一些 Python 小特性
