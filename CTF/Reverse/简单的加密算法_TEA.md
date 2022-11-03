TEA 是 `(Tiny Encryption Algorithm)` 的缩写，以加密解密速度快，实现简单著称。 <font color="red"> TEA算法每一次可以操作64bit(8byte)，采用128bit(16byte)作为key </font> ，算法采用迭代的形式， <font color="red"> 推荐的迭代轮数是64轮，最少32轮。(可以改变) </font> TEA系列算法中均使用了一个DELTA常数，但DELTA的值对算法并无什么影响，只是为了避免不良的取值，推荐DELTA的值取为黄金分割数(5√-2)/2与232的乘积， <font color="red"> 取整后的十六进制值为0x9e3779B9</font>，用于保证每一轮加密都不相同。为解决TEA算法密钥表攻击的问题，TEA算法先后经历了几次改进，从XTEA到BLOCK TEA，直至最新的XXTEA。

+ XTEA 也称做 TEAN，它使用与TEA相同的简单运算，但四个子密钥采取不正规的方式进行混合以阻止密钥表攻击。
+ Block TEA算法可以对32位的任意整数倍长度的变量块进行加解密的操作，该算法将XTEA轮循函数依次应用于块中的每个字，并且将它附加于被应用字的邻字。
+ XXTEA 使用跟Block TEA相似的结构，但在处理块中每个字时利用了相邻字，且用拥有两个输入量的MX函数代替了XTEA轮循函数。上面提到的相邻字其实就是数组中相邻的项。
+ 只要会处理 TEA,XTEA和XXTEA也是同理.

