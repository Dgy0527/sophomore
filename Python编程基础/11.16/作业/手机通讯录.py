tele_book=[]

while True:
    print("---1、添加联系人---")
    print("---2、查找联系人---")
    print("---3、修改联系人---")
    print("---4、删除联系人---")
    print("---5、显示已有的联系人---")
    print("---6、退出---")

    tianjia={}

    code=input("------请输入你要运行的功能：------")

    if code == "1":
        name=input("请输入你要添加联系人的姓名：")
        gender=input("请输入你要添加联系人的性别：")
        tele=input("请输入你要添加联系人的电话号码：")
        tianjia.update(name=name,gender=gender,tele=tele)
        tele_book.append(tianjia)
        print("---添加成功---")

    elif code =="2":
        search_name=input("请输入你要查找的姓名：")
        found=False
        for i in range(len(tele_book)):
            if tele_book[i]["name"] == search_name:
                print(f"'name':{tele_book[i]['name']},'gender':{tele_book[i]['gender']},'tele':{tele_book[i]['tele']}")
                found=True
                break
        if not found:
            print("无此人")  

    elif code == "3":
        xiugai_name=input("请输入你要修改联系人的姓名：") 
        new_name=input("请输入你要新修改的姓名：")
        new_gender=input("请输入你要新修改的性别：")
        new_tele=input("请输入你要新修改的电话号码：")
        
        found=False
        for i in range(len(tele_book)):
            if tele_book[i]["name"] == xiugai_name:
                tele_book[i]["name"] = new_name
                tele_book[i]["gender"] = new_gender 
                tele_book[i]["tele"] = new_tele
                found=True
                break
        if found:
            print("---修改成功---")
        else:
            print("无此人")

    elif code =="4":
        del_name=input("请输入你要删除联系人的姓名：")
        for dict in tele_book:
            if del_name in dict.values():
                tele_book.remove(dict)
                print("---删除成功---")
                break
        else:
            print("---无此人---")

    elif code == "5":
        print(tele_book)

    elif code == "6":
        print("---已退出---")
        break

    else:
        print("---请输入正确的数字---")
        continue
