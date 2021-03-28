# exercise

# 1.查询 显示全部
# 2.添加 添加1个
# 3.删除 删除一个
# 4.quit

# 创建一个list 以str保存
list = ['Adam\t20\tmale']
print('-'*20, 'Welcome!', '-'*20)
while True:
    print('\t 1.显示')
    print('\t 2.add')
    print('\t 3.del')
    print('\t 4.quit')
    choose = input('请输入1-4: ')
    print('-----')

    # 分支
    if choose == '1':
        # inquiry
        print('\tNo.\tname\tage\tgender')
        # 序号生成
        n = 1
        for emp in list:
            print(f'\t{n}\t{emp}')
            n += 1
    elif choose == '2':  # 添加
        Name = input('输入name')
        Age = input('age?')
        Gender = input('Gender?')
        # 拼接3个信息为1个变量,然后插入到list
        emp = f'{Name}\t{Age}\t{Gender}'
        # 确认信息
        print('将添加该人')
        print('------')
        print('name\tage\tgender')
        print(emp)
        print('-----')
        Confirm = input('是否确认？Y/N')
        if Confirm == 'Y' or 'y':
            list.append(emp)
            print('成功添加')
        else:
            print('ok')
    elif choose == '3':
        # 根据No. delete
        DeleteNum = int(input('请输入要del的No.'))
        # 是否合法的No
        if 0 < DeleteNum <= len(list):
            DeleteIndex = DeleteNum - 1
        # 确认提示
        print('将删除该人')
        print('-----')
        print(f'{DeleteNum}\t{list[DeleteIndex]}')
        print('-----')
        DeleteConfirm = input('Y/N')
        if DeleteConfirm == 'Y' or 'y':
            list.pop(DeleteIndex)
            print('删除成功')
        else:
            print('已取消')
    elif choose == '4':
        input('press enter to quit')
        break
    else:
        print('输入数字有误，重选！')
    print('-'*30)
