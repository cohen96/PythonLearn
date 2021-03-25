from time import *
begin = time()
i = 2
while i <= 50000 :
    flag = True #记录i的状态是否为质 默认是
    j = 2
    while j <= i ** 0.5 :
        if i % j ==0 :
            flag = False #余0=非质
            break
        j += 1
    if flag == True :
        pass
        #print(i)
    i += 1
end = time()
print('time?', end - begin , "s")