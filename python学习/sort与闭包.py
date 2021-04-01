# sort(): 事实上的<排序
l = [4, 7, '1', '3', 2, 6, 5]
l2 = l.sort(key=int)

l1 = (4, 5, 6, 1, 3, 2)

l3 = sorted(l1, key=int)
print(l3)

# 形成闭包的要件：
# 1.函数嵌套
# 2.将内部的函数return
# 3.内部函数必须使用外部函数的变量

# 创建函数求平均值
# 外层


def avgnum1():
    number = []  # 闭包 用于保存数字
    # 创建求avg的函数

    def avgnum2(n):
        number.append(n)
        return sum(number)/len(number)
    return avgnum2


avgnum2 = avgnum1()

print(avgnum2(10))
print(avgnum2(20))
print(avgnum2(30))
print(avgnum2(1))
