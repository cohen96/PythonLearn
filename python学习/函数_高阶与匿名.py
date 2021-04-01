# 高阶:接收函数作参数or 函数作为返回值
# 筛选 并返回列表
l = [1, 2, 3, 4, 5, 6, 7]


def fn1_odd(n):
    if n % 2 != 0:
        return True


def fn2_even(n):
    if n % 2 == 0:
        return True


def fn3_bigger_than_5(n):
    if n > 5:
        return True


def fn4_multiples_of_3(n):
    if n % 3 == 0:
        return True


def fn(func_choice, l):
    new_l = []
    for n in l:
        if func_choice(n):
            new_l.append(n)
    return new_l


print(fn(fn1_odd, l))
print(fn(fn2_even, l))
print(fn(fn3_bigger_than_5, l))
print(fn(fn4_multiples_of_3, l))

# filter(函数，可遍历的对象)
# 函数：过滤规则
# 返回值：过滤出的结构

print(list(filter(fn1_odd, l)))
print(list(filter(fn2_even, l)))
print(list(filter(fn3_bigger_than_5, l)))
print(list(filter(fn4_multiples_of_3, l)))

# 匿名函数 lambda(参数:返回值) 当参数用！创建简单函数 也就无需定义函数 只用一次的函数

print((lambda a, b: a * b)(3, 4))

#for fn1_odd:
print(list(filter(lambda n: n % 2 != 0, l)))

#map()对可迭代（遍历）对象的所有元素操作，然后添加到新对象并返回
#定义域 range(6)

y = list(map(lambda i : 2*i+3, l))


