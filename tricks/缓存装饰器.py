# coding=utf-8
"""
缓存是一种将定量数据加以保存以备迎合后续请求的处理方式, 旨在加快数据的检索速度.
functool模块中的lru_cache装饰器可以实现缓存功能.

lru_cache原型如下:
@functools.lru_cache(maxsize=None, typed=False)

使用functools模块的lur_cache装饰器,可以缓存最多maxsize个此函数的调用结果,从而提高程序执行的效率,特别适合于耗时的函数.
参数maxsize为最多缓存的次数,设置为None表示无限制,否则设置为2^n; 如果typed=True则不同参数类型的调用将分别缓存, 例如f(3)和f(3.0).
被lru_cache装饰的函数会有cache_clear和cache_info两个方法,分别用于清除缓存和查看缓存信息.
"""

from functools import lru_cache


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
print(add(2, 3))

# 从打印结果可以看出当第二次调用add(1, 2)时, 并没有执行函数体, 而是直接返回缓存的结果
