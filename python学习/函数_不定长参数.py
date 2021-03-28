# 不定长参数
# 带*参数后的所有参数必须使用关键字传递
def sum(*a):
    result = 0
    for n in a:
        result += n
    print(result)


def sum2(a, b, *c):
    print(a, b, c)


def sum3(a, b, *c, d=4):
    print(a, b, c,d)


def sum4(*, a, b, c):
    print(a, b, c)


sum4(a=1, b=2, c=3)


def sum5(b,c,**a): #只能有一个**,且必须在最后。保存在字典中
    print(a,b,c)


sum5(n=1, c=3)

def fn(a,b,c):#解包
    print(a,b,c)

t= (5,10,15)

fn(*t)#tuple解包

d={'a':100,'b':200,'c':300}
fn(**d)#dict解包

