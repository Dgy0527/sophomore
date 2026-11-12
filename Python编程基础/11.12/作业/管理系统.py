students=[]

while True:
    print("====================")
    print("学生管理系统 V10.0")
    print("1.添加学生信息")
    print("2.删除学生信息")
    print("3.修改学生信息")
    print("4.查询所有学生信息")
    print("0.退出系统")
    print("====================")

    shuru=input("请输入你要执行的功能(0~5):")
    



    # 1、添加
    if shuru == "1":
        print("=====请输入你要添加的学生的信息=====")

        name=input("请输入姓名：")
        id=input("请输入学号：")
        clas=input("请输入学生班级：")
        tele=input("请输入电话号码：")
        print("=====添加成功=====")

        stu={'name':name,'id':id,'class':clas,'tele':tele}
        students.append(stu)
        #print(students)



    # 2、删除
    elif shuru == "2":
        if len(students) == 0:
            print("学生信息表为空")
        else:
            del_id=input("请输入你要删除的学生学号：")
            found=False
            for stu in students:
                if stu["id"] == del_id:
                    students.remove(stu) 
                    print("删除成功")
                    found=True
                    break
            if not found:
                print("没有该学号的学生")



    # 3、修改
    elif shuru == "3":
        if len(students) == 0:
            print("学生信息表为空")
        else:
            mod_id=input("请输入你要修改的学生学号：")
            found=False
            for stu in students:
                if stu["id"] == mod_id:
                    stu["name"] = input("请输入修改后的学生姓名：")
                    stu["class"] = input("请输入修改后的学生班级：")
                    stu["tele"] = input("请输入修改后的学生电话号码：")
                    print("修改成功")
                    found=True
                    break
            if not found:
                print("没有该学号的学生")



    # 4、查询
    elif shuru == "4":
        if len(students) == 0:
            print("=====学生信息表为空=====")
        else:
            print("="*20)
            print("学号  姓名  班级  电话")
            for stu in students:
                print(f"{stu['id']}  {stu['name']}  {stu['class']}  {stu['tele']}")
            print("="*20)



    # 0、退出
    elif shuru == "0":
        print("=====已退出=====")
        break



    # 其他
    else:
        print("=====请输入正确的数字=====")
