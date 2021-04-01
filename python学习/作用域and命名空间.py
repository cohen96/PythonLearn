def func1():
    return 20

#scope -生效区域
#2种：全局与函数
#全局：执行时创建，结束时销毁。在函数以外的区域/全局变量
a = 100
#函数：调用时创建，每次调用生成新的scope
a = 1  
def fn2(): #从函数内部可以访问外部定义的变量 使用变量时 优先在当前作用域中寻找 无则>向上<寻找
    def fn3():
        global a#修改全局使用global
        a = 2
        print(a)
    fn3()
fn2()

# namespace 变量存储的位置- 每一个作用域和命名空间一一对应 只是一个容器
s = locals() #一个字典

def fn4():
    c = 3
    s1 = locals() #func的命名空间
    s2 = globals() #全局的命名空间



