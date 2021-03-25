# 100内的质数
i = 2
while i <= 100 :
    flag = True
    j = 2
    while j < 0.5 * i :
        if i % j ==0 :
            flag = False
        j += 1
    if flag == True :
        print(i)
    i += 1

