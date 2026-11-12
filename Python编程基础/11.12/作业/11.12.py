"""
# 方法1
shuru=input("请输入一个数字(0~9):")

num_dict={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}

result="".join([num_dict[char] for char in shuru])

print("你输入的数字是：",result)
"""





"""
# 方法2
shuru=input("请输入一个数字(0~9):")

num_dict={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}

result=""

for char in shuru:
    result=result+num_dict[char]
print("你输入的数字是:",result)
"""



"""
# 当输入的不是数字时而报错的修改代码
num_dict={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}

while True:
    shuru=input("请输入一个数字(0~9):")

    if shuru in num_dict:
        print("你输入的数字是:",num_dict[shuru])
        break   # break可省略,一直执行数字转换
    else:
        print("请输入正确的数字!")
"""



# 进阶
num_dict={'0':'零','1':'壹','2':'贰','3':'叁','4':'肆','5':'伍','6':'陆','7':'柒','8':'捌','9':'玖'}

def convert_num(num_str):
    result=""
    for char in num_dict:
        if char.isdigit():
            result+=num_dict[char]
        else:
            return "请输入正确的数字"
    return result

if __name__=="__main__":
    shuru=input("请输入一个数字(0~9):")
    print(f"你输入的数字是:"{convert_num(shuru)})
