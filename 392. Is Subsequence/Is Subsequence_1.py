# @author:leacoder 
# @des:  借助迭代器和生成器 判断子序列

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
    	# 判断 s 是否为 t 的子序列。
    	b = iter(t)  # 迭代器
    	return all(((i in b) for i in s ))

'''
代码扩展
def is_subsequence(s, t):
    b = iter(t)   # 把 t 转化成了⼀个迭代器
    print(b)

    gen = (i for i in s)  # 产生一个生成器， 这个生成器可以遍历对象 s
    print(gen)

    for i in gen:
        print(i)

    gen = ((i in b) for i in s)
    print(gen)

    for i in gen:
        print(i)

    return all(((i in b) for i in s))

b = iter(b) ， 把列表 b 转化成了一个迭代器， 
gen = (i for i in s) 产生一个生成器， 这个生成器可以遍历对象 s，能够输出 1, 3, 5。
(i in b)可以联想到 for in 语句。
(i in b) ， 大致等价于

while True:
    val = next(b)
    if val == i:
        yield True
巧妙地利用了成器的特性， next() 函数运行的时候， 保存了当前的指针。

那么((i in b) for i in s)可以理解为：遍历a中元素 i，并在b中查找元素 i 是否存在。
由于next() 函数和yield 成器的特性,如果 b 存在 i 返回True并保存当前指针不存在返回False
（下一次查找从保存的指针开始继续查找，直到s 或者 b 遍历结束），这些True或False产生一个迭代器。

最后的 all() 函数，判断一个迭代器的元素是否全部为 True， 如果是则返回 True， 否则就返回 False。

'''