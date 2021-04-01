# 递归式的函数
# 创建函数求n的阶乘
# while True:
#     n = int(input('输入n 求阶乘'))
#     for i in range(1,n):
#         n *= i
#     print(n)


def fn1(n):
    result = n
    for i in range(1, n):
        result *= i
    return result


# print(fn1(5))

#递归：自己引用自己
#递归式函数
#无穷递归=溢出
# def fn2():
#     fn2()
#2个要件：
# 基线条件：可分解为的最小问题 满足时停止递归 
# 递归条件：将问题分解的条件
def fn2(num):
    if num == 1:#基线条件
        return 1
    return num * fn2(num - 1)

# print(fn2(6))

#创建一个函数 power 来为n做i次幂运算(i>=1)
def power(n,i):
    if i == 1:
        return n
    return n * power(n,(i-1))

# print(power(2,4))

#创建一个函数 检查字符串是否是回文字符串(like 'level') 是则True
# 检查第一个和最后一个字符 然后递归： alevela -- level -- eve 
def check(x):
    '''
    检查字符串是否是回文，是则返回True，否则False
    参数x
    '''
    #基线
    if len(x) < 2:
        return True
    elif x[0] != x[-1]:
        return False
    #递归
    return check(x[1:-1])#切片原字符串
    

