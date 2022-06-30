## 一些实用的内置库

### logging


```
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='/tmp/output.log',
    datefmt='%Y/%m/%d %H:%M:%S',
    format=
    '%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')

```

```
import logging
from logging.handlers import HTTPHandler
import sys

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)

# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)

# FileHandler
file_handler = logging.FileHandler('output.log')
file_handler.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# HTTPHandler
http_handler = HTTPHandler(host='localhost:8001', url='log', method='POST')
logger.addHandler(http_handler)

# Log
logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')
```

```
%(levelno) s：打印日志级别的数值。
%(levelname) s：打印日志级别的名称。
%(pathname) s：打印当前执行程序的路径，其实就是 sys.argv [0]。
%(filename) s：打印当前执行程序名。
%(funcName) s：打印日志的当前函数。
%(lineno) d：打印日志的当前行号。
%(asctime) s：打印日志的时间。
%(thread) d：打印线程 ID。
%(threadName) s：打印线程名称。
%(process) d：打印进程 ID。
%(processName) s：打印线程名称。
%(module) s：打印模块名称。
%(message) s：打印日志信息。
```

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

### binascii


```python
import binascii

# the string must be double
hex_array = bytearray(binascii.a2b_hex("1aaa")) 


```






## 一些 Python 小特性
