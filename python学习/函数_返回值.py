def sum(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result
    print('test')
r = sum(1,2,3,4,5)
print(r)
#return执行，函数结束

print(sum)  # <function sum at 0x0000024983810840>
print(sum())#0
