d = {}
print('歡迎使用字典')
while True:
    print('1.建立辭典')
    print('2.列出所有單字')
    print('3.英翻中')
    print('4.中翻英')
    print('5.測驗')
    print('6.離開')
    
    option = input('請輸入選項: ')
    
    if option == '6':
        break
    elif option == '1':
        while True:
            voc = input('請輸入英文單字(按0離開)')
            if voc == '0':
                break
            if voc not in d:
                voc_ch = input('請輸入中文')
                d[voc] = voc_ch
            else:
                print('已存在')
    elif option == '2':
        s = sorted(d)
        for i in s:
            print(i,':',d[i])
    elif option == '3':
        voc = input('請輸入英文單字')
        if voc in d:
            print(d[voc])
        else:
            print('單字不存在')
    elif option == '4':
        got = False
        ch = input('請輸入中文單字')
        for k,v in d.items():
            if ch == v:
                print(k)
                got = True
            if got == False:
                print('單字不存在')
    elif option == '5':
        score = 0
        for k,v in d.items():
            print(k)
            ans = input('請輸入中文')
            if ans == v:
                print('答對')
                score = score + 1
            else:
                print('答錯')
        print('分數: ',score)