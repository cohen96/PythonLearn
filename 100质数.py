# 100内的质数

i = 2
while i <= 100 :
    flag = True #记录i的状态是否为质 默认是
    j = 2
    while j < 0.5 * i :
        if i % j ==0 :
            flag = False #余0=非质
        j += 1
    if flag == True :
        print(i)
    i += 1
