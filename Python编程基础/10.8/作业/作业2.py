print('欢迎使用此文字排版工具')
shuru=input('请输入你要排版的文字:\n')

shanchu=shuru.replace(" ","")
tihuan=shuru.replace(",","，").replace(".","。").replace("?","？").replace("!","！").replace(":","：")
fenge=shuru.splitlines()
daxie=shuru.upper()

while True:
    gongnen = input('请输入你要选择的功能(删除空格（1）、英文标点替换（2）、段落分割（3）、字母大写（4）和退出（0）:\n')
    if gongnen=="1":
        print(f'删除空格之后的文字：{shanchu}')
    elif gongnen=="2":
        print(f'标点替换后的文字是：{tihuan}')
    elif gongnen=="3":
        print(f'段落分割后的文字是：{fenge}')
        count = 1  # 手动控制段落编号
        for para in fenge:
            if para.strip() != "":  # 只有当这一段不是空白时才打印
                print(f'第{count}段：{para}')
                count += 1  # 打印完一段，编号加1
    elif gongnen=="4":
        print(f'字母大写后的文字是：{daxie}')
    elif gongnen=="0":
        print('你已退出')
        break
    else:
        print('无效选项,请输入正确数字')




